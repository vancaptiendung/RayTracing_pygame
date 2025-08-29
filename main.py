import map
import const

import pygame

screen = pygame.display.set_mode((const.HIGHTSCREEN, const.WIDTHSCREEN))

while True:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            pygame.quit()
            exit(0)

    screen.fill("GRAY")
    pygame.display.update()


