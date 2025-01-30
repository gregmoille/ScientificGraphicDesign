
import pickle as pkl
import pandas as pd
import numpy as np
from scipy import signal
from scipy import constants as cts
from glob import glob

import matplotlib as mpl
import plotly.graph_objs as go
import plotly.io as pio
from plotly.subplots import make_subplots
import plotly.graph_objects as go
pio.templates.default = "plotly_white"
from matplotlib.colors import LinearSegmentedColormap, to_hex
from itertools import cycle
from IPython.core.display import display, HTML

def getDisp(data, RR):
    try:
        data['neff_r'] = data.M*cts.c/(2*np.pi*RR*data.freq)
        Δf = np.gradient(data.freq)
        data['ng'] =cts.c/(2*np.pi*RR*Δf)
        vg = cts.c / data.ng
        d_vg = np.gradient(1 / vg)
        data['Disp'] = -((data.freq ** 2) / cts.c) * d_vg / Δf
    except Exception as err:
        print(err)

    return data



def getDint(data, fpmp = None, Mpmp = None, D1 = None):
    try:
        freq = data.freq.values
        M = data.M.values
        ind_nan = np.isnan(freq)
        M[ind_nan] = 0
        freq[ind_nan] = 0

        ω = 2 * np.pi * freq
        if fpmp:
            indx_pmp = np.argmin(np.abs(fpmp - freq))
        else:
            indx_pmp = np.argmin(np.abs(M - Mpmp))
        νpmp = freq[indx_pmp]
        μ = M - M[indx_pmp]
        ΔM = np.array([-2, -1, 0, 1, 2])
        # Δν = freq - νpmp

        Dfit = np.polyfit(μ[indx_pmp + ΔM], \
                          - 2*np.pi*νpmp + 2*np.pi*freq[indx_pmp + ΔM], \
                          2)
        FSR = Dfit[1]/(2*np.pi)
        D2 = Dfit[0]*2
        if not D1: 
            D1 = Dfit[1]
        Dint = ω - (νpmp * 2 * np.pi + D1 * μ)

        data['Dint'] = Dint
        data['FSR'] = FSR
        data['μ'] = μ
        data['D2'] = D2
        data['β2'] = -D2*cts.c/(2*np.pi*freq**2)
    except Exception as err:
        print('Dint processing error')
        print(err)
    return data

def getδf(dum):
    freq = dum.freq.values
    M = dum.M.values
    µ = dum.µ.values
    dum2 = [None]*freq.size

    cond = np.logical_and(µ>=0, µ<=-µ[0])
    cond = np.logical_and(cond, µ>-µ[-1])

    fpmp = freq[cond][0]
    idxpmp = np.arange(freq.size)[cond][0]

    for ii in np.arange(freq.size)[cond]:
        Δf = -2*fpmp + (freq[ii] + freq[2*idxpmp-ii])
        dum2[ii] = Δf
        dum2[2*idxpmp-ii] = Δf
    #ipdb.set_trace()
    dum['δf']= dum2

    return dum


def getSFG(dum, fpmp = None, Mpmp = None):
    freq = dum.freq.values
    M = dum.M.values
    µ = dum.µ.values
    dum2 = [None]*freq.size


    if fpmp:
        indx_pmp = np.argmin(np.abs(fpmp - freq))
    else:
        indx_pmp = np.argmin(np.abs(M - Mpmp))
    fpmp = freq[indx_pmp]
    Mpmp = M[indx_pmp]


    for ii in np.arange(freq.size):
        fsig = freq[ii]
        Msig = M[ii]
        Msfg = Msig+Mpmp
        if Msfg<=M[-1]:
            idx_sfg =  np.argmin(np.abs(M - Msfg))
            f_sfg = freq[idx_sfg]

            Δf = f_sfg - (fsig+fpmp)
            dum2[ii] = Δf
        else:
            break
    #ipdb.set_trace()
    dum['δf_sfg']= dum2

    return dum


def ProcessDispSim(H, RW, funfname, fpmp=193e12, RR = 23e-6,
                   D1 = None, doDisp = True, doDint = True, doOPO = False,
                   doSFG = False):
    if not(type(H) == list or type(H) == np.ndarray):
        H = [H]
    if not(type(RW) == list or type(RW) == np.ndarray):
        RW = [RW]

    df = pd.DataFrame(columns = ['H', 'RW', 'M',
                                'freq', 'gamma',
                                'epsCore', 'epsClad', 'epsSub', 'Aeff',
                                'neff_r', 'ng', 'Disp',
                                'FSR', 'D2', 'β2', 'Dint' , 'μ'], 
                     dtype='float')

    for h in H:
        for rw in RW:
            dum = pd.read_csv(funfname(h, rw),
                              skiprows=5,
                              names = ['M', 'freq', 'gamma',
                                       'epsCore', 'epsClad', 'epsSub', 'Aeff'], sep = '\s+', 
                             dtype='float')
            dum = dum.astype('float')
            dum['RW'] = rw
            dum['H'] = h
            dum['neff_r'] = np.nan
            dum['ng'] = np.nan
            dum['Disp'] = np.nan
            dum['FSR'] = np.nan
            dum['Dint'] = np.nan
            dum['μ'] = np.nan
            df = pd.concat([df, dum])

    #df = df.set_index(['H', 'RW'])
    if doDisp:
        df = df.groupby(['H', 'RW']).apply(lambda x: getDisp(x, RR))
        if doDint:
            df = df.groupby(['H', 'RW']).apply(lambda x: getDint(x, fpmp = fpmp, D1 = D1))
            if doOPO:
                df = df.groupby(['H', 'RW']).apply(lambda x: getδf(x))
            if doSFG:
                df = df.groupby(['H', 'RW']).apply(lambda x: getSFG(x, fpmp = fpmp))
    # df = df.set_index(['H', 'RW','M'])

#     if len(H) == 1:
#         df = df.loc[H[0]]

    return df


def ProcessCoupling(H, RW, funfname, fpmp=193e12, RR = 23e-6,
                   doDisp = True, doDint = True, doOPO = False,
                   doSFG = False):

    if not(type(H) == list or type(H) == np.ndarray):
        H = [H]
    if not(type(RW) == list or type(RW) == np.ndarray):
        RW = [RW]

    df = pd.DataFrame(columns = ['H', 'RW', 'M',
                                'freq', 'gamma',
                                'epsCore', 'epsClad', 'epsSub', 'Aeff', 'P11', 'P12', 'P21', 'P22', 'Gamma_c'
                                'neff_r', 'neff_wg', 'ng', 'Disp',
                                'FSR', 'D2', 'Dint' , 'μ'], 
                     dtype='float')


    for h in H:
        for rw in RW:
            dum = pd.read_csv(funfname(h, rw),
                              skiprows=5,
                              names = ['M', 'freq', 'neff_r', 'neff_wg', 'gamma',
                                       'epsCore', 'epsClad', 'epsSub', 'Aeff', 'P11', 'P12', 'P21', 'P22', 'Gamma_c'], sep = '\s+', 
                             dtype='float')

            dum = dum.astype('float')
            dum['RW'] = rw
            dum['H'] = h
            dum['ng'] = np.nan
            dum['Disp'] = np.nan
            dum['FSR'] = np.nan
            dum['Dint'] = np.nan
            dum['μ'] = np.nan
            df = pd.concat([df, dum])
    if doDisp:
        df = df.groupby(['H', 'RW']).apply(lambda x: getDisp(x, RR))
        if doDint:
            df = df.groupby(['H', 'RW']).apply(lambda x: getDint(x, fpmp = fpmp))

    return df.set_index(['H', 'RW','M'])
