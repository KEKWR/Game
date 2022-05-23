import pygame,background,button
from setting import *

class Inquiry:
    def __init__(self,menuBackground):
        self.mouse_x,self.mouse_y = pygame.mouse.get_pos()
        self.screen = SCREEN
        self.back = background.Background(menuBackground)
        self.backB = button.Button(870,600,'Img/Buttons/Back1.png','Img/Buttons/Back2.png')
    
    def itm(self,stat):
        if self.backB.retrunRect().collidepoint(self.mouse_x,self.mouse_y) and stat == 'CLICK':
            return 1
        else:
            return 4


    def run(self,stat):
        self.mouse_x,self.mouse_y = pygame.mouse.get_pos()
        self.back.run()
        self.backB.run()
        self.itm(stat)