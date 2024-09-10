import pygame.font

class Scoreboard:
    '''Classe para exibir informações de pontuação'''

    def __init__(self,ai_game):
        '''Inicializa os atributos de pontuação'''
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.setttings = ai_game.settings
        self.stats = ai_game.stats

        #Configurações de fonte para informações de pontuação
        self.text_color(30,30,30)
        self.font = pygame.font.SysFont(None,48)

        #Prepara a imagem inicial da pontuação
        self.prep_score()
        
