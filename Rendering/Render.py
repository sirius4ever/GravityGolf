# Main rendering Code accessing all other rendering files and managing the screen state
import pygame
from Rendering.MainMenu import renderMainMenu
from Rendering.Difficulty import renderDifficultySelect #Importing all Screens into the main Render file
from Rendering.Victory import renderVictory
from Rendering.gameRenderer import renderGame

from Game.GameManager import GameManager 


class Render: 
    def __init__(self, width, height):
        self.screenState = 0
        self.manager = GameManager(width, height)
        self.isMouseClicked = pygame.mouse.get_pressed()[0]  # Check if the mouse is clicked

    def render(self, screen, dt): #Renders the current screen based on the screen state.
    
        if self.screenState == 0:  # Main Menu
            renderMainMenu(screen, dt, self)
        elif self.screenState == 1:  # Difficulty Select
            renderDifficultySelect(screen, dt, self, self.manager)
        elif self.screenState == 2:  # Game
            self.manager.update(dt)  # Update the game state
            renderGame(screen, dt, self, self.manager)
        elif self.screenState == 3:  # Victory
            renderVictory(screen, dt, self)

    def showMainMenu(self): #Switches the screen state to Main Menu
        self.screenState = 0

    def showDifficultySelect(self): #Switches the screen state to Difficulty Select
        self.screenState = 1

    def showGame(self): #Switches the screen state to Game
        self.manager.start()  # Start the game
        self.screenState = 2

    def showVictory(self): #Switches the screen state to Victory
        self.screenState = 3

    def isMouseClickedOnce(self):
        old_state = self.isMouseClicked
        if pygame.mouse.get_pressed()[0]:
            self.isMouseClicked = True
        else:
            self.isMouseClicked = False
        return not old_state and self.isMouseClicked
        