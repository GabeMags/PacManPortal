import pygame.font

class StartScreen():

    def __init__(self, ai_settings, screen):
        self.ai_settings = ai_settings
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.game_title = "Pac Man Portal"
        self.creator_name = "Gabriel Magallanes"

        # Set the properties of the start screen, game title
        self.title_width, self.title_height = 400, 100
        self.title_font = pygame.font.SysFont('Impact', 84)
        self.start_screen_color = (0, 0, 0)
        self.text_color = (255, 255, 255)

        self.creator_credit_text_color = (131, 132, 135)
        self.creator_font = pygame.font.SysFont('Courier New', 14)

        # Build the game title's rect object and center it at the top of the start screen
        self.title_rect = pygame.Rect(0, 0, self.title_width, self.title_height)
        self.title_rect.centerx = 600
        self.title_rect.centery = 80

        # Simple credit text
        self.creator_credit_rect = pygame.Rect(0,0, 100, 100)
        self.creator_credit_rect.centerx = self.screen_rect.centerx
        self.creator_credit_rect.centery = 680
        
        # The game titles need to be prepped only once.
        self.prep_game_title()
        
    def prep_game_title(self):
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