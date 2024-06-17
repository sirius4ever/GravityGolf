import pygame
from Rendering.Render import Render  

# Define frames per second
FPS = 60

def main(): 
    pygame.init()  # Initialize the Game
    screen = pygame.display.set_mode((1920*0.7, 0.7*1080))  # Set the screen size
    pygame.display.set_caption('Gravity Golf') # Set the title of the window

    running = True 
    clock = pygame.time.Clock() 
    dt = 0 
    renderer = Render(screen.get_width(), screen.get_height())  
    
    pygame.mixer.init()
    pygame.mixer.music.load("Assets/Sound/BackgroundMusic.mp3")  # Load the background music
    pygame.mixer.music.play(-1)  # Play the background music in an infinite loop
    pygame.mixer.music.set_volume(0.08) 

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If the close button is clicked
                running = False  # Exit the loop and end the game
        
        screen.fill((0, 0, 0))  
        renderer.render(screen, dt)  # Render the game objects on the screen

        pygame.display.flip()  # Update the display
        dt = clock.tick(FPS)  
    pygame.quit()  

if __name__ == '__main__':
    main() 
