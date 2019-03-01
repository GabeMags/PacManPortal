import sys
import pygame
from buttons import Button


def update_screen(ai_settings, screen, start_screen_buttons, stats, start_screen):
    """Update the images on the screen and flup to the new screen"""
    screen.fill(ai_settings.bg_color)
    
    # If the game hasn't started yet, run the start screen
    if not stats.game_active:
        start_screen.draw_start_screen
        start_screen_buttons.draw_buttons()

    
    pygame.display.flip()
    
def check_events(ai_settings, screen):
    """Respond to keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()


            