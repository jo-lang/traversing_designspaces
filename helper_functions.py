# Some helper functions for interpolation et cetera.

def map_val(value, in_min, in_max, out_min, out_max):
	'''
	map_val(value, in_min, in_max, out_min, out_max)
	Maps a value between the range in_min and in_max to a new range between out_min and out_max.
	''' 
	return out_min + ((value - in_min) / (in_max - in_min) * (out_max - out_min))

def ip(min_val, max_val, factor): 
	'''
	ip(min_val, max_val, factor)
	Returns the interpolated value between a minimum and a maximum value. 
	Factor should be between 0 and 1, otherwise it will extrapolate.
	'''
	return min_val + factor * (max_val-min_val)

def inter_point(p1, p2, factor):
	'''
	ip(point1, point2, factor)
	Returns an interpolated point (x, y) at the factor. 
	Factor should be between 0 and 1, otherwise it will extrapolate.
	'''
	return ip(p1[0], p2[0], factor), ip(p1[1], p2[1], factor)


def get_val_at_t(p1, t1, t2, p2, t):
	'''
	get_val_at_t(p1, t1, t2, p2, t)
	Returns the of a bezier curve value at time t between p1 and p2
	where t1 and t2 are the tangent values and 
	'''
	return (1 - t)**3 * p1 + 3*(1 - t)**2 * t * t1 + 3*(1 - t)* t**2 * t2 + t **3 * p2

def get_axis_val(p1, t1, t2, p2, coordinate, t):
	'''
	get_axis_val(p1, t1, t2, p2, coordinate, t)
	get the value of coordinate n at time (t) on a bezier curve. 
	coordinate should be the index of the coordinate that should get returned.
	'''
	return (1 - t)**3 * p1[coordinate] + 3*(1 - t)**2 * t * t1[coordinate] + 3*(1 - t)* t**2 * t2[coordinate] + t **3 * p2[coordinate]

def get_p_at_t(p1, t1, t2, p2, t):
	'''
	get_p_at_t(p1, t1, t2, p2, t)
	returns the point (of n dimensions) at time (t) on a bezier curve.
	'''
	return [ get_axis_val(p1, t1, t2, p2, coordinate, t) for coordinate in range(len(p1)) ]

def lucas( min_val, max_val, step, steps ):
	factor = max_val / min_val
	return min_val * factor **(step/(steps-1))
