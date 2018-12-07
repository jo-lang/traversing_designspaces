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


wght_min = listFontVariations(f_name)['wght']['minValue']
wght_max = listFontVariations(f_name)['wght']['maxValue']
wdth_min = listFontVariations(f_name)['wdth']['minValue']
wdth_max = listFontVariations(f_name)['wdth']['maxValue']


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

        curr_wght = map_val(px, 0, axis_w, wght_min, wght_max)
        curr_wdth = map_val(py, 0, axis_h, wdth_min, wdth_max)
    
        fontVariations(wght = curr_wght, wdth = curr_wdth )
        text(txt, (axis_w/2, axis_h/2), align='center')

        # saveImage('../imgs/%.3d.png' % pageCount())    

