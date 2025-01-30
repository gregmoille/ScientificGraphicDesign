import sys
import os
import re
import ipdb

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
import warnings

warnings.filterwarnings("ignore")

zclr = "#B1BDDA"


def addPlotlyLine(fig, x, y=[0, 0], clr=zclr, lw=2, row=None, col=None, dash=None):
    if row == None and col == None:
        fig.add_shape(
            type="line",
            x0=x[0],
            x1=x[1],
            y0=y[0],
            y1=y[1],
            line=dict(color=clr, width=lw, dash=dash),
        )
    else:
        fig.add_shape(
            type="line",
            x0=x[0],
            x1=x[1],
            y0=y[0],
            y1=y[1],
            line=dict(color=clr, width=lw, dash=dash),
            row=row,
            col=col,
        )


def loadOSA(fname, noise=-85):
    df = pd.read_csv(fname)
    df["freq"] = cts.c / df.lbd
    df.S[df.S < noise] = noise
    to_keep = ["freq", "lbd", "S"]
    columns = df.columns.values
    to_drop = [cc for cc in columns if not cc in to_keep]
    df.drop(to_drop, axis=1, inplace=True)
    df.sort_values("freq", inplace=True)
    df.reset_index(inplace=True, drop=True)
    return df


from .colors import *
from .dispersion import *
from .gregplot import *
from .lineardata import *

from .plotlyServer import plotlyServer


pio.templates.default = "nord"
