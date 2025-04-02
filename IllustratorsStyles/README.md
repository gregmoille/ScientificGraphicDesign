# 🏗️ Under Constructions🏗️

# Document Settings

- **Always work in RGB color mode**. Since most of the of your figures in a manuscript will be displayed on a screen, it is better to work in RGB color mode. If you need to have high quality printout, then you can convert the figure to CMYK later.  To set it up, go to File > Document Color Mode > RGB Color.
- Set the artboard size to the size of the figure you want to create: 
    - a single columns wigure would be 256 pts
    - a double columns figure would be 512 pts
- Set the grid step to 2pt:
    - Go to Edit > Preferences > Guides & Grid
    - Set the gridline every to 2pt and subdivisions to 1
- **DO NOT WORK OUTSIDE OF THE GRID** (or at least as much as possible).The grid is your friend. It will help you to align your elements and make your figure look more professional.
    - What should be on grid: 
        - Keep the schematic on grid
        - Keep the axis of your figure on the grid. 
        - Keep the text on the grid 
    - Of course some things can't be on grid; 
        - tick marks and label 
        - curves anchor points        

# Colors Palettes

- [IBM colorpalette](https://github.com/IBM-Design/colors/blob/master/ibm-colors.ase): comes from the IBM design language which to be honest is a must to scroll through to understand how to make unified good design. It is also consisten with the [prettyplot class](../Plotting/pyprettyplot/), which include the `ibm` class to retrieve the colors (for instance `ibm.cerulean(shade = 60)`). 


# Handling bitmap figures (png, jpg, etc.)  

Of course, most of the your figure will be in vector format. But sometime you will find yourself needed to put some bitmap in your system (e.g. a photo of your sample). To do so, you can use the following steps:
- Do not mask the bitmap figure. Insteaf crop it as it will reduce its size. 
- Do not link the bitmap figure. Instead, embed it in the document. To do so, go to Properties > Quick Actions > Embed Image. This will make the file size larger, but it is necessary for publication.

To redude the size of the bitmap figure, you can use the following steps:
- Select the object you want to rasterize
- Go to Objet > Rasterize
- In the Rasterize window, select the following options:
    - Resolution: 500 ppi
    - Background: Transparent
    - Color Mode: RGB
    - Anti-aliasing: Art Optimized

This will probably give y ou good results. If you find that the figures became too pixely, you can try to increase the resolution to 1000 ppi. But be careful, this will increase the size of the file, so try to find a tradeoff between size and quality.


# Graphics design consistency

- **Use the same font for all your figures**. For info, here is what I use: 
    - tick labels: Decima Regular 6pt
    - axis labels: Aktiv Grotesk Condensed Regular 7pt
    - legend: Aktiv Grotesk Condensed Regular  6pt
    - Annotation: Aktiv Grotesk Condensed Regular 7pt
    - Subplot label: Aktiv Grotesk Condensed Bold 8pt
    - All with the same colors:  #2E3440 (true black usually not great)
- **Be consistent in your plotting**. For instance, all my plots have the same rules: 
    - tick length: 2pt
    - tick width: 0.5pt
    - axis width: 0.5pt
    - axis color: #2E3440 (true black usually not great)
    - unless emphasis, plot line width: 0.75pt
- **Be consistent in your colors**. Use the same colors if it is from the same sample/datset. 


# Saving 

UNless you have very specific reason, the figure would be better off saved as a vector compatible format (pdf, svg, eps, etc...). The PDF format came a long way and is now highly prefferable for embeding with LaTeX.

To save a pdf that is optimized for publication in a paper, install the [custom Adobe PDF Presets](./MyPapers.joboptions). In MacOS, go to ~/Library/Application Support/Adobe/Adobe PDF/Settings (if you don't know cmd+shift+G in Finder and paste the lcoation) and put the file there. Then, when you save a pdf, you can select the custom preset "MyPapers" in the dropdown menu. This will create a pdf with the following settings: 
- Standard: None
- Compatibility: Acrobat 5 (PDF 1.4)
- Preserve Illustrator Editing Capabilities: unchecked
- Embed Page Thumbnails: unchecked
- Optimize for Fast Web View: **checked**
- Preserve Hyperlinks: unchecked
- Compression to 300ppi
- Convert color to destination RGB and include profile

# Advices

- Your figures will probably never exeed more than 10MB. If that is the case, you either didn't rasterized properly your bitmap or you didn't process your data properly (e.g. way to many point that are useless.). The 10MB is a good rule of thumb in particular it makes it compatibel with Overleaf git server. 
- Keeping the size of your figure as it will apear in the manuscript helps you keep consistency over the element size (font, linestroke, etc..). After saving and while embeding the figure **YOU SHOULD NOT HAVE TO USE `[width=\textwidth]` in the `\includegraphics` command**. If you do, it means that your figure is not the right size, and you messed up somewhere 