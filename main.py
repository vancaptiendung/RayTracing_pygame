import map
import const

import time
import pygame
import math

screen = pygame.display.set_mode((const.HIGHTSCREEN, const.WIDTHSCREEN))

player = pygame.image.load("image/steve_head.png")
player_coord = player.get_rect(center = (const.HIGHTSCREEN/2, const.WIDTHSCREEN/2))

wall = pygame.image.load("image/brick.png")

shadow = pygame.image.load("image/shadow.png")
shadow_coord = shadow.get_rect(center = (const.HIGHTSCREEN/2, const.WIDTHSCREEN/2))

time_present = time.time()

while True:

    move_speed_ontime = const.SPEED * (time.time() - time_present)*100
    time_present = time.time()

    backupMove = const.PLAYER_POS.copy()
    
    event = pygame.key.get_pressed()
    is_move_x = False
    is_move_y = False
    if event[pygame.K_w]:
        const.PLAYER_POS[1] -= move_speed_ontime
        is_move_y = True
    elif event[pygame.K_s]:
        const.PLAYER_POS[1] += move_speed_ontime
        is_move_y = True
    if event[pygame.K_a]:
        const.PLAYER_POS[0] -= move_speed_ontime
        is_move_x = True
    elif event[pygame.K_d]:
        const.PLAYER_POS[0] += move_speed_ontime
        is_move_x = True
    if is_move_x and is_move_y:
        move_speed_ontime /= math.sqrt(2)

    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            pygame.quit()
            exit(0)

    screen.fill("GRAY")

    #wall
    for block in map.WALL:
        block_coord = (block[0] * const.WIDHTBLOCK, block[1] * const.HIGHTBLOCK)

        if -75 < const.PLAYER_POS[0] - block_coord[0] < 75 and -75 < const.PLAYER_POS[1] - block_coord[1] < 75:
            const.PLAYER_POS = backupMove.copy()

        wall_coord = (block_coord[0] - const.PLAYER_POS[0] + const.HIGHTSCREEN/2,
                      block_coord[1] - const.PLAYER_POS[1] + const.WIDTHSCREEN/2)
        wall_screen_coord = wall.get_rect(center = (wall_coord))
        screen.blit(wall, wall_screen_coord)
    #player
    screen.blit(player, player_coord)
    #shadow
    screen.blit(shadow, shadow_coord)

    pygame.display.update()
    


