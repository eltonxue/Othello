# othello_point.py ICS 32 Lab. Elton Xue 52611936

class Point:
    def __init__(self, frac_x: float, frac_y: float):
        'Initializes the class Point'''
        self._frac_x = frac_x
        self._frac_y = frac_y

    def frac(self) -> (float, float):
        '''Returns the fractional x and fractional y in a tuple'''
        return (self._frac_x, self._frac_y)

    def pixel(self, width: float, height: float) -> (float, float):
        '''Returns the fractional x and fractional y changed
        into pixels in relation to parameters width and height'''
        return (self._frac_x * width, self._frac_y * height)
    

def from_frac(frac_x: float, frac_y: float) -> Point:
    '''Takes a fractional x and fractional y and returns a Point class'''
    return Point(frac_x, frac_y)

def from_pixel(pixel_x: float, pixel_y: float, width: float, height: float) -> Point:
    '''Returns a Point class through conversion using points in pixel form
    in relation to parameters width and height'''
    return Point(pixel_x / width, pixel_y / height)


