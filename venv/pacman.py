import pygame


class PacMan(pygame.sprite.Sprite):
    
    def __init__(self, ai_settings, screen, maze):
        # Initialize PacMan and set his starting position
        super().__init__()
        self.ai_settings = ai_settings
        self.screen = screen
        self.maze = maze
        
        # Load the PacMan image and get its rect
        self.pm_image = pygame.image.load('images/pacmanR_2.png')
        self.rect = self.pm_image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new PacMan near the center of the map
        self.rect.centerx = self.screen_rect.centerx + 5
        self.rect.y = 470

        # Store a decimal value for pacmans centers
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
        # Collision flag
        self.collide_wall = False

    def check_wall_collision(self):
        if pygame.sprite.spritecollideany(self, self.maze.maze_blocks):
            self.collide_wall = True

    def update(self):
        # Update pacmans position based on the movement flag and if he has collided with a wall
        # Update pacmans center value, not the rect
         if self.moving_right and self.rect.right < self.screen_rect.right:
             self.centerx += self.ai_settings.pacman_speed_factor
         if self.moving_left and self.rect.left > 0:
             self.centerx -= self.ai_settings.pacman_speed_factor
         if self.moving_up and self.rect.top > 0 :
             self.centery -= self.ai_settings.pacman_speed_factor
         if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
             self.centery += self.ai_settings.pacman_speed_factor
            
        # Update rect object from self.center
         self.rect.centerx = self.centerx
         self.rect.centery = self.centery

    def blitme(self):
        # Draw PacMan at his current location
        self.screen.blit(self.pm_image, self.rect)