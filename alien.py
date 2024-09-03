import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''Classe para representar um único alienígena na frota'''
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        
        #.Carrega a imagem do alienígena e define seu atributo rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #Inicia cada alienígena novo perto do canto superior esquerdo da tela
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Armazena a posição horizontal exata do alienígena 
        self.x = float(self.rect.x)
        
