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
steps = 200

font_name = '../fonts/face.ttf'
selected_axes = [ 'LEBR', 'LEEH', 'LEEY', 'MOUT', 'NOSE', 'RIBR', 'RIEH', 'RIEY' ] 
axes = { axis : listFontVariations(font_name)[axis] for axis in selected_axes }

cols = [ 
    (22/255, 96/255, 168/255, .75), 
    (1, 106/255, 0, .75), 
    (34/255, 149/255, 26/255, .75), 
    (205/255, 12/255, 25/255, .75), 
    (129/255, 76/255, 177/255, .75), 
    (122/255, 67/255, 57/255, .75),
    (200/255, 67/255, 57/255, .75), 
    (5/255, 12/255, 25/255, .75), 
    ]

# --------------------------
#  settings 


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
    font('Menlo')


# --------------------------
#  settings  

for st in range(steps+1):

    # newDrawing()
    base_page()
    dots = []
    factor = st / steps

    font(font_name)

    vals = []

    for a, axis in enumerate(axes):

        slider_pos = sin( (a+1) * 2 * pi * factor )
        vFont_pos = .5 + slider_pos * .5
        vals.append( vFont_pos ) 

        x = cos(a * pi/len(axes) + pi/2) * slider_pos * dia
        y = sin(a * pi/len(axes) + pi/2) * slider_pos * dia

        fill( *cols[a] )
        
        oval(x - dot_s/2, y - dot_s/2, dot_s, dot_s)
        dots.append( (x,y) )

    fontVariations(
        LEBR = ip(axes['LEBR']['minValue'], axes['LEBR']['maxValue'], vals[0]), 
        LEEH = ip(axes['LEEH']['minValue'], axes['LEEH']['maxValue'], vals[1]), 
        LEEY = ip(axes['LEEY']['minValue'], axes['LEEY']['maxValue'], vals[2]), 
        MOUT = ip(axes['MOUT']['minValue'], axes['MOUT']['maxValue'], vals[3]), 
        NOSE = ip(axes['NOSE']['minValue'], axes['NOSE']['maxValue'], vals[4]), 
        RIBR = ip(axes['RIBR']['minValue'], axes['RIBR']['maxValue'], vals[5]), 
        RIEH = ip(axes['RIEH']['minValue'], axes['RIEH']['maxValue'], vals[6]), 
        RIEY = ip(axes['RIEY']['minValue'], axes['RIEY']['maxValue'], vals[7]), 

    )


    fill(0, .05)
    fill(None)
    stroke(0, .15)
    strokeWidth(.5)
        
    polygon( *dots )

    font(font_name)
    fontSize(400)
    fill(0)
    stroke(None)
    text('A', (0, -200), align = 'center' )

    # saveImage('~/Desktop/imgs/%.3d.png' % st)

