import random
from ..bot_control import Move


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
        if self._hor_move is None:
            self._hor_move = Move.RIGHT if self.position[0] == 0 else Move.LEFT
            self._ver_move = Move.UP if self.position[1] == 0 else Move.DOWN

        _reached_left = self.position[0] == 0
        _reached_right = self.position[0] == grid.shape[0] - 1
        _reached_top = self.position[1] == grid.shape[0] - 1
        _reached_bot = self.position[1] == 0

        if not (_reached_bot or _reached_top or _reached_left or _reached_right):
            return self._hor_move
        elif _reached_left:
            if self._first_iter:
                self._hor_move = Move.RIGHT

                self._first_iter = False
                return self._ver_move
            self._first_iter = True
            return self._hor_move
        elif _reached_right:
            if self._first_iter:
                self._hor_move = Move.LEFT
                self._first_iter = False
                return self._ver_move
            self._first_iter = True
            return self._hor_move
        elif _reached_bot:
            self._ver_move = Move.UP
        elif _reached_top:
            self._ver_move = Move.DOWN
        return self._ver_move
