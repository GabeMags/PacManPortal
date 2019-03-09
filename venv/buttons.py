import pygame.font

class Button():
    """This class is for the start screen buttons"""
    def __init__(self, ai_settings, screen):
        """Initialize button attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Set the dimensions and properties of the button
        self.width, self.height = 200, 50
        self.button_color = (0, 0, 0)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None, 48)

        # Build the play and high score buttons' rect objects
        self.rect_play = pygame.Rect(0,0, self.width, self.height)
        self.rect_hs = pygame.Rect(0,0, self.width, self.height)

        # Play button location
        self.rect_play.centerx = self.screen_rect.centerx
        self.rect_play.centery = 545

        # High score button location
        self.rect_hs.centerx = self.screen_rect.centerx
        self.rect_hs.centery = 625

        # The button messages only need to be prepped once
        self.prep_msgs()

    def prep_msgs(self):
        """Turn the messages into rendered images and center their texts on their buttons"""
        self.play_msg_image = self.font.render("Play!", True, self.text_color,
                                               self.button_color)
        self.play_msg_image_rect = self.play_msg_image.get_rect()
        self.play_msg_image_rect.center = self.rect_play.center

        self.hs_msg_image = self.font.render("High Scores", True, self.text_color,
                                             self.button_color)
        self.hs_msg_image_rect = self.hs_msg_image.get_rect()
        self.hs_msg_image_rect.center = self.rect_hs.center

    def draw_play_button(self):
        self.screen.fill(self.button_color, self.rect_play)
        self.screen.blit(self.play_msg_image, self.play_msg_image_rect)
        
    def draw_hs_button(self):
        self.screen.fill(self.button_color, self.rect_hs)
        self.screen.blit(self.hs_msg_image, self.hs_msg_image_rect)


