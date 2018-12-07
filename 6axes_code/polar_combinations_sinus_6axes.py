# --------------------------
#  imports

import itertools
import sys
sys.path.append("..")
from helper_functions import *

# -------------------------
# settings 

pw = ph = 500
dia = 210

dot_s = 10
steps = 10

font_name = '../fonts/varA.ttf'
selected_axes = [ 'ANLE', 'ANRI', 'WELE', 'WERI', 'WECE', 'HECE' ] 

axes = { axis : listFontVariations(font_name)[axis] for axis in selected_axes }
angle = pi/len(axes)
combis = list(itertools.product([-1, 1], repeat=6))


cols = [ 
    (22/255, 96/255, 168/255, .75), 
    (1, 106/255, 0, .75), 
    (34/255, 149/255, 26/255, .75), 
    (205/255, 12/255, 25/255, .75), 
    (129/255, 76/255, 177/255, .75), 
    (122/255, 67/255, 57/255, .75)
    ]

# -------------------------
# functions 

def base_chart(axes, s = 180, web = False):

    angle = pi/len(axes)
    for a, axis in enumerate(axes):

        fill(None)
        strokeWidth(.5)
        stroke( * cols[a])
        x = cos(angle * a + pi/2) * s
        y = sin(angle * a + pi/2) * s
        
        line( (0, 0), (x, y))
        line( (0, 0), (-x, -y))
        
        stroke(None)
        fill(0)
        text('%d' % axes[axis]['maxValue'], (x + dot_s/2, y + dot_s/2))
        text('%d' % axes[axis]['minValue'], (-x  + dot_s/2, -y + dot_s/2))
        text('%s' % axes[axis]['name'], (x  + dot_s/2, y - dot_s/2))

   
def base_page():
    newPage(pw, ph)
    fill(1)
    rect(0, 0, pw, ph)
    translate(pw/2, ph/2)
    base_chart(axes, s = dia)
    stroke(None)
    fill(0)
    

# -------------------------
# drawings  


for c, combi in enumerate(combis):


    for step in range(steps):
    
        f = .5 + .5 * cos(step/steps * pi + pi)

        # newDrawing()
        base_page()

        inter_combi = [ip(combis[c-1][a], ax_val, f) for a, ax_val in enumerate(combi) ]

        dots = []
        vals = []

        for v, val in enumerate(inter_combi):
            x = cos(angle * v + pi/2) * val * dia
            y = sin(angle * v + pi/2) * val * dia

            vals.append( map_val(val, -1, 1, 0, 1) )
            fill( *cols[v] )
            oval(x - dot_s/2, y - dot_s/2, dot_s, dot_s)
            dots.append((x, y))

        fontVariations(
            ANLE = ip(axes['ANLE']['minValue'], axes['ANLE']['maxValue'], vals[0]), 
            ANRI = ip(axes['ANRI']['minValue'], axes['ANRI']['maxValue'], vals[1]), 
            WELE = ip(axes['WELE']['minValue'], axes['WELE']['maxValue'], vals[2]), 
            WERI = ip(axes['WERI']['minValue'], axes['WERI']['maxValue'], vals[3]), 
            WECE = ip(axes['WECE']['minValue'], axes['WECE']['maxValue'], vals[4]), 
            HECE = ip(axes['HECE']['minValue'], axes['HECE']['maxValue'], vals[5]), 
        )

        font(font_name)
        fontSize(120)
        fill(0)
        stroke(None)
        text('A', (0, 0), align = 'center' )

        # saveImage('~/Desktop/imgs/%.3d.png' % (c * steps + step) )

