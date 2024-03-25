import sys
import pygame

from settings import Settings

class AlienInvasion:
    """Classe geral para gerenciar ativos e comportamento do jogo"""

    def __init__(self):
        """Inicializa o jogo e cria recursos do jogo"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings

        self.screen = pygame.display.set_mode(
            (self.settings.screen_with,
             self.settings.screen_height)
        )
        """
        está parte do código está no settings - para organizar melhor o código
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
        self.bg_color = (230, 230, 230)
        """
    def run_game(self):
        """Inicia o loop principal do jogo"""
        while True:
            # Observa eventos de teclado e mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    
            self.screen.fill(self.settings.bg_color)       
            # Deixa a tela desenhada o mais recente visível
            pygame.display.flip()
            self.clock.tick(60)
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
