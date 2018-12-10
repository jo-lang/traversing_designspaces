# --------------------------
#  imports

import sys
sys.path.append("..")
from helper_functions import *

# --------------------------
#  settings

p_w, p_h = 500, 500
margin = 40
dia = 4
steps = 200

# lissajous values
a = 2 # 2, 3, 4 are decent values
b = a + 1
delta = 0 # pi/2, pi/3, pi/4

f_name = "Skia-Regular"

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
    fill(1)
    rect(0, 0, p_w, p_h)
    translate(margin, margin)
    fontSize(8)

    fill(.75)
    rect(0, 0, axis_w, axis_h)

    fill(0)

    oval(-dia/2, -dia/2, dia, dia)
    oval(-dia/2 + axis_w, -dia/2, dia, dia)

    oval(-dia/2, -dia/2 + axis_h, dia, dia)
    oval(-dia/2 + axis_w, -dia/2 + axis_h, dia, dia)

    oval(-dia/2 + def_x, -dia/2 + def_y, dia, dia)
    
    text('%.4f' % axis1_min, (0 - 14, -12))
    text('%.4f' % axis1_max, (axis_w - 14, -12))

    text('%.4f' % axis2_min, (-33, -3))
    text('%.4f' % axis1_max, (-33, axis_h -3))

    font(f_name)
    fontSize(120)


# --------------------------
#  Drawings 

pts = []
for st in range(steps):

    # newDrawing()
    a_page()

    angle = 2 * pi / steps * st

    x = .5 + .5 * sin( a * angle + delta )
    y = .5 + .5 * sin( b * angle )

    pts.append((x, y))
    for px, py in pts:
        fill(1, 0, 0)
        oval(px*axis_w - dia/2, py*axis_h - dia/2, dia, dia)

    curr_axis1 = ip(axis1_min, axis1_max, x)
    curr_axis2 = ip(axis2_min, axis2_max, y)
    var_values = { axes[0] : curr_axis1, axes[1] : curr_axis2 }    
    fontVariations(**var_values)
    fill(0, .8)
    text('vFonts', (axis_w/2, axis_h/2), align = 'center')
    
    fontVariations(resetVariations=True)
    font('LucidaGrande')
    fontSize(8)
    text('%.4f' % curr_axis1, (px*axis_w - 14, -24))
    text('%.4f' % curr_axis2, (- 33, py*axis_h -3))

    # saveImage('../imgs/%.3d.png' % st)