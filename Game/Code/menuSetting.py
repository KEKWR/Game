import pygame,background,button
from setting import *

class MenuSetting:
    def __init__(self,menuBackground):
        self.screen = SCREEN
        self.mouse_x,self.mouse_y = pygame.mouse.get_pos()
        self.rf = pygame.font.Font('Font\Segoe Print/segoeprint.ttf', 30)
        self.backB = button.Button(870,600,'Img/Buttons/Back1.png','Img/Buttons/Back2.png')
        self.fullScreenB = button.Button(870,60,'Img/Buttons/FullScreen1.png','Img/Buttons/FullScreen2.png')
        self.windowScreenB = button.Button(450,60,'Img/Buttons/WindowScreen1.png','Img/Buttons/WindowScreen2.png')

        self.back = background.Background(menuBackground)
        self.displayMarker()



    def stm(self,stat):
        if self.backB.retrunRect().collidepoint(self.mouse_x,self.mouse_y) and stat == 'CLICK':
            return 1
        else:
            return 3

    def fullScreen(self,stat):
        if self.fullScreenB.retrunRect().collidepoint(self.mouse_x,self.mouse_y) and stat == 'CLICK':
            SCREEN = pygame.display.set_mode((WIDTH,HEIGHT), pygame.FULLSCREEN)

    def windowScreen(self,stat):
        if self.windowScreenB.retrunRect().collidepoint(self.mouse_x,self.mouse_y) and stat == 'CLICK':
            SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))

    def displaySpeedName(self):
        self.name = self.rf.render("Cкорость",1,(0,0,0))
        self.screen.blit(self.name,(1060,215))

    def displayScale(self):
        self.iS = pygame.image.load('Img/Other/Scale.png').convert_alpha()
        self.iS_rect = self.iS.get_rect(topleft = (450,200))
        self.screen.blit(self.iS,self.iS_rect)


    def displayMarker(self):
        self.iM = pygame.image.load('Img/Other/Marker.png').convert_alpha()
        match FPS:
            case 20:
                self.iM_rect = self.iM.get_rect(topleft = (400,170))
            case 60:
                self.iM_rect = self.iM.get_rect(topleft = (710,170))
            case 120:
                self.iM_rect = self.iM.get_rect(topleft = (970,170))
        
        self.screen.blit(self.iM,self.iM_rect)

    def moveMarker(self):
        self.screen.blit(self.iM,self.iM_rect)
        if self.iM_rect.collidepoint(self.mouse_x,self.mouse_y) and pygame.mouse.get_pressed()==(1,0,0) and self.mouse_x in range(465,1035):
            self.iM_rect = self.iM.get_rect(topleft = (pygame.mouse.get_pos()[0]-65,170))
            self.screen.blit(self.iM,self.iM_rect)

        elif self.iM_rect.collidepoint(self.mouse_x,self.mouse_y) and pygame.mouse.get_pressed()==(0,0,0) :
                if self.iM_rect.x in range(400,555): 
                    self.iM_rect = self.iM.get_rect(topleft = (400,170))
                    FPS = 20
                elif self.iM_rect.x in range(555,710): 
                    self.iM_rect = self.iM.get_rect(topleft = (710,170))
                    FPS = 60
                elif self.iM_rect.x in range(710,845): 
                    self.iM_rect = self.iM.get_rect(topleft = (710,170))
                    FPS = 60
                elif self.iM_rect.x in range(845,971): 
                    self.iM_rect = self.iM.get_rect(topleft = (970,170))
                    FPS = 120


    def run(self,stat):
        self.mouse_x,self.mouse_y = pygame.mouse.get_pos()
        self.back.run()
        self.backB.run()
        self.stm(stat)

        self.fullScreenB.run()
        self.fullScreen(stat)

        self.windowScreenB.run()
        self.windowScreen(stat)

        self.displayScale()
        self.moveMarker()

        self.displaySpeedName()
        