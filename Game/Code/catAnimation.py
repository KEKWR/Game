import pygame,threading
from setting import *

class CatAnimation:
    def __init__(self):
        self.screen = SCREEN
        self.c0 = pygame.image.load(f'Img/catA/0.gif').convert_alpha()
        self.c1 = pygame.image.load(f'Img/catA/1.gif').convert_alpha()
        self.c2 = pygame.image.load(f'Img/catA/2.gif').convert_alpha()
        self.c3 = pygame.image.load(f'Img/catA/3.gif').convert_alpha()
        self.cc = 0
    def run(self,stat):
        if stat == 'Menu':
            self.cat_rect = self.c0.get_rect(topleft = (0,0))
            if self.cc in range(0,20):self.screen.blit(self.c0,self.cat_rect)
            elif self.cc in range(20,40):self.screen.blit(self.c1,self.cat_rect)
            elif self.cc in range(40,60):self.screen.blit(self.c2,self.cat_rect)
            elif self.cc in range(60,80):self.screen.blit(self.c3,self.cat_rect)

            self.cc+=1
            if self.cc >= 80: self.cc = 0
        
        