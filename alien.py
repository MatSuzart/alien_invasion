import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''Classe para representar um único alienígena na frota'''
def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        #.Carrega a imagem do alienígena e define seu atributo rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #Inicia cada alienígena novo perto do canto superior esquerdo da tela
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Armazena a posição horizontal exata do alienígena 
        self.x = float(self.rect.x)
def update (self):
     self.x += self.settings.alien_speed * self.settings.fleet_direction
     self.rect.x = self.x
def check_edges(self):
    '''Retorna True se o alienígena estiver na boarda da tela'''
    screen_rect - self.screen.get_rect()
    return (self.rect.right>=screen_rect.right) or (self.rect.lef <=0)
    def update(self):
        '''Move o alienígena para a direita'''
        self.x += self.settings.alien_speed
        self.rect.x = self.x