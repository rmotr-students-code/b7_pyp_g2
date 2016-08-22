class Fly(object):
    def fly(self):
        print("'%s' is Flying" % self.name)


class Move(object):
    def __init__(self):
        self.name = 'A'

    def move(self):
        # self == b
        print("'%s' is Moving" % self.name)


class Airplane(Move, Fly):
    def __init__(self, name):
        self.name = name


a = Airplane('747')
a.move()
# a.fly()