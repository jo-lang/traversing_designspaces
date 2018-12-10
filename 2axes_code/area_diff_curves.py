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

axes = ['wght', 'wdth'] 

axis1_min = listFontVariations(f_name)[axes[0]]['minValue']
axis1_max = listFontVariations(f_name)[axes[0]]['maxValue']

axis2_min = listFontVariations(f_name)[axes[1]]['minValue']
axis2_max = listFontVariations(f_name)[axes[1]]['maxValue']

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

    var_values = { axes[0] : axis1_min, axes[1] : axis2_min }
    fontVariations( **var_values )
    text('a', (0, -20), align ='center')
    var_values = { axes[0] : axis1_max, axes[1] : axis2_min }
    fontVariations( **var_values )
    text('a', (axis_w, -20), align ='center')
    var_values = { axes[0] : axis1_min, axes[1] : axis2_max }
    fontVariations( **var_values )
    text('a', (0, axis_h + 8),align ='center')
    var_values = { axes[0] : axis1_max, axes[1] : axis2_max }
    fontVariations( **var_values )
    text('a', (axis_w, axis_h + 8),align ='center')

    fontSize(120)

# --------------------------
#  Drawings 


pts = []
for st in range(steps+1):

    a_page()
    factor = st/steps

    x = ip(axis1_min, axis1_max, factor)
    y = lucas(axis2_min, axis2_max, st, (steps+1))

    pts.append((factor * axis_w, map_val(y, axis2_min, axis2_max, 0, axis_h)))
    for px, py in pts:
        fill(1, 0, 0)
        oval(px - dia/2, py - dia/2, dia, dia)

    fill(0, .9)
    var_values = { axes[0] : x, axes[1] : y }
    
    fontVariations(**var_values)
    text(txt, (axis_w/2, axis_h/2), align = 'center')

    # saveImage('../imgs/%.3d.png' % st)    
    