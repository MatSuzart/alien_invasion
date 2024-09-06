import pygame

class Ship:
    '''Classe para cuidar da espaçonave'''

    def __init__(self, ai_game):
        '''Inicializa a espaçonave e define sua posição inicial'''
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.moving_right = False
        self.moving_left = False
    def upadte(self):
        """Atualiza a posição da espaçonova com base an flag"""
        if self.moving_right and self.rect.right< self.screen_react.right:
         self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left>0:
           self.x-= self.settings.ship_speed
        #Atualiza o objeto react a partir de self.x
        self.rect.x = self.x 
    def blitme(self):
        '''Desenha a espaçonave em sua localização atual'''
        self.screen.blit(self.image, self.rect)
    def center_ship(self):
       '''Centraliza a espaçonave na tela'''
       self.rect.midbottom = self.screen_rect_midbottom
       self.x = float(self.rect.x)