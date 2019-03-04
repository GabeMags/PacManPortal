import sys
import pygame
from buttons import Button
from pacman import PacMan


def update_screen(ai_settings, screen, play_button, hs_button, stats, start_screen, pacman):
    """Update the images on the screen and flup to the new screen"""
    screen.fill(ai_settings.bg_color)

    pacman.blitme()

    # If the game hasn't started yet, run the start screen
    if not stats.game_active:
        start_screen.draw_start_screen()
        play_button.draw_play_button()
        hs_button.draw_hs_button()

    pygame.display.flip()

def check_keydown_events(event, ai_settings, screen, pacman):
    # Respond to keypresses
    if event.key == pygame.K_RIGHT:
        pacman.moving_right = True
    elif event.key == pygame.K_LEFT:
        pacman.moving_left = True
    elif event.key == pygame.K_UP:
        pacman.moving_up = True
    elif event.key == pygame.K_DOWN:
        pacman.moving_down = True

    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, pacman):
    # Respond to key releases
    if event.key == pygame.K_RIGHT:
        pacman.moving_right = False
    if event.key == pygame.K_LEFT:
        pacman.moving_left = False
    if event.key == pygame.K_UP:
        pacman.moving_up = False
    if event.key == pygame.K_DOWN:
        pacman.moving_down = False

def check_events(ai_settings, screen, stats, play_button, hs_button, pacman):
    """Respond to keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, pacman)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, pacman)

        # Check to see where the mouse is being clicked (start button, high scores button)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_both_buttons(ai_settings, screen, stats, mouse_x, mouse_y, play_button, hs_button)

def check_both_buttons(ai_settings, screen, stats, mouse_x, mouse_y, play_button, hs_button):
    """Start a new game when the player clicks play, show high scores when the player selects high scores"""
    play_button_clicked = play_button.rect_play.collidepoint(mouse_x, mouse_y)
    hs_button_clicked = hs_button.rect_hs.collidepoint(mouse_x, mouse_y)

    if play_button_clicked and not stats.game_active:
        stats.game_active = True

    elif hs_button_clicked and not stats.game_active:
        print("another success")
