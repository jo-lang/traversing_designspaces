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
f_name = 'AmstelvarAlpha-Default'

axes = ['wght', 'wdth'] 

# --------
axis1_min = listFontVariations(f_name)[axes[0]]['minValue']
axis1_def = listFontVariations(f_name)[axes[0]]['defaultValue']
axis1_max = listFontVariations(f_name)[axes[0]]['maxValue']

axis2_min = listFontVariations(f_name)[axes[1]]['minValue']
axis2_def = listFontVariations(f_name)[axes[1]]['defaultValue']
axis2_max = listFontVariations(f_name)[axes[1]]['maxValue']

axis_w = p_w - 2 * margin
axis_h = p_h - 2 * margin

def_x = map_val(axis1_def, axis1_min, axis1_max, 0, axis_w)
def_y = map_val(axis2_def, axis2_min, axis2_max, 0, axis_h)

# --------------------------
#  functions 

def a_page():
    newPage(p_w,p_h)
    font(f_name)
    fontSize(32)

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

    oval(def_x - dia/2, def_y - dia/2, dia, dia)

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

for st in range(steps):

    a_page()
    
    angle = 2 * pi / steps * st

    x = .5 + cos(angle) * .5
    y = .5 + sin(angle) * .5

    pts.append((x, y))
    for px, py in pts:
        fill(1, 0, 0)
        oval(px*axis_w - dia/2, py*axis_h - dia/2, dia, dia)

    fill(0, .8)

    var_values = { axes[0] : ip(axis1_min, axis1_max, x), axes[1] : ip(axis2_min, axis2_max, y) }
    
    fontVariations( **var_values )
    text(txt, (axis_w/2, axis_h/2), align = 'center')
    
    # saveImage('../imgs/%.3d.png' % st)
    
    