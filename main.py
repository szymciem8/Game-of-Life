import net
import pygame
import time

screen_size = 800

fpsClock = pygame.time.Clock()
fps = 60

pygame.init()
pygame.display.set_caption("Conway's Game Of Life")
screen = pygame.display.set_mode((screen_size, screen_size))  
screen.fill(pygame.Color(255,255,255))
pygame.display.update()

board = net.Net(screen, 100)
#board.random_dots(5000)

last_x = 0
last_y = 0

object_id = 0
max_id = 4
min_id = 0

pygame.display.update()
board.logic()

#Main Loop
running = True
life = False
while running:  
    #board.game_logic()
    x, y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                board.clear_hover(object_id)
                life = not life
            elif event.key == pygame.K_w:
                board.rotate_object(object_id, "right")
            elif event.key == pygame.K_q:
                board.rotate_object(object_id, "left")

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button==1 and not life:
                board.add_cell(object_id, x, y)
            #UP SCROLL
            if event.button == 4:
                object_id += 1
                if object_id > board.MAX_ID:
                    object_id = 0
                board.clear_hover(object_id)
            #DOWN SCROLL
            if event.button == 5:
                object_id -= 1
                if object_id < 0:
                    object_id = board.MAX_ID
                board.clear_hover(object_id)
                    
    
    if life:
        pygame.display.update()
        board.logic()
        fpsClock.tick(fps)
    elif not life:
        if last_x != x or last_y != x:
            board.hover(object_id, x, y)
            last_x = x
            last_y = y
            pygame.display.update()