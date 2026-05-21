class Cell:
    def __init__(self):
        self.is_mine = False
        self.is_revealed = False
        self.is_flagged = False
        self.neighbor_mines = 0

    def __str__(self):
        if self.is_mine: return "M"
        return str(self.neighbor_mines)