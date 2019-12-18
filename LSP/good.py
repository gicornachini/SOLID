class FreeMan(object):

    def __init__(self, position):
        self.position = position

    def walk_north(self, dist):
        self.position[1] += dist

    def walk_south(self, dist):
        self.position[0] += dist


class Prisoner(object):  # Prisoner can't walk
    PRISON_LOCATION = (3, 3)

    def __init__(self):
        self.position = self.PRISON_LOCATION
