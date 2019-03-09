import pygame

from settings import Settings
from buttons import Button
from game_stats import GameStats
from start_screen import StartScreen
from pacman import PacMan
from maze import Maze


import game_functions as gf

def run_game():
    pygame.init()
    
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    # Create the maze
    maze = Maze(screen)
    
    pygame.display.set_caption(("Pac Man Portal"))

    # Make PacMan, and the start screen pacman
    pacman = PacMan(ai_settings, screen, maze)

    # Make the start screen
    start_screen = StartScreen(ai_settings, screen)

    # Make the play button and high scores buttons
    play_button = Button(ai_settings, screen)
    hs_button = Button(ai_settings, screen)

    # Create an instance to store game statistics
    stats = GameStats()

    # Start the main loop for the game
    while True:
        gf.check_events(ai_settings, screen, stats, play_button, hs_button, pacman)
        
        if stats.game_active:
            pacman.check_wall_collision()
            pacman.update()




        gf.update_screen(ai_settings, screen, play_button, hs_button, stats, start_screen, pacman, maze)

        

run_game()