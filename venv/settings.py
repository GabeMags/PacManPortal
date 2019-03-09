import pygame

class Settings():

    def __init__(self):
        """Initialize the game's static settings"""
        # Screen settings
        self.screen_width = 700
        self.screen_height = 750
        self.bg_color = (0,0,0)
        
        self.pacman_speed_factor = 0.4
    
