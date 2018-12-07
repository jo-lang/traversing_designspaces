# --------------------------
#  imports

import math, itertools, sys
sys.path.append("..")
from helper_functions import *

# --------------------------
#  settings

pw = ph = 500
cube_s = 250
dia = 8

alpha = asin ( tan(radians(20)) )
beta  = radians(60)

steps = 16

f_name = '../fonts/hope.ttf'

wght_min = listFontVariations(f_name)['wght']['minValue']
wght_max = listFontVariations(f_name)['wght']['maxValue']

wdth_min = listFontVariations(f_name)['wdth']['minValue']
wdth_max = listFontVariations(f_name)['wdth']['maxValue']

CONT_min = listFontVariations(f_name)['CONT']['minValue']
CONT_max = listFontVariations(f_name)['CONT']['maxValue']


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

    fill(0)
    font(f_name)
    fontSize(30)

    fontVariations(wght = wght_max, wdth = wdth_max, CONT = CONT_max )
    text('e', convPoint( (  s/2 + 10,  s/2 + 10,  s/2 + 10), alpha, beta ), align = 'center')

    fontVariations(wght = wght_max, wdth = wdth_max, CONT = CONT_min )
    text('e', convPoint( (  s/2 + 10,  s/2 + 10, -s/2 - 10), alpha, beta ), align = 'center')

    fontVariations(wght = wght_max, wdth = wdth_min, CONT = CONT_max )
    text('e', convPoint( (  s/2 + 10, -s/2 - 10,  s/2 + 10), alpha, beta ), align = 'center')

    fontVariations(wght = wght_max, wdth = wdth_min, CONT = CONT_min )
    text('e', convPoint( (  s/2 + 10, -s/2 - 10, -s/2 - 10), alpha, beta ), align = 'center')

    fontVariations(wght = wght_min, wdth = wdth_max, CONT = CONT_max )
    text('e', convPoint( ( -s/2 - 10,  s/2 + 10,  s/2 + 10), alpha, beta ), align = 'center')

    fontVariations(wght = wght_min, wdth = wdth_max, CONT = CONT_min )
    text('e', convPoint( ( -s/2 - 10,  s/2 + 10, -s/2 - 10), alpha, beta ), align = 'center')

    fontVariations(wght = wght_min, wdth = wdth_min, CONT = CONT_max )
    text('e', convPoint( ( -s/2 - 10, -s/2 - 10,  s/2 + 10), alpha, beta ), align = 'center')

    fontVariations(wght = wght_min, wdth = wdth_min, CONT = CONT_min )
    text('e', convPoint( ( -s/2 - 10, -s/2 - 10, -s/2 - 10), alpha, beta ), align = 'center')


def a_page():
    newPage(pw, ph)
    fill(1)
    rect(0, 0, pw, ph)
    translate(pw/2, ph/2)
    a_cube(cube_s, alpha, beta)
    font(f_name)
    fontSize(100)
    fill(0)
    lineJoin('round')



# --------------------------
#  drawings

cube_points = [ (x, y, z) for x in [-1, 1] for y in [-1, 1] for z in [-1, 1] ]
combis = list(itertools.permutations(cube_points, len(cube_points)))

print ('%d possible paths to visit all corners of a cube.' % len(combis))

choice = int(random() * len(combis))
# choice = 5698, 4683

selected_order = combis[ choice ]
print ('Selected path is nr: %d' % choice)

convPoints = [ convPoint( (x * cube_s/2, y * cube_s/2, z * cube_s/2), alpha, beta ) for x, y, z in selected_order ]


page_count = 0
for p, point in enumerate(selected_order):
    
    x1, y1, z1 = point
    x2, y2, z2 = selected_order[p-1] 
    
    for st in range(steps):

        # newDrawing()
        a_page()

        fill(None)
        stroke(1, 0, 0)
        
        polygon( *convPoints )


        fill(0)
        stroke(None)

        f = .5 + .5 * cos(st/steps * pi + pi)

        x, y, z = ip(x2, x1, f), ip(y2, y1, f), ip(z2, z1, f)
        
        plot_x, plot_y = convPoint( (x * cube_s/2, y * cube_s/2, z * cube_s/2), alpha, beta )
        oval(plot_x - dia/2, plot_y - dia/2, dia, dia)

        curr_wght = map_val(x, -1, 1, wght_min, wght_max)
        curr_wdth = map_val(y, -1, 1, wdth_min, wdth_max)
        curr_CONT = map_val(z, -1, 1, CONT_min, CONT_max)
    
        fill(0, .8)
        fontVariations(CONT = curr_CONT, wght = curr_wght, wdth = curr_wdth) 
        text('hope', (0, 0), align = 'center')

        # saveImage( '~/Desktop/imgs/%.3d.png' % page_count )
        page_count += 1