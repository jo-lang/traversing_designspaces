# --------------------------
#  imports

import sys
sys.path.append("..")
from helper_functions import *

# --------------------------
#  settings

p_w, p_h = 300, 300
margin = 30
dia = 4
steps = 40

txt = 'vfonts'
f_name = 'Skia-Regular'

axis_w = p_w - 2 * margin
axis_h = p_h - 2 * margin

wght_min = listFontVariations(f_name)['wght']['minValue']
wght_def = listFontVariations(f_name)['wght']['defaultValue']
wght_max = listFontVariations(f_name)['wght']['maxValue']

wdth_min = listFontVariations(f_name)['wdth']['minValue']
wdth_def = listFontVariations(f_name)['wdth']['defaultValue']
wdth_max = listFontVariations(f_name)['wdth']['maxValue']


# --------------------------
#  functions 

def a_page():
    newPage(p_w,p_h)
    translate(margin, margin)

    fill(.75)
    rect(0, 0, axis_w, axis_h)

    fill(0)

    oval(-dia/2, -dia/2, dia, dia)
    oval(-dia/2 + axis_w, -dia/2, dia, dia)

    oval(-dia/2, -dia/2 + axis_h, dia, dia)
    oval(-dia/2 + axis_w, -dia/2 + axis_h, dia, dia)

    text('min|min', (0, -12), align ='center')
    text('max|min', (axis_w, -12), align ='center')

    text('min|max', (0, axis_h + 8),align ='center')
    text('max|max', (axis_w, axis_h + 8),align ='center')

    font(f_name)
    fontSize(80)
    

# --------------------------
#  Drawings 


pts = []
for st in range(steps):

    a_page()
    factor = st/steps

    x = ip(wght_min, wght_max, factor)
    y = ip(wdth_min, wdth_max, factor)

    pts.append((factor * axis_w, factor * axis_h))
    for px, py in pts:
        fill(1, 0, 0)
        oval(px - dia/2, py - dia/2, dia, dia)

    fill(0, .8)
    curr_wght = x
    curr_wdth = y
    
    fontVariations(wght = curr_wght, wdth = curr_wdth)
    text(txt, (axis_w/2, axis_h/2), align = 'center')
    
    