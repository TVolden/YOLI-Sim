import pygame
import os

class Tile(pygame.sprite.Sprite):

    def __init__(self, image_file, width, height):
        pygame.sprite.Sprite.__init__(self)

        if (image_file is not None and os.path.exists(image_file)):
            self.image = pygame.image.load(image_file).convert()
            self.image = pygame.transform.scale(self.image, (int(width), int(height)))
        else:
            self.image = pygame.Surface((width, height))
            self.image.fill((255, 0, 0))
            font = pygame.font.Font('freesansbold.ttf', 32)
            text = font.render("?", True, (0,0,0))
            textRect = text.get_rect()
            textRect.center = (width//2, height//2)
            self.image.blit(text, textRect)
        
        self.rect = self.image.get_rect()