import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mp
import matplotlib.gridspec as gridspec
import re
import os
from itertools import cycle
import warnings
from importlib import reload
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
from matplotlib import font_manager
warnings.simplefilter("ignore")
from SecretColors import Palette
from glob import glob
from scipy import constants as cts
# from mpl_toolkits.axes_grid1.inset_locator import (
#     Bbox,
#     TransformedBbox,
#     BboxPatch,
#     BboxConnector,
#     inset_axes, 
#     InsetPosition, 
#     mark_inset
# )
import numpy as np
from SecretColors import ColorMap
from matplotlib.ticker import FormatStrFormatter


""
p = Palette()  # Generates Default color palette i.e. IBM Color Palette
ibm = Palette("ibm")
nord = dict(
    PolarNight=["#2E3440", "#3B4252", "#434C5E", "#4C566A"],
    SnowStorm=["#D8DEE9", "#E5E9F0", "#ECEFF4"],
    Frost=["#8FBCBB", "#88C0D0", "#81A1C1", "#5E81AC"],
    Aurora=dict(
        red="#BF616A",
        orange="#D08770",
        yellow="#EBCB8B",
        green="#A3BE8C",
        purple="#B48EAD",
    ),
)

def createColor(clr1, clr2, N):
    cmap = LinearSegmentedColormap.from_list("", [clr1, clr2])
    return [cmap(ii/N) for ii in np.arange(N)]

file_path = os.path.dirname(__file__)
file = f"{file_path}/matplotlibrc"
mp.rcParams.update(mp.rc_params_from_file(file))

def adjust_spines(ax, spines):
    for loc, spine in ax.spines.items():
        spine.set_position(("outward", 5))  # outward by 5 points


def adjustFont(f = None, ax = None): 
    ticks_font = font_manager.FontProperties(family='monospace', size = 8)
    if f: 
        for aa in f.get_axes():
            aa.xaxis.set_major_formatter(FormatStrFormatter('%.4g'))
            aa.yaxis.set_major_formatter(FormatStrFormatter('%.4g'))
            for tick in aa.get_xticklabels():
                tick.set_fontproperties(ticks_font)
            for tick in aa.get_yticklabels():
                tick.set_fontproperties(ticks_font)
    if ax: 
        ax.xaxis.set_major_formatter(FormatStrFormatter('%.4g'))
        ax.yaxis.set_major_formatter(FormatStrFormatter('%.4g'))
        for tick in ax.get_xticklabels():
            tick.set_fontproperties(ticks_font)
        for tick in ax.get_yticklabels():
        
            tick.set_fontproperties(ticks_font)
            


cm = 1 / 2.54
pt = 0.013887591104466456  # inch
col = 246 * pt
col2 = 510 * pt

clrnord = cycle(["#3b4252","#60758f", "#4e4c6b", "#5c818a", "#324f32","#637087",])


def mark_inset_custom(
    parent_axes, inset_axes, loc1a=1, loc1b=1, loc2a=2, loc2b=2, **kwargs
):
    rect = TransformedBbox(inset_axes.viewLim, parent_axes.transData)

    pp = BboxPatch(rect, fill=False, **kwargs)
    parent_axes.add_patch(pp)
    p1 = BboxConnector(inset_axes.bbox, rect, loc1=loc1a, loc2=loc1b, **kwargs)

    inset_axes.add_patch(p1)
    p1.set_clip_on(False)
    p2 = BboxConnector(inset_axes.bbox, rect, loc1=loc2a, loc2=loc2b, **kwargs)
    inset_axes.add_patch(p2)
    p2.set_clip_on(False)

    return pp, p1, p2


def PlotCrossGuides(f):
    for xx in np.arange(0, 1.1, 0.25):
        # for yy in np.arange(0, 1.1, 0.25):
        for yy in [0, 1]:
            f.text(
                xx, yy, "+", va="center", ha="center", c="#4a4a4a", fontweight="regular"
            )
    for yy in np.arange(0, 1.1, 0.25):
        # for yy in np.arange(0, 1.1, 0.25):
        for xx in [0, 1]:
            f.text(
                xx, yy, "+", va="center", ha="center", c="#4a4a4a", fontweight="regular"
            )
