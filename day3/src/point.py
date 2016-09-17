"""This module has classes that work with Points and Triangles"""

from math import sqrt


class Point(object):
    '''
    A 2d point class
    '''
    def __init__(self, x, y):
        '''
        Initialize a point with the given x and y coordinate values.
        '''
        self.x = x
        self.y = y

    def __repr__(self):
        '''
        Return a string representation of the point.
        '''
        return 'Point: {}, {}'.format(self.x, self.y)

    def __eq__(self, other):
        '''
        INPUT:
            - other: Point
        Return True iff this is the same point as other.
        '''
        if self.x == other.x and self.y == other.y:
            return True
        #     output = 'expected {0} equal to {1}'
        # else:
        #     output = 'expected {0} not equal to {1}'
        # return output.format(self, other)

    def __add__(self, other):
        '''
        INPUT:
            - other: Point
        Return a new Point which adds the x and y coordinates of the two points
        together.
        '''
        return Point(self.x+other.x, self.y+other.y)

    def __sub__(self, other):
        '''
        INPUT:
            - other: Point
        Return a new Point which subtracts
        the x and y coordinates of the second
        point from the first.
        '''
        return Point(self.x-other.x, self.y-other.y)

    def __mul__(self, other):
        '''
        INPUT:
            - other: int/float
        Return a new Point which multiplies both the x and y coordinate values
        by the given value.
        '''
        return Point(self.x * other, self.y * other)

    def length(self):
        '''
        Return the length of the vector (squareroot of the two values squared)
        '''
        return sqrt(self.x ** 2.0 + self.y ** 2.0)

    def dist(self, other):
        '''
        Return the distance (float) between this
        point and the other point given.

        Hint: You should use subtract and length!
        '''
        return (self.__sub__(other)).length()


class Triangle(object):
    def __init__(self, a, b, c, d, e, f):
        self.vertex1 = Point(a, b)
        self.vertex2 = Point(c, d)
        self.vertex3 = Point(e, f)

    def __repr__(self):
        lineformat = 'Triangle: {}, {}, {}'
        return lineformat.format(self.vertex1, self.vertex2, self.vertex3)

    def perimiter(self):
        sidea = Point.dist(self.vertex1, self.vertex2)
        sideb = Point.dist(self.vertex3, self.vertex2)
        sidec = Point.dist(self.vertex3, self.vertex1)
        return sidea+sideb+sidec

    def area(self):
        sidea = Point.dist(self.vertex1, self.vertex2)
        sideb = Point.dist(self.vertex3, self.vertex2)
        sidec = Point.dist(self.vertex3, self.vertex1)
        s = float((sidea+sideb+sidec)/2)
        return sqrt(s*(s-sidea)*(s-sideb)*(s-sidec))
