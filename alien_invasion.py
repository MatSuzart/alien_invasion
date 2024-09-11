import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from time import sleep
from game_stats import GameStats
from button import Button

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
             self.stats = GameStats(self)
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
        self.game_active = False
        self.sb = Scoreboard(self)
        #Cria botão Play
        self.play_button = Button(self, "Play")
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
            if self.game_active:
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
    def _ship_hit(self):
        '''Responde á espaçonave sendo abatida por um alienígena'''
        #Decrementa quaisquer projéteis e alienígenas restantes
        if self.stats.ships_left >0:
            self.statis_left -= 1
            #Descarta quaisquer projéteis e alienígenas restantes
            self.bullets.empty()
            self.aliens.empty()
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)
        #Cria uma frota nova e centraliza a espaçonave
        self._create_fleet()
        self.ship.center_ship()
        #Pausa
        sleep(0.5)
    def _check_aliens_bottom(self):
        '''Verifica se algum alienígena chegou a parte inferior da tela'''
        for alien in self.aliens.sprintes():
            if alien.rect.bottom >=self.settings.screen_height:
                #Trata isso como se a espaçonave tivesse sido abatida
                self.ship_hit()
                break
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
    def _check_play_button(self,mouse_pos):
        ''''Inicia um jogo novo quando o jogador clica em Play'''
        if self.play_button.rect.collidepoint(mouse_pos):
            self.stats.rect_stats()
            self.settings.initialize_dynamic_settings()
            self.game_active = True
            #Descarta quaiquer projéteis e alienígenas restantes
            self.bullets.empty()
            self.aliens.empty()
            self.sb.prep.score()
            #Cria uma frota nova e centraliza a espaçonave
            self._create_fleet()
            self.ship.center_ship()
            pygame.mouse.set_visible(False)
    def _fire_bullet(self):
        '''Criar um novo projétil e o adiciona ao grupo projétis'''
        if len (self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    def _update_bullets(self):
        '''Atualiza a posição dos projéteis e descarta os projéteis antigos'''
        #Verifica se algum projétil atingiu um alienígena
        #Se sim, descarta o projétil e o alienígena
        collisions = pygame.sprite.groupcollide(
            self.bullets,self.aliens,True,True)
        if not self.aliens:
            #Destrói os projéteis existentes e cria uma forta nova
            self.bullets.empty()
            self._create_fleet()
        
    def _check_keyup_events(self, event):
        '''Responde a teclas soltas'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False    
    def _check_fleet_edges(self):
        '''Responde apropriadamente se algum alienígena alcançou uma borda'''
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    def _change_fleet_direction(self):
        ''''Faz toda a forta descer e mudar de direção'''
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1     
    def _update_aliens(self):
        '''Verifica se a forta está na borda e, sem seguida atualiza as posições'''
        self._check_fleet_edges()
        self.aliens.update()   
        self._check_bullet_alien_collisions()
        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            self._ship_hit()
            self._check_aliens_bottom()
            print("Ship hit!!!")
        if collisions:
            for aliens in collision.values():
                self.stats.score +=self.settings.alien_points * len(aliens)
            self.stats.score += self.settings.alien_points
            self.sb.prep_score()    
    def _check_bullet_alien_collisions(self):
        '''Responde á colisões alienígenas'''
        # Remove todos os prjéteis e os alienígenas que tenham colidido    
        if not self.aliens:
            #Destrói os projéteis existentes e cria uma frota nova

            self.bullets.empty()
            self.create_fleet()
            self.settings.increase_speed()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color) 
        for bullet in self.bullets.sprintes():
            bullet.draw_bullet()
        self.ship.blitme()
        self.sb.shoe_score()
        self.aliens.draw(self.screen)
        # Deixa a tela desenhada o mais recente visível
        if not self.game_active:
            self.play_button.draw_button()
        pygame.display.flip()  

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
