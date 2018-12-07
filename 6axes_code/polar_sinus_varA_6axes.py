# --------------------------
#  imports

import sys
sys.path.append("..")
from helper_functions import *

# --------------------------
#  settings

pw = ph = 500
dia = 220

dot_s = 10
steps = 60

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

# --------------------------
#  functions 

def base_chart(axes, s = 180, web = False):

    for a, axis in enumerate(axes):

        fill(None)
        strokeWidth(.5)
        stroke( * cols[a])
        x = cos(angle * (a) - pi/2) * s
        y = sin(angle * (a) - pi/2) * s
        
        line( (0, 0), (x, y))
        line( (0, 0), (-x, -y))
        
        stroke(None)
        fill(0)
        text('%.3f' % axes[axis]['maxValue'], (x + dot_s/2, y + dot_s/2))
        text('%.3f' % axes[axis]['minValue'], (-x  + dot_s/2, -y + dot_s/2))
        text('%s' % axes[axis]['name'], (-x  + dot_s/2, -y - dot_s/2))
    
def base_page():
    newPage(pw, ph)
    fill(1)
    rect(0, 0, pw, ph)
    translate(pw/2, ph/2)
    base_chart(axes, s = dia)
    stroke(None)
    fill(0)
    

# --------------------------
#  drawings 

all_polys = []

for st in range(steps+1):

    base_page()
    dots = []
    factor = st / steps

    font(font_name)
    vals = []

    for a, axis in enumerate(axes):

        slider_pos = cos(2 * pi * factor + a * pi/len(axes)) * dia
        vals.append( slider_pos )
        x = cos(a * pi/len(axes) + pi/2) * slider_pos
        y = sin(a * pi/len(axes) + pi/2) * slider_pos 

        fill( *cols[a] )
        
        oval(x - dot_s/2, y - dot_s/2, dot_s, dot_s)
        dots.append( (x,y) )

    fontVariations(
        ANLE = map_val(vals[0], -dia, dia, axes['ANLE']['minValue'], axes['ANLE']['maxValue']), 
        ANRI = map_val(vals[1], -dia, dia, axes['ANRI']['minValue'], axes['ANRI']['maxValue']), 
        WELE = map_val(vals[2], -dia, dia, axes['WELE']['minValue'], axes['WELE']['maxValue']), 
        WERI = map_val(vals[3], -dia, dia, axes['WERI']['minValue'], axes['WERI']['maxValue']), 
        WECE = map_val(vals[4], -dia, dia, axes['WECE']['minValue'], axes['WECE']['maxValue']), 
        HECE = map_val(vals[5], -dia, dia, axes['HECE']['minValue'], axes['HECE']['maxValue']), 
    )

    fill(0, .05)
    fill(None)
    stroke(0, .15)
    strokeWidth(.5)
    
    
    all_polys.append( dots )
    for poly in all_polys:
        polygon( *poly )

    font(font_name)
    fontSize(pw/4)
    fill(0)
    stroke(None)
    text('A', (0, 0))

    # saveImage('~/Desktop/imgs/%.3d.png' % st)

