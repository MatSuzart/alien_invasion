import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

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
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)    
        self.settings.screen_width = self.screen.get_react().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
    def _create_fleet(self):
        '''Criada a frota de alienígenas'''
        #Cria um alienígena
        alien = Alien(self)
        alien_with, alein_height = alien.rect.size

        current_x,current_y = alien_with,alein_height
        while current_y <(self.settings.screen_height -2 * alein_height):
         while current_x <(self.settings.screen_width - 2* alien_with):
            self._create_alien(current_x,current_y)
            current_x = alien_with
            current_x += 2* alein_height
            current_x += 2* alien_with
    def _creat_alien(self,x_position,y_position):
        '''Cria um alienígena e o posiciona na fileira'''
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)
        current_x +=2* alien_with
        self.aliens.add(alien)
    def run_game(self):
        """Inicia o loop principal do jogo"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            
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
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()    
    
    def _fire_bullet(self):
        '''Criar um novo projétil e o adiciona ao grupo projétis'''
        if len (self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    def _update_bullets(self):
        '''Atualiza a posição dos projéteis e descarta os projéteis antigos'''
    def _check_keyup_events(self, event):
        '''Responde a teclas soltas'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False    
               
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color) 
        for bullet in self.bullets.sprintes():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        # Deixa a tela desenhada o mais recente visível
        pygame.display.flip()  

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
