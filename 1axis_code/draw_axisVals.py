# --------------------------
#  settings

p_w, p_h = 500, 140
margin = 30
dia = 4

f_name = 'Skia-Regular'

axis_w = p_w - 2 * margin
axes = listFontVariations(f_name).keys()


# --------------------------
#  functions

def a_page():
    newPage(p_w,p_h)
    fill(1)
    rect(0, 0, p_w, p_h)
    translate(margin, p_h/2)
    fontSize(8)
    fill(.75)
    rect(0, -dia/2, axis_w, dia)
    fill(0)
    fontSize(12)


def map_vals(value, in_min, in_max, out_min, out_max):
    return out_min + ((value - in_min) / (in_max - in_min) * (out_max - out_min))


# --------------------------
#  drawings

for axis in axes:
    a_page()
    text('%s: %s axis' % (f_name, axis), (0, 40))

    for val in ['minValue', 'defaultValue', 'maxValue']:

        curr_val = listFontVariations(f_name)[axis][val]
        min_val  = listFontVariations(f_name)[axis]['minValue']
        max_val  = listFontVariations(f_name)[axis]['maxValue']
    
        fill(1, 0, 0)
        x = map_vals(curr_val, min_val, max_val, 0, axis_w)
        oval(x - dia/2, - dia/2, dia, dia) 
        fill(0)
        text('%.3f' % curr_val, (x, 12), align = 'center')
        text('%s' % val, (x, -42), align = 'center')

        var_values = { axis : curr_val }

        with savedState():
            font(f_name)
            fontSize(24)
            fontVariations( ** var_values )
            text('a', (x, -24), align = 'center')

    
    # saveImage('../images/axis_values_%d.png' % pageCount())