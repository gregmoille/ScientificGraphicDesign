# Plotting Data

## Some simple tips 

- **Clarity, simplicity, consistency**. If there is only one rule you need to remember, it's this one. Your goal is to balance 
    - _Clarity_ of the message: your plot (or subplots) convey **one and only one point** and need to be understood from a first look
    - _Simplicity_
    - _Consistency_
- **Stick to a style** and keep it for the whole paper. 
- **Don't reinvent the wheel.** Usually, big journal hired real graphic designer so their style are never off. It can be be a great starting point. Similar for color palette, professional already took care of it. 
- **Create a habit** Always try to plot your figure like you will publish them. It will create a metnal gymnastic, leading to muscle memory, making clear and simple figure much easier with time
- **Make it automatic**. Minimize your work load by creating function/module/etc which pre-load your style and make consistency automatic. Same for exporting the figure, you don't want to spend to mch time tweaking stuff in the vector software because you didn't plot thing correctly


## Colorpalettes and colormaps 

A detail discussion on what kind of color palettes and colormap should be use for efficient visualization. Most of these paletes are available through python packages: 
- [Scientific Colormap](https://www.fabiocrameri.ch/colourmaps/) 
by Fabio Crameri can be installed through the [cmcrameri pypi packaged](https://pypi.org/project/cmcrameri/0.11/). I highly recommand using `batlow`, `oslo` (or its reverse version `oslo_r`) and `lipari` for 2D map plot. Also don't forget to acknowledge his work if you use this colors ([more info](https://www.fabiocrameri.ch/ws/media-library/ce2eb6eee7c345f999e61c02e2733962/readme_scientificcolourmaps.pdf#Acknowledgement))
- [IBM color palettes](https://www.ibm.com/design/language/color) (along with some other good palettes) can be installed through the [SecretColors module](https://github.com/secretBiology/SecretColors)


## Python Plotting—`pyprettyplot`    

## Ploting is only 75% of the job 

Plotting the data will probably get you up to 3/4 of the way of a complete figure. You will still have to edit it in Adobe Illustrator/Inkscape (or whatever your software of choice). Hence keep in mind you want to plot and make your life easier for editting, meaning: 

- Make your plot the right size 
- Make all your font the right size 
- Avoid the need for unecessary edit


