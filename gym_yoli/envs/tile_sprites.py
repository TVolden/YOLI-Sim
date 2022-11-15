import pygame

class Tile(pygame.sprite.Sprite):

    def __init__(self, image_file, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(image_file).convert()
        self.image = pygame.transform.scale(self.image, (width, height))

        self.rect = self.image.get_rect()