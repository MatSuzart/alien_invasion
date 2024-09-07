import pygame.font
class Button:
    def __init__(self,ai_game,msg): 
        ''''Inicializa os atributos do botão'''
        self.screen = ai_game.screen
        self.screen_rect = self.screen_rect()

        #Define as dimensões e propriedades do botão
        self.width,self.height = 200,50
        self.button_color = (0,135,0)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None,48)

        #Cria o objeto rect do botão e o centraliza
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center

        self._prep_msg(msg)
    def __prep__msg(self,msg):
        '''Transforma msg em uma imagem renderizada e centraliza texto no botão'''
        self.msg_image = self.font.render(msg,True, self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    def draw_button(self):
        '''Desenha o botão em branco e depois desenhe a mensagem'''
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)