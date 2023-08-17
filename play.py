from yoli_sim.play_yoli import PlayYoli, MatchTwo
import pygame

# Games must inherit YoliTileGame
sim = PlayYoli(game=MatchTwo())
print("This is a very limited sample game to show the YOLI Board simulator.")
print("The goal is to match two tiles with he same label.")

clock = pygame.time.Clock()
tile_selected = None
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN and \
            pygame.mouse.get_pressed()[0]:
            (x,y) = pygame.mouse.get_pos()
            sim.select_tile(x,y)

        elif event.type == pygame.MOUSEBUTTONUP and \
            not pygame.mouse.get_pressed()[0]:
            (x,y) = pygame.mouse.get_pos()
            sim.place_tile(x,y)
            if sim.notification == 1:
                print("Goal reached!")

    if sim.selected is not None:
        sim.move_selected_tile(pygame.mouse.get_pos())

    sim.render()
    clock.tick(60)  # limits FPS to 60

sim.close()