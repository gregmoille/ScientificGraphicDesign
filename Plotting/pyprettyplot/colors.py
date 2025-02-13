import pickle as pkl
import pandas as pd
import numpy as np
from scipy import signal
from scipy import constants as cts
from glob import glob
from copy import copy
import matplotlib as mpl
import plotly.graph_objs as go
import plotly.io as pio
from cmcrameri import cm as cmap
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# pio.templates.default = "plotly_white"
from matplotlib.colors import LinearSegmentedColormap, to_hex
from itertools import cycle
from IPython.core.display import display, HTML

from itertools import cycle
from SecretColors import Palette

p = Palette()  # Generates Default color palette i.e. IBM Color Palette
ibm = Palette("ibm")

ibm_light_palette12_raw = [
    ibm.purple,
    ibm.cyan,
    ibm.teal,
    ibm.magenta,
    ibm.red,
    ibm.red,
    ibm.green,
    ibm.blue,
    ibm.magenta,
    ibm.yellow,
    ibm.teal,
    ibm.cyan,
    ibm.orange,
    ibm.purple,
]

ibm_light_palette12 = [
    ibm.purple(shade=70),
    ibm.cyan(shade=50),
    ibm.teal(shade=70),
    ibm.magenta(shade=70),
    ibm.red(shade=50),
    ibm.red(shade=90),
    ibm.green(shade=60),
    ibm.blue(shade=80),
    ibm.magenta(shade=50),
    ibm.yellow(shade=50),
    ibm.teal(shade=50),
    ibm.cyan(shade=90),
    ibm.orange(shade=70),
    ibm.purple(shade=50),
]
ibm_light_palette2 = [ibm.purple(shade=70), ibm.teal(shade=50)]
ibm_light_palette3 = [ibm.purple(shade=50), ibm.teal(shade=70), ibm.magenta(shade=70)]
ibm_light_palette4 = [
    ibm.teal(shade=50),
    ibm.blue(shade=80),
    ibm.purple(shade=50),
    ibm.purple(shade=70),
]
ibm_light_palette5 = [
    ibm.blue(shade=80),
    ibm.teal(shade=50),
    ibm.magenta(shade=70),
    ibm.red(shade=90),
    ibm.purple(shade=50),
]

pancoty = ["5A5B9F", "D94F70", "009473", "F0C05A", "7BC4C4", "FF6F61"]
# ==== TEMPLATES ====
tmplt = pio.templates["plotly_white"].layout
tmplt.update(
    xaxis={"showspikes": True, "spikethickness": 0.5},
    yaxis={"showspikes": True, "spikethickness": 0.5},
    hovermode="closest",
)
pio.templates["google"] = go.layout.Template(
    layout_colorway=[
        "#4285F4",
        "#DB4437",
        "#F4B400",
        "#0F9D58",
        "#185ABC",
        "#B31412",
        "#EA8600",
        "#137333",
        "#d2e3fc",
        "#ceead6",
    ],
    layout=tmplt,
)

pio.templates["ibm_light"] = go.layout.Template(
    layout_colorway=ibm_light_palette12, layout=tmplt
)

pio.templates["default"] = go.layout.Template(
    layout_colorway=[
        "#1f77b4",
        "#ff7f0e",
        "#2ca02c",
        "#d62728",
        "#9467bd",
        "#8c564b",
        "#e377c2",
        "#7f7f7f",
        "#bcbd22",
        "#17becf",
    ],
    layout=tmplt,
)

pio.templates["nature"] = go.layout.Template(
    layout_colorway=[
        "#E64B35",
        "#4DBBD5",
        "#00A087",
        "#3C5488",
        "#F39B7F",
        "#8491B4",
        "#91D1C2",
        "#DC0000",
        "#7E6148",
        "#B09C85",
    ],
    layout=tmplt,
)

pio.templates["science"] = go.layout.Template(
    layout_colorway=[
        "#3B4992",
        "#EE0000",
        "#008B45",
        "#631879",
        "#008280",
        "#BB0021",
        "#5F559B",
        "#A20056",
        "#808180",
        "#1B1919",
    ],
    layout=tmplt,
)

#    layout = tmplt)
clrs_nords = ["#67789c", "#BF616A", "#407578", "#8FBCBB", "#993a88", "#89a86d"]
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

tmplt = pio.templates["plotly_white"].layout
tmplt.title.update(x=0.05, font = dict(family="Aktiv Grotesk Cd, Open Sans, verdana, arial, sans-serif", size=18))
tmplt.font.update(family="Aktiv Grotesk Cd ,Open Sans, verdana, arial, sans-serif", color=nord["PolarNight"][0])
tmplt.xaxis.tickfont.update(family="Decima, Open Sans, verdana, arial, sans-serif")
tmplt.yaxis.tickfont.update(family="Decima, Open Sans, verdana, arial, sans-serif")
tmplt.yaxis.title.font.update(family="Aktiv Grotesk Cd, Open Sans, verdana, arial, sans-serif", size=16)
tmplt.xaxis.title.font.update(family="Aktiv Grotesk Cd, Open Sans, verdana, arial, sans-serif", size=16)

tmplt.yaxis.update(zeroline=False)

tmplt.xaxis.update(
    showline=True,
    title_standoff = 0,
    linecolor=nord["PolarNight"][0],
    linewidth=0.5 / 0.5,
    ticks="outside",
    zeroline=False,
    tickcolor=nord["PolarNight"][0],
    tickwidth=0.5 / 0.5,
    ticklen=2 / 0.5,
)

tmplt.yaxis.update(showline=True,
    linecolor=nord["PolarNight"][0],
    linewidth=0.5 / 0.5,
    ticks="outside",
    zeroline=False,
    tickcolor=nord["PolarNight"][0],
    tickwidth=0.5 / 0.5,
    ticklen=2 / 0.5,
    title_standoff = 0,
    showgrid = False,)

tmplt.xaxis.update(showline=True,showgrid = False)
tmplt.update(margin_pad=0)
clrs_nords = ["#356BA0", "#D18F98", "#499E4B", "#7181A3", "#844A84", "#7181A3", "#BC394C"]
pio.templates["nord"] = go.layout.Template(layout_colorway=clrs_nords, layout=tmplt)
pio.templates["nord"].data.scatter = [go.Scatter(line_width = 1.5)]
pio.templates["nord"].layout.legend.update(borderwidth = 0, font_size = 12,tracegroupgap = 2)

def plotly_color(cycling=True, scheme="nature"):
    if scheme == "default":
        plotly_colors = [
            "#1f77b4",
            "#ff7f0e",
            "#2ca02c",
            "#d62728",
            "#9467bd",
            "#8c564b",
            "#e377c2",
            "#7f7f7f",
            "#bcbd22",
            "#17becf",
        ]
        if cycling:
            return cycle(plotly_colors)
        else:
            return plotly_colors
    if scheme == "nature":
        plotly_colors = [
            "#E64B35",
            "#4DBBD5",
            "#00A087",
            "#3C5488",
            "#F39B7F",
            "#8491B4",
            "#91D1C2",
            "#DC0000",
            "#7E6148",
            "#B09C85",
        ]
        if cycling:
            return cycle(plotly_colors)
        else:
            return plotly_colors
    if scheme == "science":
        plotly_colors = [
            "#3B4992",
            "#EE0000",
            "#008B45",
            "#631879",
            "#008280",
            "#BB0021",
            "#5F559B",
            "#A20056",
            "#808180",
            "#1B1919",
        ]
        if cycling:
            return cycle(plotly_colors)
        else:
            return plotly_colors


def colorFader(
    c1, c2, mix=0
):  # fade (linear interpolate) from color c1 (at mix=0) to c2 (mix=1)
    c1 = np.array(mpl.colors.to_rgb(c1))
    c2 = np.array(mpl.colors.to_rgb(c2))
    return mpl.colors.to_hex((1 - mix) * c1 + mix * c2)


def mpl_to_plotly(cmap, pl_entries=11, rdigits=15):
    scale = np.linspace(0, 1, pl_entries)
    colors = (cmap(scale)[:, :3] * 255).astype(np.uint8)
    pl_colorscale = [
        [round(s, rdigits), f"rgb{tuple(color)}"] for s, color in zip(scale, colors)
    ]
    return pl_colorscale

def lighten_color(color, amount=0.5):
    """
    Lightens the given color by multiplying (1-luminosity) by the given amount.
    Input can be matplotlib color string, hex string, or RGB tuple.

    Examples:
    >> lighten_color('g', 0.3)
    >> lighten_color('#F034A3', 0.6)
    >> lighten_color((.3,.55,.1), 0.5)
    """
    import matplotlib.colors as mc
    import colorsys

    try:
        c = mc.cnames[color]
    except:
        c = color
    c = colorsys.rgb_to_hls(*mc.to_rgb(c))
    return mc.rgb2hex(colorsys.hls_to_rgb(c[0], 1 - amount * (1 - c[1]), c[2]))

"""
This file contains the scientific colormaps (see http://www.fabiocrameri.ch/visualisation.php, and https://zenodo.org/record/1243863#.Ww6bgEiFNPY)
converted to Plotly colorscales """

"""Sequential scientific colorscales"""

acton=[[0.0, 'rgb(46, 33,77)'],
       [0.1, 'rgb(72, 56, 100)'],
       [0.2, 'rgb(102, 80, 123)'],
       [0.3, 'rgb(135, 96, 141)'],
       [0.4, 'rgb(166, 102, 148)'],
       [0.5, 'rgb(196, 110, 155)'],
       [0.6, 'rgb(212, 134, 173)'],
       [0.7, 'rgb(212, 156, 189)'],
       [0.8, 'rgb(213, 178, 205)'],
       [0.9, 'rgb(220, 204, 222)'],
       [1.0, 'rgb(230, 230, 240)']]

bilbao= [[0.0,'rgb(255, 255, 255)'],
         [0.1, 'rgb(220, 220, 220)'],
         [0.2, 'rgb(198, 195, 183)'],
         [0.3, 'rgb(188, 180, 149)'],
         [0.4, 'rgb(178, 163, 116)'],
         [0.5, 'rgb(171, 139, 103)'],
         [0.6, 'rgb(164, 115, 93)'],
         [0.7, 'rgb(157, 90, 82)'],
         [0.8, 'rgb(139, 63, 63)'],
         [0.9, 'rgb(108, 31, 31)'],
         [1.0, 'rgb(77, 0, 1)']]

davos= [[0.0, 'rgb(44, 26, 76)'],
        [0.1, 'rgb(40, 59, 110)'],
        [0.2, 'rgb(42, 94, 151)'],
        [0.3, 'rgb(68, 117, 193)'],
        [0.4, 'rgb(96, 137, 190)'],
        [0.5, 'rgb(125, 156, 181)'],
        [0.6, 'rgb(155, 175, 172)'],
        [0.7, 'rgb(186, 196, 163)'],
        [0.8, 'rgb(215, 217, 161)'],
        [0.9, 'rgb(237, 236, 206)'],
        [1.0, 'rgb(255, 255, 255)']]

devon= [[0.0, 'rgb(43, 26, 76)'],
        [0.1, 'rgb(41, 50, 101)'],
        [0.2, 'rgb(38, 76, 127)'],
        [0.3, 'rgb(46, 98, 159)'],
        [0.4, 'rgb(68, 117, 195)'],
        [0.5, 'rgb(121, 140, 219)'],
        [0.6, 'rgb(166, 162, 236)'],
        [0.7, 'rgb(190, 184, 242)'],
        [0.8, 'rgb(211, 207, 246)'],
        [0.9, 'rgb(233, 231, 250)'],
        [1.0, 'rgb(255, 255, 255)']]

grayC= [[0.0, 'rgb(255, 255, 255)'],
        [0.1, 'rgb(227, 227, 227)'],
        [0.2, 'rgb(198, 198, 198)'],
        [0.3, 'rgb(172, 172, 172)'],
        [0.4, 'rgb(145, 145, 145)'],
        [0.5, 'rgb(118, 118, 118)'],
        [0.6, 'rgb(94, 94, 94)'],
        [0.7, 'rgb(70, 70, 70)'],
        [0.8, 'rgb(48, 48, 48)'],
        [0.9, 'rgb(27, 27, 27)'],
        [1.0, 'rgb(0, 0, 0)']]

lajolla= [[0.0, 'rgb(255, 255, 204)'],
          [0.1, 'rgb(251, 238, 156)'],
          [0.2, 'rgb(246, 216, 105)'],
          [0.3, 'rgb(238, 182, 85)'],
          [0.4, 'rgb(232, 150, 82)'],
          [0.5, 'rgb(225, 116, 79)'],
          [0.6, 'rgb(206, 83, 76)'],
          [0.7, 'rgb(160, 69, 67)'],
          [0.8, 'rgb(112, 55, 46)'],
          [0.9, 'rgb(64, 39, 22)'],
          [1.0, 'rgb(26, 26, 0)']]

lapaz= [[0.0, 'rgb(26, 12, 101)'],
        [0.1, 'rgb(33, 46, 124)'],
        [0.2, 'rgb(39, 77, 145)'],
        [0.3, 'rgb(49, 105, 159)'],
        [0.4, 'rgb(68, 131, 167)'],
        [0.5, 'rgb(102, 153, 164)'],
        [0.6, 'rgb(141, 163, 152)'],
        [0.7, 'rgb(179, 167, 139)'],
        [0.8, 'rgb(223, 183, 148)'],
        [0.9, 'rgb(253, 217, 197)'],
        [1.0, 'rgb(255, 243, 243)']]

oslo= [[0.0, 'rgb(0, 1, 0)'],
       [0.1, 'rgb(11, 25, 39)'],
       [0.2, 'rgb(17, 48, 77)'],
       [0.3, 'rgb(27, 73, 117)'],
       [0.4, 'rgb(46, 98, 160)'],
       [0.5, 'rgb(78, 125, 199)'],
       [0.6, 'rgb(111, 146, 202)'],
       [0.7, 'rgb(144, 166, 201)'],
       [0.8, 'rgb(176, 185, 200)'],
       [0.9, 'rgb(215, 215, 216)'],
       [1.0, 'rgb(255, 255, 255)']]

tokyo= [[0.0, 'rgb(26, 14, 51)'],
        [0.1, 'rgb(67, 27, 74)'],
        [0.2, 'rgb(110, 54, 101)'],
        [0.3, 'rgb(132, 86, 119)'],
        [0.4, 'rgb(140, 114, 128)'],
        [0.5, 'rgb(144, 140, 135)'],
        [0.6, 'rgb(148, 165, 142)'],
        [0.7, 'rgb(154, 193, 149)'],
        [0.8, 'rgb(175, 225, 163)'],
        [0.9, 'rgb(222, 251, 194)'],
        [1.0, 'rgb(255, 255, 217)']]

turku= [[0.0, 'rgb(0, 0, 0)'],
        [0.1, 'rgb(33, 33, 31)'],
        [0.2, 'rgb(61, 60, 53)'],
        [0.3, 'rgb(90, 86, 70)'],
        [0.4, 'rgb(120, 113, 86)'],
        [0.5, 'rgb(156, 141, 103)'],
        [0.6, 'rgb(193, 158, 122)'],
        [0.7, 'rgb(222, 161, 139)'],
        [0.8, 'rgb(247, 175, 169)'],
        [0.9, 'rgb(255, 203, 203)'],
        [1.0, 'rgb(255, 230, 230)']]

"""Diverging scientific colorscales"""

berlin=[[0.0, 'rgb(158, 176, 255)'],
        [0.05, 'rgb(130, 173, 242)'],
        [0.1, 'rgb(98, 166, 224)'],
        [0.15, 'rgb(68, 151, 198)'],
        [0.2, 'rgb(50, 128, 166)'],
        [0.25, 'rgb(40, 104, 134)'],
        [0.3, 'rgb(32, 82, 106)'],
        [0.35, 'rgb(23, 60, 77)'],
        [0.4, 'rgb(17, 39, 50)'],
        [0.45, 'rgb(17, 22, 27)'],
        [0.5, 'rgb(25, 12, 9)'],
        [0.55, 'rgb(38, 13, 1)'],
        [0.6, 'rgb(55, 16, 0)'],
        [0.65, 'rgb(74, 21, 2)'],
        [0.7, 'rgb(97, 32, 11)'],
        [0.75, 'rgb(125, 52, 30)'],
        [0.8, 'rgb(150, 74, 54)'],
        [0.85, 'rgb(176, 98, 83)'],
        [0.9, 'rgb(202, 123, 113)'],
        [0.95, 'rgb(229, 149, 144)'],
        [1.0, 'rgb(255, 173, 173)']]

broc=[[0.0, 'rgb(44, 26, 76)'],
      [0.05, 'rgb(43, 44, 95)'],
      [0.1, 'rgb(41, 64, 115)'],
      [0.15, 'rgb(45, 86, 136)'],
      [0.2, 'rgb(65, 109, 154)'],
      [0.25, 'rgb(94, 132, 170)'],
      [0.3, 'rgb(122, 154, 185)'],
      [0.35, 'rgb(153, 178, 202)'],
      [0.4, 'rgb(185, 202, 218)'],
      [0.45, 'rgb(217, 226, 234)'],
      [0.5, 'rgb(239, 241, 237)'],
      [0.55, 'rgb(237, 238, 217)'],
      [0.6, 'rgb(225, 224, 187)'],
      [0.65, 'rgb(208, 208, 155)'],
      [0.7, 'rgb(184, 184, 125)'],
      [0.75, 'rgb(157, 157, 100)'],
      [0.8, 'rgb(132, 132, 79)'],
      [0.85, 'rgb(106, 106, 57)'],
      [0.9, 'rgb(81, 81, 37)'],
      [0.95, 'rgb(58, 58, 18)'],
      [1.0, 'rgb(38, 39, 1)']]

cork=[[0.0, 'rgb(44, 26, 76)'],
      [0.05, 'rgb(43, 44, 94)'],
      [0.1, 'rgb(41, 64, 115)'],
      [0.15, 'rgb(44, 86, 135)'],
      [0.2, 'rgb(64, 108, 153)'],
      [0.25, 'rgb(92, 131, 169)'],
      [0.3, 'rgb(120, 152, 184)'],
      [0.35, 'rgb(150, 176, 200)'],
      [0.4, 'rgb(182, 199, 217)'],
      [0.45, 'rgb(213, 223, 233)'],
      [0.5, 'rgb(231, 239, 237)'],
      [0.55, 'rgb(216, 232, 218)'],
      [0.6, 'rgb(188, 216, 191)'],
      [0.65, 'rgb(160, 200, 164)'],
      [0.7, 'rgb(133, 183, 137)'],
      [0.75, 'rgb(106, 167, 111)'],
      [0.8, 'rgb(82, 151, 85)'],
      [0.85, 'rgb(65, 130, 58)'],
      [0.9, 'rgb(64, 110, 36)'],
      [0.95, 'rgb(65, 92, 18)'],
      [1.0, 'rgb(67, 77, 2)']]

lisbon=[[0.0, 'rgb(230, 229, 255)'],
        [0.05, 'rgb(197, 206, 236)'],
        [0.1, 'rgb(163, 181, 215)'],
        [0.15, 'rgb(129, 156, 195)'],
        [0.2, 'rgb(96, 131, 174)'],
        [0.25, 'rgb(65, 106, 151)'],
        [0.3, 'rgb(42, 83, 125)'],
        [0.35, 'rgb(26, 61, 95)'],
        [0.4, 'rgb(19, 42, 66)'],
        [0.45, 'rgb(17, 28, 40)'],
        [0.5, 'rgb(23, 25, 25)'],
        [0.55, 'rgb(36, 35, 25)'],
        [0.6, 'rgb(56, 53, 34)'],
        [0.65, 'rgb(79, 75, 47)'],
        [0.7, 'rgb(104, 97, 62)'],
        [0.75, 'rgb(129, 122, 78)'],
        [0.8, 'rgb(154, 145, 96)'],
        [0.85, 'rgb(181, 173, 121)'],
        [0.9, 'rgb(207, 201, 152)'],
        [0.95, 'rgb(232, 229, 185)'],
        [1.0, 'rgb(255, 255, 217)']]

roma=[[0.0, 'rgb(126, 26, 1)'],
      [0.05, 'rgb(141, 57, 11)'],
      [0.1, 'rgb(155, 85, 23)'],
      [0.15, 'rgb(168, 111, 34)'],
      [0.2, 'rgb(181, 138, 45)'],
      [0.25, 'rgb(194, 166, 59)'],
      [0.3, 'rgb(208, 193, 81)'],
      [0.35, 'rgb(222, 217, 117)'],
      [0.4, 'rgb(230, 230, 152)'],
      [0.45, 'rgb(227, 236, 180)'],
      [0.5, 'rgb(209, 237, 202)'],
      [0.55, 'rgb(180, 234, 213)'],
      [0.6, 'rgb(141, 222, 218)'],
      [0.65, 'rgb(105, 202, 215)'],
      [0.7, 'rgb(84, 178, 207)'],
      [0.75, 'rgb(72, 154, 197)'],
      [0.8, 'rgb(63, 133, 188)'],
      [0.85, 'rgb(54, 111, 179)'],
      [0.9, 'rgb(45, 90, 170)'],
      [0.95, 'rgb(36, 70, 161)'],
      [1.0, 'rgb(27, 51, 153)']]

tofino=[[0.0, 'rgb(222, 217, 255)'],
        [0.05, 'rgb(190, 194, 241)'],
        [0.1, 'rgb(155, 170, 226)'],
        [0.15, 'rgb(121, 145, 209)'],
        [0.2, 'rgb(87, 119, 186)'],
        [0.25, 'rgb(62, 94, 154)'],
        [0.3, 'rgb(48, 74, 123)'],
        [0.35, 'rgb(35, 55, 91)'],
        [0.4, 'rgb(25, 37, 61)'],
        [0.45, 'rgb(17, 24, 35)'],
        [0.5, 'rgb(13, 22, 19)'],
        [0.55, 'rgb(17, 32, 19)'],
        [0.6, 'rgb(24, 50, 26)'],
        [0.65, 'rgb(33, 71, 37)'],
        [0.7, 'rgb(44, 93, 48)'],
        [0.75, 'rgb(56, 117, 61)'],
        [0.8, 'rgb(74, 141, 75)'],
        [0.85, 'rgb(106, 168, 95)'],
        [0.9, 'rgb(145, 190, 116)'],
        [0.95, 'rgb(183, 211, 137)'],
        [1.0, 'rgb(219, 230, 155)']]

vik=[[0.0, 'rgb(1, 18, 97)'],
     [0.05, 'rgb(2, 37, 109)'],
     [0.1, 'rgb(2, 57, 122)'],
     [0.15, 'rgb(3, 78, 135)'],
     [0.2, 'rgb(16, 100, 150)'],
     [0.25, 'rgb(47, 125, 166)'],
     [0.3, 'rgb(83, 149, 183)'],
     [0.35, 'rgb(125, 176, 201)'],
     [0.4, 'rgb(166, 201, 218)'],
     [0.45, 'rgb(207, 225, 234)'],
     [0.5, 'rgb(235, 237, 233)'],
     [0.55, 'rgb(234, 225, 206)'],
     [0.6, 'rgb(220, 203, 168)'],
     [0.65, 'rgb(205, 181, 131)'],
     [0.7, 'rgb(190, 159, 95)'],
     [0.75, 'rgb(174, 136, 60)'],
     [0.8, 'rgb(159, 113, 28)'],
     [0.85, 'rgb(141, 87, 4)'],
     [0.9, 'rgb(126, 63, 1)'],
     [0.95, 'rgb(111, 41, 1)'],
     [1.0, 'rgb(97, 18, 0)']]

""" Special colorscale, oleron, that is a concatenation of two
sequential colorscales """

oleron=[[0.0, 'rgb(26, 38, 89)'],
        [0.05, 'rgb(44, 56, 107)'],
        [0.1, 'rgb(65, 77, 128)'],
        [0.15, 'rgb(86, 99, 150)'],
        [0.2, 'rgb(108, 121, 172)'],
        [0.25, 'rgb(131, 144, 195)'],
        [0.3, 'rgb(153, 166, 217)'],
        [0.35, 'rgb(177, 189, 237)'],
        [0.4, 'rgb(196, 209, 246)'],
        [0.45, 'rgb(214, 226, 251)'],
        [0.5, 'rgb(26, 76, 0)'],
        [0.55, 'rgb(56, 85, 0)'],
        [0.6, 'rgb(83, 94, 2)'],
        [0.65, 'rgb(113, 108, 22)'],
        [0.7, 'rgb(142, 125, 51)'],
        [0.75, 'rgb(170, 144, 80)'],
        [0.8, 'rgb(197, 164, 108)'],
        [0.85, 'rgb(226, 188, 139)'],
        [0.9, 'rgb(243, 212, 171)'],
        [0.95, 'rgb(249, 233, 201)'],
        [1.0, 'rgb(253, 253, 230)']]