hosts = Hosts()
hosts = hosts + Host()

class Player(object):
    pass


class Board(object):
    pass


class Game(object):
    def move(self, player, position):
        row, col = position
        # checking if valid depends on the board
        # winning depends on Board
        self.board.move(player.name, positio)

p1 = Player('X')
p2 = Player('O')
game = Game(p1, p2)
game.move(p1, (0, 2))


class Cell(object):
    pass


class Move(object):
    pass