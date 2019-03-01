import pygame

from settings import Settings
from buttons import Button
from game_stats import GameStats
from start_screen import StartScreen

import game_functions as gf

def run_game():
    pygame.init()
    
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    
    pygame.display.set_caption(("Pac Man Portal"))

    # Make the start screen
    start_screen = StartScreen(ai_settings, screen)

    # Make the play button and high scores buttons
    start_screen_buttons = Button(ai_settings, screen)

    # Create an instance to store game statistics
    stats = GameStats()

    # Start the main loop for the game
    while True:
        gf.check_events(ai_settings, screen)

        gf.update_screen(ai_settings, screen, start_screen_buttons, stats, start_screen)

        

run_game()