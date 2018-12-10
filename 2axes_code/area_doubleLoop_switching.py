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
steps = 10

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

for x in range(steps+1):
    for y in range(steps+1):


        a_page()
        if x % 2 != 0: y = steps - y

        px = x * axis_w / (steps)
        py = y * axis_h / (steps)

        pts.append((px, py))

        fill(None)
        strokeWidth(1)
        stroke(0)

        for p, point in enumerate(pts[:-1]):
            line(point, (pts[p+1][0], pts[p+1][1]))

        stroke(None)
        fill(1, 0, 0)
        for p_x, p_y in pts:
            oval(p_x - dia/2, p_y - dia/2, dia, dia)

        fill(0, .8)

        var_values = { axes[0] : map_val(px, 0, axis_w, axis1_min, axis1_max), axes[1] : map_val(py, 0, axis_h, axis2_min, axis2_max) }

        fontVariations( **var_values )
        text(txt, (axis_w/2, axis_h/2), align='center')

        # saveImage('../imgs/%.3d.png' % pageCount())    

