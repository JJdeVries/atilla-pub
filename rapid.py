from ..bot_control import Move

UP = Move.UP
DOWN = Move.DOWN
LEFT = Move.LEFT
RIGHT = Move.RIGHT

FIRST_ZERO = RIGHT
FIRST_ELSE = LEFT

SECOND_ZERO = UP
SECOND_ELSE = DOWN


class RapidRothko:
    def __init__(self):
        self._size = 0
        self._move_ver = UP
        self._move_hor = LEFT
        self._first_iter = True

        self._idx_one = 0
        self._idx_two = 1

    def get_name(self):
        return "RapidRothko"

    def get_contributor(self):
        return "Jorik de Vries"

    def determine_next_move(self, grid, enemies, game_info):
        _x = self.position[0]

        _reached_zero = _x == 0

        if _reached_zero or _x == self._size:
            if self._first_iter:
                if not self._size:
                    self._size = grid.shape[0] - 1

                self._move_hor = RIGHT if _reached_zero else LEFT

                _y = self.position[1]

                if _y == 0:
                    self._move_ver = UP

                elif _y == self._size:
                    self._move_ver = DOWN

                self._first_iter = False
                return self._move_ver

            self._first_iter = True
        return self._move_hor
