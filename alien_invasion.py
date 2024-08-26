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
        esta parte do código está no settings - para organizar melhor o código
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
        self.bg_color = (230, 230, 230)
        """
        self.ship = Ship(self)
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)    
        self.settings.screen_width = self.screen.get_react().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
    def run_game(self):
        """Inicia o loop principal do jogo"""
        while True:
            self._check_events()
            self.ship.update()
            #Descarta os projétis que desaparecem
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <=0:
                    self.bullets.remove(bullet)
            print(len(self.bullets)) 
            self._update_screen()
            self.clock.tick(60)    
            # Observa eventos de teclado e mouse
    def _check_events(self):
        for event in pygame.event.get():
            """Respondendo as teclas pressionadas e a eventos de mouse"""   
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
                
    def _check_keydown_events(self, event):
        '''Responde a teclas pressionadas''' 
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True   
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        '''Responde a teclas soltas'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False    
               
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color) 
        self.ship.blitme()
        # Deixa a tela desenhada o mais recente visível
        pygame.display.flip()  

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
