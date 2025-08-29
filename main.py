import map
import const

import pygame

screen = pygame.display.set_mode((const.HIGHTSCREEN, const.WIDTHSCREEN))

player = pygame.image.load("image/steve_head.png")
player_coord = player.get_rect(center = (const.HIGHTSCREEN/2, const.WIDTHSCREEN/2))

wall = pygame.image.load("image/brick.png")

while True:
    event = pygame.key.get_pressed()
    if event[pygame.K_w]:
        const.PLAYER_POS[1] -= const.SPEED
    if event[pygame.K_s]:
        const.PLAYER_POS[1] += const.SPEED
    if event[pygame.K_a]:
        const.PLAYER_POS[0] -= const.SPEED
    if event[pygame.K_d]:
        const.PLAYER_POS[0] += const.SPEED

    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            pygame.quit()
            exit(0)

    screen.fill("GRAY")

    #wall
    for block in map.WALL:
        block_coord = (block[0] * const.WIDHTBLOCK, block[1] * const.HIGHTBLOCK)
        wall_coord = (block_coord[0] - const.PLAYER_POS[0] + const.HIGHTSCREEN/2,
                      block_coord[1] - const.PLAYER_POS[1] + const.WIDTHSCREEN/2)
        wall_screen_coord = wall.get_rect(center = (wall_coord))
        screen.blit(wall, wall_screen_coord)
    #player
    screen.blit(player, player_coord)
    #shadow

    pygame.display.update()


