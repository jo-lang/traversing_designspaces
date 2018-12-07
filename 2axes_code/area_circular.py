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
wght_def = listFontVariations(f_name)['wght']['defaultValue']
wght_max = listFontVariations(f_name)['wght']['maxValue']

wdth_min = listFontVariations(f_name)['wdth']['minValue']
wdth_def = listFontVariations(f_name)['wdth']['defaultValue']
wdth_max = listFontVariations(f_name)['wdth']['maxValue']

axis_w = p_w - 2 * margin
axis_h = p_h - 2 * margin

def_x = map_val(wght_def, wght_min, wght_max, 0, axis_w)
def_y = map_val(wdth_def, wdth_min, wdth_max, 0, axis_h)

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
    curr_wght = ip(wght_min, wght_max, x)
    curr_wdth = ip(wdth_min, wdth_max, y)
    
    fontVariations(wght = curr_wght, wdth = curr_wdth )
    text(txt, (axis_w/2, axis_h/2), align = 'center')
    
    # saveImage('../imgs/%.3d.png' % st)
    
    