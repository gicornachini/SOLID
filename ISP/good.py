from abc import ABCMeta, abstractmethod


class Car(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def accelerate(self):
        pass


class TimeMachine(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def back_to_the_past(self):
        pass

    @abstractmethod
    def back_to_the_future(self):
        pass


class Mustang(Car):

    def start(self): pass

    def accelerate(self): pass


class DeloRean(Car, TimeMachine):
    def start(self): pass

    def accelerate(self): pass

    def back_to_the_past(self): pass

    def back_to_the_future(self): pass
