from abc import ABCMeta, abstractmethod


class Car(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def accelerate(self):
        pass


class Mustang(Car):

    def start(self):
        # start implementation
        pass

    def accelerate(self):
        # accelerate implementation
        pass


# After We need to create DeloRean class

class Car(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def accelerate(self):
        pass

    @abstractmethod
    def back_to_the_past(self):
        pass

    @abstractmethod
    def back_to_the_future(self):
        pass


class Mustang(Car):

    def start(self):
        # start implementation
        pass

    def accelerate(self):
        # accelerate implementation
        pass

    def back_to_the_past(self):  # ?
        pass

    def back_to_the_future(self):  # ?
        pass


class DeloRean(Car):
    def start(self):
        # start implementation
        pass

    def accelerate(self):
        # accelerate implementation
        pass

    def back_to_the_past(self):
        pass

    def back_to_the_future(self):
        pass
