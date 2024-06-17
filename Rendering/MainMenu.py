# Renders the main menu of the game

import pygame

# Define the backrounds
backgounds = [
    pygame.image.load("Assets/textures/backrounds/backround0.png"),
    pygame.image.load("Assets/textures/backrounds/backround1.png"),
    pygame.image.load("Assets/textures/backrounds/backround2.png"),
    pygame.image.load("Assets/textures/backrounds/backround3.png"),
]

time = 0
IMAGE_TIME = 2000
BLINK_TIME = 600

def renderMainMenu(screen, dt, render):
    #Render Background
    global time
    time = time + dt

    #Change the background every 2 seconds
    num_background = (time//IMAGE_TIME) % len(backgounds) 
    backround = backgounds[num_background] 
    backround = pygame.transform.scale(backround, screen.get_size())
    screen.blit(backround, (0, 0))

    #Render Game Title
    title = pygame.image.load("Assets/textures/titles/title3.png")
    title = pygame.transform.scale(title, (int(screen.get_width()*0.7), int(screen.get_height()*0.2)))
    titleRect = title.get_rect()
    titleRect.center = (screen.get_width()//2, screen.get_height()//2-100)
    screen.blit(title, titleRect)

    #Render Space to Start
    spacetostart = pygame.image.load("Assets/textures/Buttons/spacetostart.png")
    spacetostart = pygame.transform.scale(spacetostart, (int(screen.get_width()*0.4), int(screen.get_height()*0.1)))
 
    interval = time % (2*BLINK_TIME) #Blink the text every 0.6 seconds
    if interval > BLINK_TIME:
        spacetostart.set_alpha(0) #Blinking effect by setting the opacity to 0 and back to 255
    else:
        spacetostart.set_alpha(255) 
    spacetostartRect = spacetostart.get_rect() 
    spacetostartRect.center = (screen.get_width()//2,screen.get_height() - 100)
    screen.blit(spacetostart, spacetostartRect)
  
    #Check if the space key is pressed to show the difficulty select screen
    keys = pygame.key.get_pressed() 
    if keys[pygame.K_SPACE]:
        render.showDifficultySelect()

