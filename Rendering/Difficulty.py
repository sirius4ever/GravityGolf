# Rendering of the difficulty selection screen

import pygame

backgounds = [
    pygame.image.load("Assets/textures/backrounds/backround0.png"),
    pygame.image.load("Assets/textures/backrounds/backround1.png"),
    pygame.image.load("Assets/textures/backrounds/backround2.png"),
    pygame.image.load("Assets/textures/backrounds/backround3.png"),
]

time = 0
IMAGE_TIME = 2000
BLINK_TIME = 600

hovered_button = None

show_help = False


def renderDifficultySelect(screen ,dt, render, manager):

    global hovered_button
    global show_help

    #Render Background
    global time
    time = time + dt

    #Make the background change every 2 seconds
    num_background = (time//IMAGE_TIME) % len(backgounds)
    backround = backgounds[num_background]
    backround = pygame.transform.scale(backround, screen.get_size())
    screen.blit(backround, (0, 0))

    #Render Page Title
    title = pygame.image.load("Assets/textures/Buttons/difficultyselect.png")
    title = pygame.transform.scale(title, (int(title.get_width()*1), int(title.get_height()*1)))
    titleRect = title.get_rect()
    titleRect.center = (screen.get_width()//2, screen.get_height()//2-250)
    screen.blit(title, titleRect)

    #Questionmark top right
    help_rect = None
    if not show_help:
        questionmark = pygame.image.load("Assets/textures/Buttons/fragezeichen.png")
        questionmark = pygame.transform.scale(questionmark, (int(questionmark.get_width()*0.5), int(questionmark.get_height()*0.5)))
        help_rect = questionmark.get_rect()
        help_rect.topright = (screen.get_width()-10, 10) #position the questionmark in the top right corner
        screen.blit(questionmark, help_rect)

    #Render help text when hovering over the questionmark
    else:
        help = pygame.image.load("Assets/textures/help.png")
        help = pygame.transform.scale(help, (int(help.get_width()*1), int(help.get_height()*1)))
        help_rect = help.get_rect()
        help_rect.topright = (screen.get_width()-10, 10)
        screen.blit(help, help_rect)

    #Render difficulty buttons with different sizes when hovered
    easy_scale = 0.7
    if hovered_button == 'easy':
        easy_scale = 0.8
    medium_scale = 0.7
    if hovered_button == 'medium':
        medium_scale = 0.8
    hard_scale = 0.7
    if hovered_button == 'hard':
        hard_scale = 0.8

    #Load the textures for the buttons
    easy = pygame.image.load("Assets/textures/Buttons/easyborder.png")
    easy = pygame.transform.scale(easy, (int(easy.get_width()*easy_scale), int(easy.get_height()*easy_scale)))
    medium = pygame.image.load("Assets/textures/Buttons/mediumborder.png")
    medium = pygame.transform.scale(medium, (int(medium.get_width()*medium_scale), int(medium.get_height()*medium_scale)))
    hard = pygame.image.load("Assets/textures/Buttons/hardborder.png")
    hard = pygame.transform.scale(hard, (int(hard.get_width()*hard_scale), int(hard.get_height()*hard_scale)))

    #make three difficulty buttons
    easyRect = easy.get_rect()
    easyRect.center = (screen.get_width()//2, screen.get_height()//2-50)
    screen.blit(easy, easyRect)
    
    mediumRect = medium.get_rect()
    mediumRect.center = (screen.get_width()//2, screen.get_height()//2 + 100)
    screen.blit(medium, mediumRect)
   
    hardRect = hard.get_rect()
    hardRect.center = (screen.get_width()//2, screen.get_height()//2+250)
    screen.blit(hard, hardRect)


    show_help = False

    click = pygame.mixer.Sound("Assets/Sound/Click.mp3")

    # Check if the mouse is hovering over the buttons or if it is clicked
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if easyRect.collidepoint(mouse_x, mouse_y):
        if hovered_button != 'easy':
            click.play()  
            hovered_button = 'easy'
        if render.isMouseClickedOnce():
            manager.set_difficulty(0)
            render.showGame()
    elif mediumRect.collidepoint(mouse_x, mouse_y):
        if hovered_button != 'medium':
            click.play() 
            hovered_button = 'medium'
        if render.isMouseClickedOnce():
            manager.set_difficulty(1)
            render.showGame()
    elif hardRect.collidepoint(mouse_x, mouse_y):
        if hovered_button != 'hard':
            click.play()
            hovered_button = 'hard'
        if render.isMouseClickedOnce():
            manager.set_difficulty(2)
            render.showGame()
    elif help_rect.collidepoint(mouse_x, mouse_y):
        if hovered_button != 'help':
            click.play()
            hovered_button = 'help'
        show_help = True
    else:
        hovered_button = None
