import pygame
from setting import *


class Button():
    def __init__(self,posX,posY,
                imgB1,imgB2,text="",
                textColor1=(0,0,0),textColor2=(255,255,255)):
        
        self.screen = SCREEN
        self.rf = pygame.font.Font('Font\Segoe Print/segoeprint.ttf', FONTSIZE)

        self.createButton(imgB1,imgB2,posX,posY)
        
        self.posX = posX
        self.posY = posY
        self.textColor1 = textColor1
        self.textColor2 = textColor2

        self.text = text

        self.textColor = self.textColor1

    def createButton(self,imgB1,imgB2,posX,posY):
        self.imgB1 = pygame.image.load(imgB1).convert_alpha()
        self.imgB2 = pygame.image.load(imgB2).convert_alpha()
        self.imgB_rect = self.imgB1.get_rect(topleft = (posX,posY))  
        

    def buttonCondition(self):
        self.mouse_x,self.mouse_y = pygame.mouse.get_pos()
        if self.imgB_rect.collidepoint(self.mouse_x,self.mouse_y):
            self.screen.blit(self.imgB2,self.imgB_rect)
            self.textColor = self.textColor2
        else:
            self.screen.blit(self.imgB1,self.imgB_rect)
            self.textColor = self.textColor1 

    def retrunRect(self):
        return self.imgB_rect

    def displayText(self):
        self.text_rect = pygame.Rect = (self.posX+10,self.posY+20,820,60)
        self.line = self.rf.render(self.text,1,self.textColor)
        self.screen.blit(self.line,self.text_rect)


    def run(self):
        self.buttonCondition()
        self.displayText()

