# --------------------------
#  imports

import math, itertools

# --------------------------
#  settings

pw = ph = 500
cube_s = 250
dia = 8

alpha = asin ( tan(radians(20)) )
beta  = radians(60)

size(pw, ph)
translate(pw/2, ph/2)

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


a_cube(cube_s, alpha, beta)

fill(0)

    # points = [ (x * s/2, y * s/2, z * s/2) for x in [-1, 1] for y in [-1, 1] for z in [-1, 1] ]


cube_points = [ (x * cube_s/2, y * cube_s/2, z * cube_s/2) for x in [-1, 1] for y in [-1, 1] for z in [-1, 1] ]

# cube_points = [ 
#     # (0, 0, 0),
#     (0, 0,  cube_s/2),
#     (0, 0, -cube_s/2),
#     (0,  cube_s/2, 0),
#     (0, -cube_s/2, 0),
#     ( cube_s/2, 0, 0),
#     (-cube_s/2, 0, 0),
#     ]

convPoints = [ convPoint( p, alpha, beta ) for p in cube_points ]

combis = list(itertools.permutations(convPoints, len(convPoints)))

print (len(combis))

fill(None)
stroke(1, 0, 0)
polygon( *combis[444] )

fill(0)
stroke(None)
for p in convPoints:
    x, y = p
    oval(x - dia/2, y - dia/2, dia, dia)
    

# saveImage(['~/Desktop/insta/isometric.jpg'])