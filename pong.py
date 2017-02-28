import pygame, sys

pygame.init()

BLACK=(0,0,0)
WHITE=(255,255,255)
#GREEN=(0,255,0)
#RED=(255,0,0)
#BLUE=(0,0,255)

size = (600,400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Pong')
done = False
screen.fill(BLACK)
#Start position and speed of the rectange, draw it
rect_x = 50
rect_y = 50
rect_change_x = 5
rect_change_y = 5
pygame.draw.rect(screen, WHITE, [rect_x,rect_y,50,50])
#program loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
            sys.exit()
    #erase the screen
    screen.fill(BLACK)
    #draw the rectangle
    pygame.draw.rect(screen, WHITE, [rect_x,rect_y,50,50])
    #change the rectangle starting point
    if rect_y > size[1]-50 or rect_y < 0:
        rect_change_y = -1 * rect_change_y
    if rect_x > size[0]-50 or rect_x < 0:
        rect_change_x = -1 * rect_change_x
    rect_x += rect_change_x
    rect_y += rect_change_y
    pygame.display.flip()
