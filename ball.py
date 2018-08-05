import pygame

class Ball(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.image1 = pygame.image.load("images/球.jpg").convert_alpha()
        self.ball_speed = [3, -3]
        self.is_hit = False
        self.is_speedupball = False
        self.rect = self.image1.get_rect()

        self.width, self.height = bg_size[0], bg_size[1]
        self.rect.left, self.rect.top = (self.width - self.rect.width) // 2, self.height - self.rect.height - 50
        self.mask = pygame.mask.from_surface(self.image1)