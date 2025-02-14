# 🏗️ Under Constructions🏗️

# What is it? 

# How to use it? 

## Quick reminder for Blender and Settings


## Assets Available 

In the file [`Assets.blend`](./Assets/Assests.blend), several geoemtry are defined and can be used later on in your own blender file: 
- Straight wavevguide ring resonator 
- Pulley coupled ring resonator 
- Straight waveguide photonics crystal ring resonator
- Single soliton in a microring

Note that all these assests have a material that is defined to be used with Eevee, similar to the ready-made model discussed later. If you want to go with cycle and provide a more realistic render (glasses and so on), you will need to tweak the material.


To use them, open the [`Assets.blend`](./Assets/Assests.blend) and flag each element of interst as asset (right click → mark as asset). 

In the Blender setting, add the folder where you store the `Assets.blend` in your computer. 

Now you can open a asset panel and you would only need to drag an drop into the 3D viewport to have the object 

## Ready made models 

If you don't care much about tweaking everything (lighting and co), there are 3 files that are provided and can be tweaked as needed: 
- [RingCaroon.blend](./MiscModels/RingCaroon.blend): toon like render of a micriring resonator. Pretty useful for paper as it gives a neat professional render without the unecessary fuzz of pseudo-realistic render. Quite useful to then use in Adobe Illustrator to add parameter on the system (such as in the fiugre of this paper).The rendered background is transparent to make it less weird in paper figures. Render in eevee
- [CladdingRing.blend](./MiscModels/CladdingRing.blend): a more realistic render with some fuzz and interesting stuff that some may like. Render in eeve
- [???](): a pretty cool render that I use mostly as the background of the title page of a slidedeck. Since there are transparency and some light effect, it renderes in cycle (so you will need a good GPU). There is a layer of postprocessing that can also be tweaked, providing the different psychadelic light render. 



## Creating an image

Just a quick remindr. Play with to get the angle you want. Go to Render → render image, and save as a png/tiff/whatever you want. 

## Some tutorials 

[![Demo CountPages alpha](https://img.youtube.com/vi/rj1BpFC8rmU/0.jpg)](https://youtu.be/rj1BpFC8rmU?si=9B-U8giXcsKT2VlK)
