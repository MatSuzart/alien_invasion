class GameStats:
    '''Rastreia as estatísticas de Invasão Alienígena'''

    def __init__(self,ai_game):
        '''Inicializa as estatísticas'''
        self.settings = ai_game.settings
        self.reset_stats()
        self.high_score = 0
        self.prep_high_score()

    def reset_stats(self):
        '''Iniciliza as esta´tisticas que pode mudar durante o jogo'''
        self.ships_left = self.settings.ship_limit
        self.score = 0