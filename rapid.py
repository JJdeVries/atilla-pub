import random
from ..bot_control import Move

UP = Move.UP
DOWN = Move.DOWN
LEFT = Move.LEFT
RIGHT = Move.RIGHT

SIZE = 0


class RapidRothko:
    def __init__(self):
        self._hor_move = None
        self._ver_move = None

        self._first_iter = True

    def get_name(self):
        return "RapidRothko"

    def get_contributor(self):
        return "Jorik de Vries"

    def determine_next_move(self, grid, enemies, game_info):
        _x = self.position[0]
        if self._hor_move is None:
            self._hor_move = RIGHT if _x == 0 else LEFT
            self._ver_move = UP if self.position[1] == 0 else DOWN
            global SIZE
            SIZE = grid.shape[0] - 1

        _reached_left = _x == 0
        _reached_right = _x == SIZE

        if _reached_left or _reached_right:
            _y = self.position[1]
            if _y == 0:
                self._ver_move = UP
            elif _y == SIZE:
                self._ver_move = DOWN

            if _reached_left:
                if self._first_iter:
                    self._hor_move = RIGHT
                    self._first_iter = False
                    return self._ver_move
                self._first_iter = True
            elif _reached_right:
                if self._first_iter:
                    self._hor_move = LEFT
                    self._first_iter = False
                    return self._ver_move
                self._first_iter = True
        return self._hor_move
