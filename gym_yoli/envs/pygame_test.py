import pygame
from pygame.locals import *
import math
from tile_sprites import Tile
import random
import os
import numpy as np

## Test data
size = 5
tiles = 30

window_size = 500

tiles_info = [{"image": f"tiles\\{x+1:02}.png"} for x in range(tiles-2)]
random.shuffle(tiles_info)
tiles_info.insert(0, {"image": ""})
positions = np.array([0] * size)
positions[2] = tiles-1#random.randint(0, tiles)

## Pygame logic

pygame.init()
pygame.display.init()


window = pygame.display.set_mode((window_size, window_size))
pygame.display.set_caption("Tile Board")
clock = pygame.time.Clock()

board_canvas = pygame.Surface((window_size, window_size))
board_canvas.fill((255, 255, 255))

board_pix_square_size = (
    window_size / size
)  # The size of a single board grid square in pixels

tile_squares = math.floor(math.sqrt(tiles) + 1)
tile_pix_square_size = (
    (window_size - board_pix_square_size)  / tile_squares
)  # The size of a single tile grid square in pixels
margin = 10

# Draw board
all_sprites_list = pygame.sprite.Group()

for x in range(size):
    rect = (
        x * board_pix_square_size + margin / 2,
        margin / 2,
        board_pix_square_size - margin, 
        board_pix_square_size - margin
     )
    pygame.draw.rect(
        board_canvas,
        (0, 0, 0),
        rect,
        1
    )
    pos = positions[x]
    if pos > 0:
        img = tiles_info[pos].get("image") if len(tiles_info) > pos else ""
        object_ = Tile(img, board_pix_square_size-margin-2, board_pix_square_size-margin-2)
        object_.rect.x = x * board_pix_square_size + margin / 2 + 1
        object_.rect.y = margin / 2 + 1
        all_sprites_list.add(object_)

for x in range(tiles):
    col = x % tile_squares
    row = math.floor(x / tile_squares)
    rect = (
        col * tile_pix_square_size + board_pix_square_size / 2,
        row * tile_pix_square_size + board_pix_square_size + margin / 2,
        tile_pix_square_size - margin, 
        tile_pix_square_size - margin
     )
    pygame.draw.rect(
        board_canvas,
        (0, 0, 0),
        rect,
        1
    )
    pos = x+1
    if pos not in positions:
        img = tiles_info[pos].get("image") if len(tiles_info) > pos else ""
        object_ = Tile(img, tile_pix_square_size-margin-2, tile_pix_square_size-margin-2)
        object_.rect.x = col * tile_pix_square_size + board_pix_square_size / 2 + 1
        object_.rect.y = row * tile_pix_square_size + board_pix_square_size + margin / 2 + 1
        all_sprites_list.add(object_)

while True:
    all_sprites_list.update()
    window.fill((255, 255, 255))
    pygame.event.pump()
    window.blit(board_canvas, board_canvas.get_rect())
    all_sprites_list.draw(window)
    pygame.display.flip()
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()