from ..bot_control import Move
import gc
import time
import threading
import numpy as np
import weakref

UP = Move.UP
DOWN = Move.DOWN
LEFT = Move.LEFT
RIGHT = Move.RIGHT

FIRST_ZERO = RIGHT
FIRST_ELSE = LEFT

SECOND_ZERO = UP
SECOND_ELSE = DOWN


def loop(rothko):
    obj = rothko()
    prev_pos = obj.position
    last_update = time.time()
    while obj and obj.c_round < obj.n_rounds:
        if not np.array_equal(obj.position, prev_pos):
            obj.next = obj.decide_move()
            prev_pos = obj.position
            last_update = time.time()

        obj = None
        obj = rothko()
        time.sleep(0.01)


class RapidRothko:
    def __init__(self):
        self._size = 0
        self._move_ver = UP
        self._move_hor = LEFT
        self._first_iter = True

        self.position = np.array([0, 0], dtype=np.int16)

        self.n_rounds = 10000
        self.c_round = 0

        self._update_thread = threading.Thread(target=loop, args=(weakref.ref(self),))
        self._update_thread.start()

        self.next = Move.LEFT

    def decide_move(self):
        _x = self.position[0]
        _reached_zero = _x == 0

        if _reached_zero or _x == self._size:
            if self._first_iter:
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

    def get_name(self):
        return "RapidRothko"

    def get_contributor(self):
        return "Jorik de Vries"

    def determine_next_move(self, grid, enemies, game_info):
        if not self._size:
            self._size = grid.shape[0] - 1
            self.n_rounds = game_info.number_of_rounds
        self.c_round = game_info.current_round
        return self.next
