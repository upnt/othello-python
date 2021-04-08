from enum import Enum, auto


class Stone:
    def __init__(self, state):
        self.state = state

    def reverse(self):
        if self.state == Color.BLACK:
            self.state = Color.WHITE
            return

        if self.state == Color.WHITE:
            self.state = Color.BLACK
            return

    def __str__(self):
        if self.state == Color.BLACK:
            return '○'

        if self.state == Color.WHITE:
            return '●'

class Color(Enum):
    BLACK = auto()
    WHITE = auto()
