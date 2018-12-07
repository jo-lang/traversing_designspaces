# --------------------------
#  imports

import sys
sys.path.append("..")
from helper_functions import *

# --------------------------
#  settings

p_w, p_h = 300, 120
margin = 30
dia = 4
steps = 40
axis = 'wght'
f_name = 'Skia-Regular'


interpol = 'linear'
interpol = 'bezier'
interpol = 'luc_de_groot'
interpol = 'sinus'

axis_w = p_w - 2 * margin

min_val = listFontVariations(f_name)[axis]['minValue']
max_val = listFontVariations(f_name)[axis]['maxValue']
val_range = max_val - min_val

# --------------------------
#  functions 

def a_page():
    newPage(p_w*2,p_h*2)
    scale(2)
    fill(1)
    rect(0, 0, p_w, p_h)

    translate(margin, p_h/3)
    fill(.75)
    rect(0, -dia/2, axis_w, dia)

    fill(0)

    oval(-dia/2, -dia/2, dia, dia)
    oval(-dia/2 + axis_w, -dia/2, dia, dia)

    text('min', (0, -20))
    text('max', (axis_w, -20))

    font(f_name)
    fontSize(80)


# --------------------------
#  Drawings 

dots = []

if interpol == 'bezier':
    t1 = min_val + val_range * random()
    t2 = min_val + val_range * random()

    t1_map = map_val(t1, min_val, max_val, 0, axis_w)
    t2_map = map_val(t2, min_val, max_val, 0, axis_w)


for s in range(steps+1):

    a_page()

    if interpol == 'linear': 
        curr_val = min_val + s * val_range / steps
    elif interpol == 'sinus':
        curr_val = min_val + val_range/2 - sin(s/steps * pi + pi/2) * val_range/2
    elif interpol == 'luc_de_groot':
        curr_val = lucas( min_val, max_val, s, (steps+1))
    elif interpol == 'bezier':
        curr_val = get_val_at_t(min_val, t1, t2, max_val, s/steps)
        rect(t1_map-dia/2, - dia/2, dia, dia) 
        rect(t2_map-dia/2, - dia/2, dia, dia) 
    else:
        print ('%s interpolation not implemented' % interpol)
        break

    x = map_val(curr_val, min_val, max_val, 0, axis_w)
    
    fill(0)
    fontVariations( wght = curr_val )
    text('vfont', (0, p_h/8))

    fill(1, 0, 0)
    dots.append(x)
    for x in dots:
        oval(x-dia/2, - dia/2, dia, dia) 

    # saveImage('../imgs/%.3d.png' % s)


