# --------------------------
#  imports

import sys
sys.path.append("..")
from helper_functions import *

# --------------------------
#  settings


pw = ph = 500
axis_l = 420
dot_s = 10
steps = 60

margin = (pw - axis_l)/2

font_name = '../fonts/varA.ttf'
selected_axes = [ 'ANLE', 'ANRI', 'WELE', 'WERI', 'WECE', 'HECE' ] 
axes = { axis : listFontVariations(font_name)[axis] for axis in selected_axes }

angle = pi/len(axes)

cols = [ 
    (22/255, 96/255, 168/255, .75), 
    (1, 106/255, 0, .75), 
    (34/255, 149/255, 26/255, .75), 
    (205/255, 12/255, 25/255, .75), 
    (129/255, 76/255, 177/255, .75), 
    (122/255, 67/255, 57/255, .75)
    ]


# ------------------------------------
# functions 


def base_chart(axes, l, web = False):

    for a, axis in enumerate(axes):

        fill(None)
        strokeWidth(.5)
        stroke( * cols[a])
        y = a * l/(len(axes)-1)

        line( (0, y), (axis_l, y))
        
        stroke(None)
        fill(0)
        text('%.3f' % axes[axis]['minValue'], (0, y + dot_s/2))
        text('%.3f' % axes[axis]['maxValue'], (axis_l, y + dot_s/2), align ='right')
        text('%s' % axes[axis]['name'], (0, y - dot_s))
    
def base_page():
    newPage(pw, ph)
    fill(1)
    rect(0, 0, pw, ph)
    translate(margin, margin)
    base_chart(axes, axis_l)
    stroke(None)
    fill(0)
    
# ------------------------------------
# drawings

all_polys = []

for st in range(steps):

    # newDrawing()
    base_page()
    factor = st / steps
    
    vals = []
    
    for a, axis in enumerate(axes):

        x = axis_l/2 + cos(pi*2 * factor + a * pi/len(axes)) * axis_l/2

        fill( *cols[a] )
        vals.append(x)
        oval(x - dot_s/2, a * (axis_l/(len(axes)-1))- dot_s/2, dot_s, dot_s)

    fontVariations(
        ANLE = map_val(vals[0], 0, axis_l, axes['ANLE']['minValue'], axes['ANLE']['maxValue']), 
        ANRI = map_val(vals[1], 0, axis_l, axes['ANRI']['minValue'], axes['ANRI']['maxValue']), 
        WELE = map_val(vals[2], 0, axis_l, axes['WELE']['minValue'], axes['WELE']['maxValue']), 
        WERI = map_val(vals[3], 0, axis_l, axes['WERI']['minValue'], axes['WERI']['maxValue']), 
        WECE = map_val(vals[4], 0, axis_l, axes['WECE']['minValue'], axes['WECE']['maxValue']), 
        HECE = map_val(vals[5], 0, axis_l, axes['HECE']['minValue'], axes['HECE']['maxValue']), 
    )

    fill(0, .05)
    fill(None)
    stroke(0, .25)
    strokeWidth(1)
    
    
    font(font_name)
    fontSize(pw/4)
    fill(0)
    stroke(None)
    text('A', (pw/3, ph/3))

    # saveImage('~/Desktop/imgs/%.3d.png' % st)
