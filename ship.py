import pygame

class Ship:
    '''Classe para cuidar da espaçonave'''

    def __init__(self, ai_game):
        '''Inicializa a espaçonave e define sua posição inicial'''
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        '''Desenha a espaçonave em sua localização atual'''
        self.screen.blit(self.image, self.rect)
