import pygame
import os

class Tile(pygame.sprite.Sprite):

    def __init__(self, image_file, width = 100, height = 100):
        pygame.sprite.Sprite.__init__(self)
        self._org_image = None

        if (image_file is not None and os.path.exists(image_file)):
            self._org_image = pygame.image.load(image_file).convert()
        
        self.scale(width, height)
        self.rect = self.image.get_rect()
    
    def _render_placeholder(self, width, height):
        image = pygame.Surface((width, height))
        image.fill((255, 0, 0))
        pygame.font.init()
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("?", True, (0,0,0))
        textRect = text.get_rect()
        textRect.center = (width//2, height//2)
        image.blit(text, textRect)
        return image

    def scale(self, width, height):
        if self._org_image is not None:
            self.image = pygame.transform.scale(self._org_image, (int(width), int(height)))
        else:
            self.image = self._render_placeholder(width, height)

    def transform(self, x, y):
        self.rect.x = x
        self.rect.y = y