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

# these are the two tangent points for the bezier curve
t1 = 40, axis_h + 380
t2 = axis_w - 40, -380

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

    font(f_name)
    fontSize(32)
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

    x, y = get_p_at_t((0, 0), t1, t2, (axis_w, axis_h), factor) 

    pts.append((x, y))
    for px, py in pts:
        fill(1, 0, 0)
        oval(px - dia/2, py - dia/2, dia, dia)

    curr_wght = map_val(x, 0, axis_w, wght_min, wght_max)
    curr_wdth = map_val(y, 0, axis_h, wdth_min, wdth_max)

    fill(0, .75)
    fontVariations(wght = curr_wght, wdth = curr_wdth )
    text('vfont', (axis_w/2, axis_h/2), align = 'center')
    
    fill(0, 1, 0)
    rect(t1[0] - dia/2, t1[1] - dia/2, dia, dia)
    rect(t2[0] - dia/2, t2[1] - dia/2, dia, dia)

    # saveImage('../imgs/%.3d.png' % st)