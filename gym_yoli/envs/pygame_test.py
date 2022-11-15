import pygame
from pygame.locals import *
import math

size = 5
tiles = 30

window_size = 500

pygame.init()
pygame.display.init()
window = pygame.display.set_mode((window_size, window_size))
clock = pygame.time.Clock()
board_canvas = pygame.Surface((window_size, window_size))
board_canvas.fill((255, 255, 255))
pygame.display.set_caption("Tile Board")

board_pix_square_size = (
    window_size / size
)  # The size of a single board grid square in pixels

tile_squares = math.floor(math.sqrt(tiles) + 1)
tile_pix_square_size = (
    (window_size - board_pix_square_size)  / tile_squares
)  # The size of a single tile grid square in pixels

margin = 10
# Draw board
for x in range(size + 1):
    rect = (
        x * board_pix_square_size + margin/2,
        margin/2,
        board_pix_square_size - margin, 
        board_pix_square_size - margin
     )
    pygame.draw.rect(
        board_canvas,
        (0, 0, 0),
        rect,
        1
    )

for x in range(tiles):
    col = x % tile_squares
    row = math.floor(x / tile_squares)
    rect = (
        col * tile_pix_square_size + board_pix_square_size/2,
        row * tile_pix_square_size + board_pix_square_size + margin/2,
        tile_pix_square_size - margin, 
        tile_pix_square_size - margin
     )
    pygame.draw.rect(
        board_canvas,
        (0, 0, 0),
        rect,
        1
    )

while True:
    window.blit(board_canvas, board_canvas.get_rect())
    pygame.event.pump()
    pygame.display.update()
    clock.tick(30)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()