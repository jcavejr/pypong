##Jeffrey Cave Pong Beta Update 1.0.0
#Import libraries
import pygame
import sys
from pygame.locals import *

#Initialize pygame window
pygame.init()
WHITE = (255, 255, 255)

#Set the screen size
screenHeight = 600
screenWidth = 800
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Pong")

#Load images for player1, player2, ball, and background
player1 = pygame.image.load('paddle.bmp').convert()
player2 = pygame.image.load('paddle.bmp').convert()
ball = pygame.image.load('ball.bmp').convert()
background = pygame.image.load('background.bmp').convert()

#Put scoreboard on the screen
player1Score = 0
player2Score = 0
if pygame.font:
    font = pygame.font.Font(None, 36)
    text = font.render(str(player1Score)+" "+str(player2Score), 1, WHITE)
    textpos = text.get_rect(centerx=screen.get_width()/2)
    screen.blit(text, textpos)

#Add background to the screen
screen.blit(background, (0, 0))

#Set position of player1 and add player1 to screen. Also set speed. Also set
#variables for player1.get_rect()
player1Position = player1.get_rect().move(0 , 280)
screen.blit(player1, player1Position)
player1Speed = 6
player1Xpos, player1Ypos, player1Width, player1Height = player1.get_rect()
player1Xpos = 0
player1Ypos = 280

#Set position of player2 and add player2 to screen. Also set speed. Also set
#variables for player1.get_rect(). Also set variable player2Xpos to 790 since
#get_rect() failed to do it properly
player2Position = player2.get_rect().move(790, 280)
screen.blit(player2, player2Position)
player2Speed = 6
player2Xpos, player2Ypos, player2Width, player2Height = player2.get_rect()
player2Xpos = 790
player2Ypos = 280

#Set position of ball and add ball to screen. Also add speed of ball. Also set
#variables for ball.get_rect(). Also create ballY2pos variable, which is bottom
#right corner of the ball.
ballPosition = ball.get_rect().move(396, 296)
screen.blit(ball, ballPosition)

ballXSpeed = 4
ballYSpeed = 4
ballXpos, ballYpos, ballWidth, ballHeight = ball.get_rect()
ballXpos = 400
ballYpos = 300
ballY2pos = ballYpos + ballHeight

def resetBall(xpos, ypos):
    global ballPosition
    global ballXpos
    global ballYpos
    ballPosition = ballPosition.move((-1*(xpos - 400)), (-1 *(ypos - 300)))
    ballXpos = 400
    ballYpos = 300

def resetPlayers(ypos1, ypos2):
    global player1Position
    global player1Ypos
    global player2Position
    global player2Ypos
    player1Position = player1Position.move(0, (-1*(ypos1-280)))
    player2Position = player2Position.move(0, (-1*(ypos2-280)))
    player1Ypos = 280
    player2Ypos = 280

def changeSpeed(inc):
    return (inc*2), (inc*2), inc, inc
#Initialize the scores
player1Score = 0
player2Score = 0
#Create a clock to maintain a steady framrate
clock = pygame.time.Clock()

#Update the screen with all of the components.
pygame.display.update()

while 1:
    #Use the clock to keep 60fps
    clock.tick(60)
    #Check which keys are being pressed and move the players accordingly. Also
    #update playerPos variables with each key press
    keys  = pygame.key.get_pressed()
    #if keys[pygame.K_1]:
    #    player1Speed, player2Speed, ballXSpeed, ballYSpeed = changeSpeed(1)
    #if keys[pygame.K_2]:
    #    player1Speed, player2Speed, ballXSpeed, ballYSpeed = changeSpeed(2)
    #if keys[pygame.K_3]:
    #    player1Speed, player2Speed, ballXSpeed, ballYSpeed = changeSpeed(3)
    #if keys[pygame.K_4]:
    #    player1Speed, player2Speed, ballXSpeed, ballYSpeed = changeSpeed(4)
    #if keys[pygame.K_5]:
    #    player1Speed, player2Speed, ballXSpeed, ballYSpeed = changeSpeed(5)
    #if keys[pygame.K_6]:
    #    player1Speed, player2Speed, ballXSpeed, ballYSpeed = changeSpeed(6)
    #if keys[pygame.K_7]:
    #    player1Speed, player2Speed, ballXSpeed, ballYSpeed = changeSpeed(7)
    #if keys[pygame.K_8]:
    #    player1Speed, player2Speed, ballXSpeed, ballYSpeed = changeSpeed(8)
    #if keys[pygame.K_9]:
    #    player1Speed, player2Speed, ballXSpeed, ballYSpeed = changeSpeed(9)
    #if keys[pygame.K_0]:
    #    player1Speed, player2Speed, ballXSpeed, ballYSpeed = changeSpeed(10)
    #Update ball position variables with each frame
    ballYpos = ballYpos + ballYSpeed
    ballXpos = ballXpos + ballXSpeed
    ballY2pos = ballYpos + ballHeight
    if keys[pygame.K_UP]:
        player2Position = player2Position.move(0, -player2Speed)
        player2Ypos = player2Ypos - player2Speed
    if keys[pygame.K_DOWN]:
        player2Position = player2Position.move(0, player2Speed)
        player2Ypos = player2Ypos + player2Speed
    if keys[pygame.K_w]:
        player1Position = player1Position.move(0, -player1Speed)
        player1Ypos = player1Ypos - player1Speed
    if keys[pygame.K_s]:
        player1Position = player1Position.move(0, player1Speed)
        player1Ypos = player1Ypos + player1Speed
    #Loop that checks when user closes the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #Math that checks if the ball collides with player1. If it does, it makes
    #the ball bounce
    if ((player1Xpos + player1Width) > ballXpos) and ((player1Ypos < ballY2pos \
        <(player1Ypos + player1Height)) or (player1Ypos < (ballY2pos - ballHeight) \
        < (player1Ypos + player1Height ))):
        ballXSpeed = ballXSpeed * -1
    #Math that checks if the ball collides with player2. If it does, it makes
    #the ball bounce
    if (player2Xpos <= (ballXpos + ballWidth)) and (((player2Ypos < ballYpos < \
        (player2Ypos + player2Height))) or (player2Ypos < ballY2pos < \
        (player2Ypos + player2Height))):
        ballXSpeed = (ballXSpeed * -1)
    #Math that checks if the ball goes off of the top or bottom of the screen.
    #If it does, it makes the ball bounce
    if ballY2pos >= screenHeight or ballYpos < 0:
        ballYSpeed = (ballYSpeed * -1)
    #Check if player2 scored
    if ballXpos < (player1Xpos + player1Width) and not ((player1Ypos < ballY2pos \
        <(player1Ypos + player1Height)) or (player1Ypos < (ballY2pos - ballHeight) \
        < (player1Ypos + player1Height ))):
        player2Score = player2Score + 1
        newBallXpos = ballXpos
        newBallYpos = ballYpos
        resetBall(newBallXpos, newBallYpos)
        resetPlayers(player1Ypos, player2Ypos)
    #Check if player1 scored
    if (ballXpos + ballWidth) > player2Xpos and not (((player2Ypos < ballYpos < \
        (player2Ypos + player2Height))) or (player2Ypos < ballY2pos < \
        (player2Ypos + player2Height))):
        player1Score = player1Score + 1
        newBallXpos = ballXpos
        newBallYpos = ballYpos
        resetBall(newBallXpos, newBallYpos)
        resetPlayers(player1Ypos, player2Ypos)
    #Update the position of the ball
    ballPosition = ballPosition.move(ballXSpeed, ballYSpeed)
    #Paste all images on the screen in their new positions
    screen.blit(background, (0, 0))
    screen.blit(ball, ballPosition)
    screen.blit(player1, player1Position)
    screen.blit(player2, player2Position)
    text = font.render(str(player1Score)+" "+str(player2Score), 1, WHITE)
    textpos = text.get_rect(centerx=screen.get_width()/2)
    screen.blit(text, textpos)
    pygame.display.update()
