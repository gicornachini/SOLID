from abc import ABCMeta, abstractmethod


class Shape(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def draw(self):
        pass


class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self):
        # Override Shape draw method
        pass


class Square(Shape):

    def __init__(self, side):
        self.side = side

    def draw(self):
        # Override Shape draw method
        pass


class ShapePrinter(object):

    def draw_shape(self, shape):
        shape.draw()
