import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """Classe geral para gerenciar ativos e comportamento do jogo"""

    def __init__(self):
        """Inicializa o jogo e cria recursos do jogo"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,
             self.settings.screen_height)
        )
        """
        está parte do código está no settings - para organizar melhor o código
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
        self.bg_color = (230, 230, 230)
        """
        self.ship = Ship(self)
        
    def run_game(self):
        """Inicia o loop principal do jogo"""
        while True:
            self._chech_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60) 
            # Observa eventos de teclado e mouse
    def _check_events(self):
        for event in pygame.event.get():
                """Respondendo as teclas pressionadas e a eventos de mouse"""   
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type==pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        #Move a espaçonave para a direita
                      self.ship.moving_right = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = False  
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color) 
        self.ship.blitme()
        # Deixa a tela desenhada o mais recente visível
        pygame.display.flip()              
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
