import pygame
import os

pygame.init()

SCR_WIDTH = 800
SCR_HEIGHT = 600
GRID_ROWS = 8
GRID_COLS = 8
MINE_COUNT = 12
TILE_COUNT = GRID_ROWS * GRID_COLS
TILE_SIZE = 32
FPS = 60
TITLE = "Minesweeper"

# Image assets
tile_numbers = []
for i in range(1, 9):
    path = os.path.join("ui", "assets", f"Tile{i}.png")
    tile_numbers.append(pygame.transform.scale(pygame.image.load(path), (TILE_SIZE, TILE_SIZE)))

tile_empty = pygame.transform.scale(pygame.image.load(os.path.join("ui", "assets", "TileEmpty.png")), (TILE_SIZE, TILE_SIZE))
tile_exploded = pygame.transform.scale(pygame.image.load(os.path.join("ui", "assets", "TileExploded.png")), (TILE_SIZE, TILE_SIZE))
tile_flag = pygame.transform.scale(pygame.image.load(os.path.join("ui", "assets", "TileFlag.png")), (TILE_SIZE, TILE_SIZE))
tile_mine = pygame.transform.scale(pygame.image.load(os.path.join("ui", "assets", "TileMine.png")), (TILE_SIZE, TILE_SIZE))
tile_unknown = pygame.transform.scale(pygame.image.load(os.path.join("ui", "assets", "TileUnknown.png")), (TILE_SIZE, TILE_SIZE))
tile_not_mine = pygame.transform.scale(pygame.image.load(os.path.join("ui", "assets", "TileNotMine.png")), (TILE_SIZE, TILE_SIZE))