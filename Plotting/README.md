# Plotting Data

## Some simple tips 

- **Clarity, simplicity, consistency**. If there is only one rule you need to remember, it's this one. Your goal is to balance 
    - _Clarity_ of the message: your plot (or subplots) conveys **one and only one point** and needs to be understood at first glance.
    \- _Simplicity_: avoid unnecessary plot elements. _Does your plot need a surrounding box, fine tick spacing, or a grid?_ Remove **all superficial** elements.
    - _Consistency_ throughout your plots. Tastes and colors vary, and some people won't like your style for a given paper, but so be it. However, not having consistent size (axis spine, fonts, etc.), color coding, and so on makes your whole work sloppy and will give the impression of an unpolished work. In contrast, a consistent style will make your work look professional and show that you actually cared for your work.
- **Stick to a style** and try to find works well for you
- **Don't reinvent the wheel.** Usually, big journal hired real graphic designer so their style are never off. It can be be a great starting point. Similar for color palette, professional already took care of it. 
- **Create a habit** Always try to plot your figures as if you will publish them. It will create a mental gymnastic, leading to muscle memory, making clear and simple figures much easier over time.
- **Make it automatic**. Minimize your workload by creating a function/module/etc. that pre-loads your style and makes consistency automatic, for instance using the [pyprettyplot package here](./pyprettyplot). The same goes for exporting the figure; you don't want to spend too much time tweaking things in the vector software because you didn't plot things correctly.


## Colorpalettes and colormaps 

A detail discussion on what kind of color palettes and colormap should be use for efficient visualization. Most of these paletes are available through python packages: 
- [Scientific Colormap](https://www.fabiocrameri.ch/colourmaps/) 
by Fabio Crameri can be installed through the [cmcrameri pypi packaged](https://pypi.org/project/cmcrameri/0.11/). I highly recommand using `batlow`, `oslo` (or its reverse version `oslo_r`) and `lipari` for 2D map plot. Also don't forget to acknowledge his work if you use this colors ([more info](https://www.fabiocrameri.ch/ws/media-library/ce2eb6eee7c345f999e61c02e2733962/readme_scientificcolourmaps.pdf#Acknowledgement))
- [IBM color palettes](https://www.ibm.com/design/language/color) (along with some other good palettes) can be installed through the [SecretColors module](https://github.com/secretBiology/SecretColors)


## Python Plotting—[`pyprettyplot`](./pyprettyplot/)    

As mentioned, you should make plotting your figure automatic. On my end, I use the [`plotly`](https://plotly.com/python/) package for plotting, as it enables interactive plotting and easy HTML export (while keeping the interaction), which I can then embed in Notion.

To maintain a consistent style across my figures, either during experiments or when I prepare paper figures, I created a simple package for my notebooks, [`pyprettyplot`](./pyprettyplot/).

### How to install it? 

Two ways:  
-  Just download the pyprettyplot folder and put it in the current directory you are working in. Install any required packages (pandas/scipy/numpy/matplotlib/plotly/cmcrameri/SecretColors/nbformat/kaleido) by running `pip install -r requirements.txt`. This way, you will still be able to tweak it.  
-  If you use it often, it's better to install it system-wide by using the command `python ./setup.py install` in this downloaded folder.

### How to use it? 

Not very complicated: 

```
from pyprettyplot import *
```

And voilà, you are all set. By default, the style will be:  
1. Axis with a linewidth of 0.5 pt with color #2E3440  
2. Tick with a linewidth of 0.5 pt with color #2E3440, and a length of 2 pt  
3. No top and right spines  
4. Tick labels using Decima (fallback to default if not installed) 7 pt  
5. Axis title labels using Aktiv Grotesk Condensed Regular (fallback to default if not installed) 8 pt  
6. Cycling color palette using the [Nord theme](https://www.nordtheme.com/docs/colors-and-palettes) #356BA0, #D18F98, #499E4B, #7181A3, #844A84, #7181A3, #BC394C'


### Example of use

You can find a detailed example in this [notebook](./Notebook.ipynb) demonstrating the creation of a subpanel from figure 2 in this [paper](https://pubs.aip.org/app/article/10/1/016104/3330155/All-optical-azimuthal-trapping-of-dissipative-Kerr)


## Ploting is only 75% of the job 

Plotting the data will probably get you up to 3/4 of the way to a complete figure. You will still have to edit it in Adobe Illustrator, Inkscape, or whatever your software of choice is. Hence, keep in mind that you want to plot and make your life easier for editing, meaning:

- Make your plot the right size 
- Make all your font the right size 
- Avoid the need for unecessary edit

If you did that correctly, then the work that will be done in Adobe Illustrator/Inkscape/etc. will be much easier. Some tips for Adobe Illustrator are provided here.

