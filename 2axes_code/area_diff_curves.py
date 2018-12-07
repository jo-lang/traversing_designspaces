# --------------------------
#  imports

import sys
sys.path.append("..")
from helper_functions import *

# --------------------------
#  settings

p_w, p_h = 500, 500
margin = 30
dia = 4
steps = 40


txt = 'vfonts'
f_name = 'Skia-Regular'

wght_min = listFontVariations(f_name)['wght']['minValue']
wght_max = listFontVariations(f_name)['wght']['maxValue']

wdth_min = listFontVariations(f_name)['wdth']['minValue']
wdth_max = listFontVariations(f_name)['wdth']['maxValue']

axis_w = p_w - 2 * margin
axis_h = p_h - 2 * margin


# --------------------------
#  functions 

def a_page():
    '''Make a base page with the designspace in the background'''
    newPage(p_w,p_h)
    fill(1)
    rect(0, 0, p_w, p_h)
    translate(margin, margin)

    fill(.75)
    rect(0, 0, axis_w, axis_h)

    fill(0)

    oval(-dia/2, -dia/2, dia, dia)
    oval(-dia/2 + axis_w, -dia/2, dia, dia)

    oval(-dia/2, -dia/2 + axis_h, dia, dia)
    oval(-dia/2 + axis_w, -dia/2 + axis_h, dia, dia)

    fontSize(32)
    font(f_name)

    fontVariations(wght = wght_min, wdth = wdth_min )
    text('a', (0, -20), align ='center')
    fontVariations(wght = wght_max, wdth = wdth_min )
    text('a', (axis_w, -20), align ='center')
    fontVariations(wght = wght_min, wdth = wdth_max )
    text('a', (0, axis_h + 8),align ='center')
    fontVariations(wght = wght_max, wdth = wdth_max )
    text('a', (axis_w, axis_h + 8),align ='center')

    fontSize(120)

# --------------------------
#  Drawings 


pts = []
for st in range(steps+1):

    a_page()
    factor = st/steps

    x = ip(wdth_min, wdth_max, factor)
    y = lucas(wght_min, wght_max, st, (steps+1))

    pts.append((factor * axis_w, map_val(y, wght_min, wght_max, 0, axis_h)))
    for px, py in pts:
        fill(1, 0, 0)
        oval(px - dia/2, py - dia/2, dia, dia)

    fill(0, .9)
    curr_wght = y
    curr_wdth = x
    
    fontVariations(wght = curr_wght, wdth = curr_wdth )
    text(txt, (axis_w/2, axis_h/2), align = 'center')

    # saveImage('../imgs/%.3d.png' % st)    
    