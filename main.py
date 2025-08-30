import map
import const

import time
import pygame
import math

screen = pygame.display.set_mode((const.HIGHTSCREEN, const.WIDTHSCREEN))

def dis_form_middle(pointCoord : list, middle):
    pow2_dis = (pointCoord[0] - middle[0]) ** 2 + (pointCoord[1] - middle[1]) ** 2
    return math.sqrt(pow2_dis)

def create_shadow(blockMidCoord : tuple):
    if dis_form_middle(blockMidCoord, const.MIDSCREEN) > const.LIGHT_DIS :
        return 0

    verticese_block = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    
    for k in range(4):
        if (k < 2):
            verblock1 = (blockMidCoord[0] + const.WIDHTBLOCK/2 * verticese_block[k][0], 
                        blockMidCoord[1] + const.HIGHTBLOCK/2 )
            verblock2 = (blockMidCoord[0] + const.WIDHTBLOCK/2 * verticese_block[k][0], 
                        blockMidCoord[1] - const.HIGHTBLOCK/2 )
        else:
            verblock1 = (blockMidCoord[0] + const.WIDHTBLOCK/2,
                        blockMidCoord[1] + const.WIDHTBLOCK/2 * verticese_block[k][1])
            verblock2 = (blockMidCoord[0] - const.WIDHTBLOCK/2,
                        blockMidCoord[1] + const.WIDHTBLOCK/2 * verticese_block[k][1])

        vector_ver1 = [verblock1[k] - const.MIDSCREEN[k] for k in range(2)]
        vector_ver2 = [verblock2[k] - const.MIDSCREEN[k] for k in range(2)]

        disvec1 = dis_form_middle(vector_ver1, [0,0])
        disvec2 = dis_form_middle(vector_ver2, [0,0])

        real_vec1 = [vector_ver1[k]/disvec1 * const.SHADOW_LONG for k in range(2)]
        real_vec2 = [vector_ver2[k]/disvec2 * const.SHADOW_LONG for k in range(2)]

        shadowPoint1 = (real_vec1[0] + const.MIDSCREEN[0], real_vec1[1] + const.MIDSCREEN[1])
        shadowPoint2 = (real_vec2[0] + const.MIDSCREEN[0], real_vec2[1] + const.MIDSCREEN[1])


        pygame.draw.polygon(screen, "BLACK", [verblock1, shadowPoint1, shadowPoint2, verblock2])



player = pygame.image.load("image/steve_head.png")
player_coord = player.get_rect(center = const.MIDSCREEN)

wall = pygame.image.load("image/brick.png")

shadow = pygame.image.load("image/shadow.png")
shadow_coord = shadow.get_rect(center = const.MIDSCREEN)

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

        wall_coord = (block_coord[0] - const.PLAYER_POS[0] + const.HIGHTSCREEN/2,
                      block_coord[1] - const.PLAYER_POS[1] + const.WIDTHSCREEN/2)
        create_shadow(wall_coord)


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
    pygame.draw.rect(screen, "BLACK", (0, 0, const.HIGHTSCREEN/2 - const.LIGHT_DIS, const.WIDTHSCREEN))
    pygame.draw.rect(screen, "BLACK", (const.HIGHTSCREEN/2 + const.LIGHT_DIS, 0, const.HIGHTSCREEN/2 - const.LIGHT_DIS, const.WIDTHSCREEN)) 
    pygame.display.update()
    


