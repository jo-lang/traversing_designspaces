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

axes = ['wght', 'wdth'] 

# --------
axis1_min = listFontVariations(f_name)[axes[0]]['minValue']
axis1_def = listFontVariations(f_name)[axes[0]]['defaultValue']
axis1_max = listFontVariations(f_name)[axes[0]]['maxValue']

axis2_min = listFontVariations(f_name)[axes[1]]['minValue']
axis2_def = listFontVariations(f_name)[axes[1]]['defaultValue']
axis2_max = listFontVariations(f_name)[axes[1]]['maxValue']


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

    x = ip(axis1_min, axis1_max, factor)
    y = ip(axis2_min, axis2_max, factor)

    pts.append((factor * axis_w, factor * axis_h))
    for px, py in pts:
        fill(1, 0, 0)
        oval(px - dia/2, py - dia/2, dia, dia)

    fill(0, .8)
    var_values = { axes[0] : x, axes[1] : y }
    
    fontVariations(**var_values)
    text(txt, (axis_w/2, axis_h/2), align = 'center')
    
    