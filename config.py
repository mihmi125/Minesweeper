import pygame
import os

SCR_WIDTH = 800
SCR_HEIGHT = 600
GRID_ROWS = 3
GRID_COLS = 3
MINE_COUNT = 8
TILE_COUNT = GRID_ROWS * GRID_COLS
TILE_SIZE = 32
FPS = 60
TITLE = "Minesweeper"

tile_numbers = []
for i in range(1, 9):
    tile_numbers.append(pygame.transform.scale(pygame.image.load(os.path.join("assets", f"Tile{i}.png")), (TILE_SIZE, TILE_SIZE)))

tile_empty = pygame.transform.scale(pygame.image.load(os.path.join("assets", "TileEmpty.png")), (TILE_SIZE, TILE_SIZE))
tile_exploded = pygame.transform.scale(pygame.image.load(os.path.join("assets", "TileExploded.png")), (TILE_SIZE, TILE_SIZE))
tile_flag = pygame.transform.scale(pygame.image.load(os.path.join("assets", "TileFlag.png")), (TILE_SIZE, TILE_SIZE))
tile_mine = pygame.transform.scale(pygame.image.load(os.path.join("assets", "TileMine.png")), (TILE_SIZE, TILE_SIZE))
tile_unknown = pygame.transform.scale(pygame.image.load(os.path.join("assets", "TileUnknown.png")), (TILE_SIZE, TILE_SIZE))
tile_not_mine = pygame.transform.scale(pygame.image.load(os.path.join("assets", "TileNotMine.png")), (TILE_SIZE, TILE_SIZE))