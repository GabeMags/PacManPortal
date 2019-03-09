import pygame.font

class StartScreen():

    def __init__(self, ai_settings, screen):
        self.ai_settings = ai_settings
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.game_title = "Pa   Man Portal"
        self.creator_name = "Gabriel Magallanes"

        # Set the properties of the start screen, game title, and creator credits
        self.title_width, self.title_height = 200, 100
        self.creator_width, self.creator_height = 100, 100
        self.title_font = pygame.font.SysFont('Snap ITC', 47)
        self.start_screen_color = (0, 0, 0)
        self.text_color = (255, 255, 255)

        self.creator_credit_text_color = (131, 132, 135)
        self.creator_font = pygame.font.SysFont('Courier New', 14)

        # Build the game title's rect object and center it at the top of the start screen
        self.title_rect = pygame.Rect(0, 0, self.title_width, self.title_height)
        self.title_rect.centerx = self.screen_rect.centerx
        self.title_rect.centery = 100
        
        # Build the title pac man SPRITE
        #Title "C" Pacman
        self.title_pacman_image = pygame.image.load("images/pacmanR_2_70px.png")
        self.title_pacman_image_rect = self.title_pacman_image.get_rect()
        self.title_pacman_image_rect.centerx = 230
        self.title_pacman_image_rect.centery = 105

        # Simple credit text
        self.creator_credit_rect = pygame.Rect(0,0, self.creator_width, self.creator_height)
        self.creator_credit_rect.centerx = self.screen_rect.centerx
        self.creator_credit_rect.centery = 680
        
        # The game titles need to be prepped only once.
        self.prep_game_title()
        
    def prep_game_title(self):

        # Title of the game
        self.title_image = self.title_font.render(self.game_title, True, self.text_color, None)
        self.title_image_rect = self.title_image.get_rect()
        self.title_image_rect.center = self.title_rect.center
        
        # Creator credit image
        self.creator_credit_image = self.creator_font.render(self.creator_name, False, self.creator_credit_text_color, None)
        self.creator_credit_image_rect = self.creator_credit_image.get_rect()
        self.creator_credit_image_rect.center = self.creator_credit_rect.center
        
    def draw_start_screen(self):
        self.screen.fill(self.start_screen_color, self.screen_rect)
        self.screen.blit(self.title_image, self.title_image_rect)
        self.screen.blit(self.creator_credit_image, self.creator_credit_image_rect)
        self.screen.blit(self.title_pacman_image, self.title_pacman_image_rect)