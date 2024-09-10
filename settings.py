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
        self.ship_limit = 3
        #Configurações do projétil
        self.bullet_speed = 2.5
        self.bullet_with = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        '''Inicializa as configurações que mudam ao longo do jogo'''
        self.ship_speed = 1.5
        self.bullet_speed = 2.5
        self.alien_speed = 1.0

        #fleet_direction de 1 representa a direta; -1 representa a esquerda

        self.fleet_direction = 1
    def increase_speed(self):
        '''Aumenta as configurações de velocidade'''
        self.ship_speed *= self.speed_slace
        self.bullet_speed *=self.speedup_scale
        self.alien_speed *= self.speedup_scale