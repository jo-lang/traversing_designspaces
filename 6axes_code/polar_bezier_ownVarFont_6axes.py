# --------------------------
#  imports

import sys
sys.path.append("..")
from helper_functions import *

# -------------------------
# settings 

pw = ph = 500
dia = 210
dot_s = 10

steps = 40


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

# -------------------------
# functions 

def base_chart(axes, s = 180, web = False):

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
        text('%.3f' % axes[axis]['maxValue'], (x + dot_s/2, y + dot_s/2))
        text('%.3f' % axes[axis]['minValue'], (-x  + dot_s/2, -y + dot_s/2))
        text('%s' % axes[axis]['name'], (x  + dot_s/2, -y - dot_s/2))
    
def base_page():
    newPage(pw, ph)
    fill(1)
    rect(0, 0, pw, ph)
    fill(0)
    translate(pw/2, ph/2)
    base_chart(axes, s = dia)
    stroke(None)
    fill(0)
    

# -------------------------
# drawings 

start = [-dia] * len(axes)
end   = [ dia] * len(axes)

t1 = [random() * -dia for _ in range(len(axes))]
t2 = [random() *  dia for _ in range(len(axes))]

all_polys = []


for st in range(steps+1):

    # newDrawing()
    base_page()
    dots = []
    factor = st / steps
    curr_p = get_p_at_t(start, t1, t2, end, factor)

    font(font_name)

    for a, val in enumerate(curr_p):

        x = cos(angle * a + pi/2) * val
        y = sin(angle * a + pi/2) * val

        fill( *cols[a] )
        oval(x - dot_s/2, y - dot_s/2, dot_s, dot_s)
        dots.append( (x,y) )

    fontVariations(
        ANLE = map_val(curr_p[0], -dia, dia, axes['ANLE']['minValue'], axes['ANLE']['maxValue']), 
        ANRI = map_val(curr_p[1], -dia, dia, axes['ANRI']['minValue'], axes['ANRI']['maxValue']), 
        WELE = map_val(curr_p[2], -dia, dia, axes['WELE']['minValue'], axes['WELE']['maxValue']), 
        WERI = map_val(curr_p[3], -dia, dia, axes['WERI']['minValue'], axes['WERI']['maxValue']), 
        WECE = map_val(curr_p[4], -dia, dia, axes['WECE']['minValue'], axes['WECE']['maxValue']), 
        HECE = map_val(curr_p[5], -dia, dia, axes['HECE']['minValue'], axes['HECE']['maxValue']), 
    )


    fill(0, .05)
    fill(None)
    stroke(0, .25)
    strokeWidth(.5)
    
    all_polys.append( dots )
    for poly in all_polys:
        polygon( *poly )
    font(font_name)
    fontSize(120)
    fill(0)
    stroke(None)
    text('A', (0, 0), align='center')

    # saveImage('~/Desktop/imgs/%.3d.png' % st)
