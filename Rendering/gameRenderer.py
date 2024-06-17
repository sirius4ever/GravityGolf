# Renders the game screen

import pygame
from Game.GameManager import BALL_RADIUS,HOLE_RADIUS
import math

time = 0

def resetTime():
    global time
    time = 0

def renderGame(screen, dt, MainRenderer, manager):
    global time
    time = time + dt

    #Render background
    backround = pygame.image.load("Assets/textures/backrounds/backround0.png")
    backround = pygame.transform.scale(backround, screen.get_size())
    screen.blit(backround, (0, 0))


    #Render ball
    ball_x, ball_y = manager.ball_position
    pygame.draw.circle(screen, (255, 255, 255), (int(ball_x), int(ball_y)), BALL_RADIUS)
    
    #render hole
    hole_x, hole_y = manager.hole_position
    blackhole = pygame.image.load("Assets/textures/planets/blackhole.png")
    blackhole = pygame.transform.scale(blackhole, (HOLE_RADIUS*2, HOLE_RADIUS*2))
    screen.blit(blackhole, (hole_x - HOLE_RADIUS, hole_y - HOLE_RADIUS)) #Render the black hole in the middle of the screen

    #Render planets getting the position and radius of the planets from the Planet class
    for p in manager.planets:
        x, y = p.position
        radius = p.radius
        texture = pygame.image.load(p.texture)
        texture = pygame.transform.scale(texture, (int(radius*2), int(radius*2)))
        screen.blit(texture, (x - radius, y - radius))

    shoot = pygame.mixer.Sound("Assets/Sound/walls.mp3")
    shoot.set_volume(0.5)

    #Render line to mouse cursor if velocity and position is 0
    if(manager.state == 0): #If the ball is not moving
        pygame.draw.line(screen, (255, 255, 255, 128), (ball_x, ball_y), pygame.mouse.get_pos())

        #if mouse is pressed set velocity of the ball to the direction of the mouse
        if MainRenderer.isMouseClickedOnce():
            shoot.play()
            mouse_x, mouse_y = pygame.mouse.get_pos()
            velocity_x = mouse_x - ball_x
            velocity_y = mouse_y - ball_y
            max_velocity = 100
            velocity = math.sqrt(velocity_x**2 + velocity_y**2) 
            if(velocity > max_velocity):
                velocity_x = velocity_x * max_velocity / velocity #Limit the velocity to 100
                velocity_y = velocity_y * max_velocity / velocity 
            manager.set_velocity((velocity_x/150, velocity_y/150)) #Divide by 150 to slow down the ball
        
    if(manager.state == 2): #If the ball is in the hole
        MainRenderer.showVictory()
    elif(manager.state == 3): #If the ball hits the planet
        MainRenderer.showGame()

    #Check if escape is pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        MainRenderer.showDifficultySelect()
