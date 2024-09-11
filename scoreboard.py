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

    def prep_score(self):
        '''Transforma a pontução em uma imagem renderizada'''
        score_str= str(self.stats.score)
        self.score_image = self.font.render(score_str,True,self.text_color,self.settings.bg_color)

        '''Exibe a pontuação no canto superior direito da tela'''

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        '''Desenha a pontuação na tela'''
        self.screen.blit(self.score_image,self.score_rect)
        
