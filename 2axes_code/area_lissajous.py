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
    
    text('%.4f' % wght_min, (0 - 14, -12))
    text('%.4f' % wght_max, (axis_w - 14, -12))

    text('%.4f' % wdth_min, (-33, -3))
    text('%.4f' % wdth_max, (-33, axis_h -3))

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

    curr_wght = ip(wght_min, wght_max, x)
    curr_wdth = ip(wdth_min, wdth_max, y)
    
    fontVariations(wght = curr_wght, wdth = curr_wdth )
    fill(0, .8)
    text('vFonts', (axis_w/2, axis_h/2), align = 'center')
    
    fontVariations(resetVariations=True)
    font('LucidaGrande')
    fontSize(8)
    text('%.4f' % curr_wght, (px*axis_w - 14, -24))
    text('%.4f' % curr_wdth, (- 33, py*axis_h -3))

    # saveImage('~/Desktop/imgs/%.3d.png' % st)