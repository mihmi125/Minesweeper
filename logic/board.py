from logic.cell import Cell
from random import randint

class Board:
    def __init__(self, rows, cols, mine_count):
        self.rows = rows
        self.columns = cols
        self.mine_count = mine_count
        self.grid = [[Cell() for _ in range(cols)] for _ in range(rows)]
        self._setup_board()

    def _setup_board(self):
        self._place_mines()
        self._calculate_neighbors()

    def _place_mines(self):
        mines_placed = 0
        while mines_placed < self.mine_count:
            r = randint(0, self.rows - 1)
            c = randint(0, self.columns - 1)

            if not self.grid[r][c].is_mine:
                self.grid[r][c].is_mine = True
                mines_placed += 1

    def _get_neighbors(self, row, col):
        neighbors = []
        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                if (0 <= r < self.rows and 0 <= c < self.columns) and (r != row or c != col):
                    neighbors.append((r, c))
        return neighbors

    def _calculate_neighbors(self):
        for r in range(0, self.rows):
            for c in range(0, self.columns):
                if not self.grid[r][c].is_mine:
                    neighbor = self._get_neighbors(r, c)
                    mine_count = sum(1 for nr, nc in neighbor if self.grid[nr][nc].is_mine)
                    self.grid[r][c].neighbor_mines = mine_count

    def reveal_cell(self, r, c):
        cell = self.grid[r][c]
        if cell.is_revealed or cell.is_flagged:
            return True

        cell.is_revealed = True

        if cell.is_mine:
            self.reveal_all_mines()
            return False

        if cell.neighbor_mines == 0:
            for nr, nc in self._get_neighbors(r, c):
                self.reveal_cell(nr, nc)
        return True

    def toggle_flag(self, r, c):
        if not self.grid[r][c].is_revealed:
            self.grid[r][c].is_flagged = not self.grid[r][c].is_flagged

    def reveal_all_mines(self):
        for r in range(self.rows):
            for c in range(self.columns):
                if self.grid[r][c].is_mine:
                    self.grid[r][c].is_revealed = True

    def check_win(self):
        for r in range(self.rows):
            for c in range(self.columns):
                if not self.grid[r][c].is_mine and not self.grid[r][c].is_revealed:
                    return False
        return True

    def reset_board(self):
        self.grid = [[Cell() for _ in range(self.columns)] for _ in range(self.rows)]
        self._setup_board()