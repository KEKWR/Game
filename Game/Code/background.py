import pygame
from setting import *

class Background:

    def __init__(self,link):
        self.screen = SCREEN
        self.link = link
        self.setBack(f'Img/Backgrounds/{link}.jpg')
        self.i =1
        self.c =1

        self.vision = 0

    def setBack(self,link):
        self.img = pygame.image.load(link).convert()
        self.img_rect = self.img.get_rect(topleft = (0,0))

    def returnDVis(self):
        return self.vision


    def run(self):
        if self.c:
            self.vision = 0
            if self.i%3 == 0:
                self.img.set_alpha(self.i)
                self.screen.blit(self.img,self.img_rect)    
            self.i+=1
            if self.i ==100:
                self.c =0
        else:
            if self.link != 'blac' :self.vision = 1
            self.screen.blit(self.img,self.img_rect)  
        