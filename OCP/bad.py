class Rectangle(object):

    def __init__(self, width, height):
        self.width = width
        self.height = height


class Square(object):

    def __init__(self, side):
        self.side = side


# And if I need to extend ShapePrinter?
class ShapePrinter(object):

    def draw_shape(self, shape):
        if type(shape) == Rectangle:
            # Draw rectangle: width != height
            pass
        elif type(shape) == Square:
            # Draw square: width == height
            pass
