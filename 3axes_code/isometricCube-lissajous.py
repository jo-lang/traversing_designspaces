# --------------------------
#  imports

import math, itertools, sys
sys.path.append("..")
from helper_functions import *

# --------------------------
#  settings

pw = ph = 500
cube_s = 250
steps = 200

tail = 50
dia = 6

# angles for isometric projection 
alpha = asin ( tan(radians(20)) )
beta  = radians(60)

# lissajous values
a = 1
b = a + 2
c = b + 1
delta = pi/3 #, pi/3, pi/4

angle = 2 * pi / steps
pts = [(sin( a * angle * st + delta ), sin( b * angle * st ), sin( c * angle * st )) for st in range(steps)]

f_name = '../fonts/hope.ttf'

var_info_dict = listFontVariations(f_name)


print ('Possible variable axes: ', ', '.join([k for k in var_info_dict.keys()]))

# define a list of three axis tags
axes = ['wght', 'wdth', 'CONT'] 
# or just use the dictionary 
# axes = var_info_dict.keys()
extremes = [(var_info_dict[a]['minValue'], var_info_dict[a]['maxValue']) for a in axes ]
assert len(axes) == 3, 'The axes should be limited to three. Currently there are %d.' % len(axes)

# for k, v in listFontVariations(f_name).items(): print (k,v)


# --------------------------
#  functions 

def convPoint(point, alpha, beta):
    x_, y_, z_ = point    
    x = cos(beta) * x_ - sin(beta) * z_
    y = sin(alpha) * sin(beta) * x_ + cos(alpha) * y_ + sin(alpha) * cos(beta) * z_
    z = cos(alpha) * sin(beta) * x_ - sin(alpha) * y_ + cos(alpha) * cos(beta) * z_
    return x, y


def a_cube(s, alpha, beta):

    fill(None)
    strokeWidth(1)

    stroke(.75)
    line(  convPoint( ( -s/2, -s/2, -s/2), alpha, beta ),
           convPoint( ( -s/2, -s/2,  s/2), alpha, beta ) )
    line(  convPoint( (  s/2, -s/2, -s/2), alpha, beta ),
           convPoint( (  s/2, -s/2,  s/2), alpha, beta ) )
    line(  convPoint( (  s/2,  s/2, -s/2), alpha, beta ),
           convPoint( (  s/2,  s/2,  s/2), alpha, beta ) )
    line(  convPoint( ( -s/2,  s/2, -s/2), alpha, beta ),
           convPoint( ( -s/2,  s/2,  s/2), alpha, beta ) )
    line(  convPoint( (  s/2, -s/2,  s/2), alpha, beta ),
           convPoint( (  s/2,  s/2,  s/2), alpha, beta ) )
    line(  convPoint( (  s/2, -s/2, -s/2), alpha, beta ),
           convPoint( (  s/2,  s/2, -s/2), alpha, beta ) )
    line(  convPoint( ( -s/2, -s/2,  s/2), alpha, beta ),
           convPoint( ( -s/2,  s/2,  s/2), alpha, beta ) )
    line(  convPoint( ( -s/2, -s/2, -s/2), alpha, beta ),
           convPoint( ( -s/2,  s/2, -s/2), alpha, beta ) )
    line(  convPoint( ( -s/2, -s/2, -s/2), alpha, beta ),
           convPoint( (  s/2, -s/2, -s/2), alpha, beta ) )
    line(  convPoint( ( -s/2,  s/2, -s/2), alpha, beta ),
           convPoint( (  s/2,  s/2, -s/2), alpha, beta ) )
    line(  convPoint( ( -s/2, -s/2,  s/2), alpha, beta ),
           convPoint( (  s/2, -s/2,  s/2), alpha, beta ) )
    line(  convPoint( ( -s/2,  s/2,  s/2), alpha, beta ),
           convPoint( (  s/2,  s/2,  s/2), alpha, beta ) )
    
    strokeWidth(2)
    stroke(1, 0, 0)
    line(  convPoint( ( 0, 0, -s/2), alpha, beta ),
           convPoint( ( 0, 0,  s/2), alpha, beta ))
    stroke(0, 1, 0)
    line( convPoint( ( 0, -s/2, 0), alpha, beta ),
          convPoint( ( 0,  s/2, 0), alpha, beta ))
    stroke(0, 0, 1)
    line(  convPoint( ( -s/2, 0, 0), alpha, beta ),
           convPoint( (  s/2, 0, 0), alpha, beta ))

    strokeWidth(1)

    fill(1, 0, 0, .2)
    stroke(None)
    polygon( 
        convPoint( ( -s/2, 0, -s/2), alpha, beta ),
        convPoint( (  s/2, 0, -s/2), alpha, beta ),
        convPoint( (  s/2, 0,  s/2), alpha, beta ),
        convPoint( ( -s/2, 0,  s/2), alpha, beta ),
    )

    fill(0, 1, 0, .2)
    polygon( 
        convPoint( ( 0, -s/2, -s/2), alpha, beta ),
        convPoint( ( 0,  s/2, -s/2), alpha, beta ),
        convPoint( ( 0,  s/2,  s/2), alpha, beta ),
        convPoint( ( 0, -s/2,  s/2), alpha, beta ),
    )

    fill(0, 0, 1, .2)
    polygon( 
        convPoint( ( -s/2, -s/2, 0), alpha, beta ),
        convPoint( (  s/2, -s/2, 0), alpha, beta ),
        convPoint( (  s/2,  s/2, 0), alpha, beta ),
        convPoint( ( -s/2,  s/2, 0), alpha, beta ),
    )



def a_page():
    newPage(pw, ph)
    fill(1)
    rect(0, 0, pw, ph)
    translate(pw/2, ph/2)
    a_cube(cube_s, alpha, beta)
    font(f_name)
    fontSize(100)


# --------------------------
#  drawings


for st in range(steps):

    a_page()
    fill(1, 0, 0)
    
    for p in range(tail):
        d = dia * (1 - p/tail)
        x, y, z = pts[st-p]
        x1, y1 = convPoint( (cube_s/2*x, cube_s/2*y, cube_s/2*z), alpha, beta )
        oval(x1 - d/2, y1 - d/2, d, d)
    
    x, y, z = pts[st]
    
    var_values = { axis : map_val(pts[st][i], -1, 1, extremes[i][0], extremes[i][1])  for i, axis in enumerate(axes) }
    
    fill(0, .8)
    font(f_name)
    fontVariations(**var_values) 
    text('hope', (0, 0), align = 'center')

