class Settings:
    """Classe para armazenar as configurações do jogo Invasão Alienígena"""

    def __init__(self):
        """Inicializa as configurações do jogo"""
        # Configurações da tela
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        #configuração da espaçonave
        self.ship_speed = 1.5
