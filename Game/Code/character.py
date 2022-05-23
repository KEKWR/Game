import pygame
from setting import *

class Character:

    def __init__(self,posX,posY,link):
        self.rf = pygame.font.Font('Font\Segoe Print/segoeprint.ttf', FONTSIZE)
        self.c =1
        self.l =0
        self.r =0
        self.cen = 0
        self.link = link
        self.screen = SCREEN
        self.i =0
        self.name = CHARNAME.get(self.link)
        
        self.createChar(link,(posX,posY))
        #self.dName()
             
    def createChar(self,link,pos):
        if self.link == 'none':
            self.img = pygame.image.load(f'Img/Characters/{link}.png').convert()
            self.img_rect = self.img.get_rect(topleft = pos)
        self.img = pygame.image.load(f'Img/Characters/{link}.png').convert_alpha()
        self.img_rect = self.img.get_rect(topleft = pos)

    def move(self):
        if self.c==1:
            self.img_rect.y-=2
            if self.img_rect.y == -30:
               self.c=2
        elif self.c==2:
            self.img_rect.y+=2
            if self.img_rect.y == 0:
                self.c=0

    def moveL(self):
        if self.l:
                self.img_rect.x-=SPEED
                if self.img_rect.x == -100:
                    self.l = 0

    def moveR(self):
        if self.r:
                self.img_rect.x+=SPEED
                if self.img_rect.x == 720:
                    self.r=0

    def moveC(self):
        if self.cen:
            if self.img_rect.x <300:
               self.img_rect.x+=SPEED
            elif self.img_rect.x >300:
               self.img_rect.x-=SPEED 
            elif self.img_rect.x ==300:
                self.cen = 0

    def getName(self):
        self.name = CHARNAME.get(self.link)
        self.named = self.rf.render(self.name,1,(255,255,255))
    
    def dName(self):
        self.getName()
        self.screen.blit(self.named, (80,510,1280,60))
        

    def run(self):
        if self.link == 'none':
            if self.i%3 == 0:
                self.img.set_alpha(self.i)
                self.screen.blit(self.img,self.img_rect)    
            self.i+=1

        self.screen.blit(self.img,self.img_rect)
        self.move() 
        
        