# Victory Screen Rendering file

import pygame

pygame.mixer.init()

hover_difficulty = False #Check if the mouse is hovering over the two buttons
hover_next = False
time = 0
last_hovered_button = None #Check if the last hovered button was the same as the current one


def renderVictory(screen, dt, render): 

    # Importing the global variables
    global hover_difficulty
    global hover_next
    global last_hovered_button

    # Render Background
    background = pygame.image.load("Assets/textures/backrounds/backround0.png")
    background = pygame.transform.scale(background, screen.get_size())
    screen.blit(background, (0, 0))

    # Render Page Title
    title = pygame.image.load("Assets/textures/titles/victory.png")
    title = pygame.transform.scale(title, (int(title.get_width()*1.3), int(title.get_height()*1.3)))
    title_rect = title.get_rect()
    title_rect.center = (screen.get_width() // 2, screen.get_height() // 2 - 180)
    screen.blit(title, title_rect)

    # Define button scales
    difficulty_scale = 0.7 if not hover_difficulty else 0.8
    next_scale = 0.7 if not hover_next else 0.8

    # Render buttons "Difficulty Select" and "Next" below each other
    difficulty_button = pygame.image.load("Assets/textures/Buttons/difficultyselectborder.png")
    difficulty_button = pygame.transform.scale(difficulty_button, (int(difficulty_button.get_width()*difficulty_scale), int(difficulty_button.get_height()*difficulty_scale)))
    difficulty_rect = difficulty_button.get_rect()
    difficulty_rect.center = (screen.get_width() // 2, screen.get_height() // 2 + 150)
    screen.blit(difficulty_button, difficulty_rect)

    next_button = pygame.image.load("Assets/textures/Buttons/Again.png")
    next_button = pygame.transform.scale(next_button, (int(next_button.get_width()*next_scale), int(next_button.get_height()*next_scale)))
    next_rect = next_button.get_rect()
    next_rect.center = (screen.get_width() // 2, screen.get_height() // 2)
    screen.blit(next_button, next_rect)
    
    
    click = pygame.mixer.Sound("Assets/Sound/Click.mp3")

    hover_difficulty = hover_next = False
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Check if the mouse is hovering over the buttons
    if difficulty_rect.collidepoint(mouse_x, mouse_y): #adding a time delay to avoid the mouse click from the victory screen to affect the difficulty select 
        if last_hovered_button != 'difficulty':
            click.play()  # Play the hover sound
            last_hovered_button = 'difficulty'
        hover_difficulty = True
        if render.isMouseClickedOnce(): #get pressed is a list of all the mouse buttons, 0 is the left mouse button
            render.showDifficultySelect()
    elif next_rect.collidepoint(mouse_x, mouse_y):
        if last_hovered_button != 'next':
            click.play()  # Play the hover sound
            last_hovered_button = 'next'
        hover_next = True
        if render.isMouseClickedOnce():
            render.showGame()
    else:
        last_hovered_button = None
