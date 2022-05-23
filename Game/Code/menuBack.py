import pygame
from setting import *

class MenuBack:
    def __init__(self,link):
        self.screen = SCREEN
        self.setBack(f'Img/Backgrounds/{link}.jpg')

    def setBack(self,link):
        self.img = pygame.image.load(link).convert()
        self.img_rect = self.img.get_rect(topleft = (0,0))
    
    def run(self):
        self.screen.blit(self.img,self.img_rect) 