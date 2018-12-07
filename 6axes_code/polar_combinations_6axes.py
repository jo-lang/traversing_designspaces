# --------------------------
#  imports

import itertools

# -------------------------
# settings 

pw = ph = 500
dia = 210
axes = 6
dot_s = 10


master_vals = [dia, 0, -dia]
master_vals = [dia, -dia]
combis = itertools.product(master_vals, repeat=6)


angle = pi/axes

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

def base_chart(axes = 6, s = 180, web = False):

    for arm in range(axes):
        
        fill(None)
        strokeWidth(.5)
        stroke( * cols[arm])
        x = cos(angle * arm + pi/2) * s
        y = sin(angle * arm + pi/2) * s
        
        line( (0, 0), (x, y))
        line( (0, 0), (-x, -y))
        
        stroke(None)
        fill(0)
        text('max', (x + dot_s/2, y + dot_s/2))
        text('min', (-x  + dot_s/2, -y + dot_s/2))
    text('def', (dot_s/2, dot_s/2))

    
def base_page():
    newPage(pw, ph)
    fill(1)
    rect(0, 0, pw, ph)
    translate(pw/2, ph/2)
    base_chart(axes = axes, s = dia)
    stroke(None)
    fill(0)
    

# -------------------------
# drawings  


for c, combi in enumerate(combis):

    # newDrawing()
    base_page()
    text('%d' % (c+1), (- pw/2 + dot_s, -ph/2 + dot_s))

    dots = []

    for a, axis in enumerate(combi):
        x = cos(angle * a + pi/2) * axis
        y = sin(angle * a + pi/2) * axis

        fill( *cols[a] )
        oval(x - dot_s/2, y - dot_s/2, dot_s, dot_s)
        dots.append((x, y))

    fill(0, .2)
    stroke(0)
    strokeWidth(1)
    polygon( *dots )
    # saveImage('../imgs/%.3d.png' % c)
    
    
    