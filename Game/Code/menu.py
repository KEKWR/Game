import pygame
from setting import *
import button,sys,storytelling,menuSetting,inquiry,catAnimation,menuBack

class Menu:

    def __init__(self,menuBackground,startFile,startBack):
        self.screen = SCREEN
        self.back = menuBack.MenuBack(menuBackground)
        self.menuS = menuSetting.MenuSetting(menuBackground)
        self.story = storytelling.Storytelling(startFile,startBack)
        self.inquiry = inquiry.Inquiry(menuBackground)
        self.bPlay = button.Button(870,270,'Img/Buttons/Play1.png','Img/Buttons/Play2.png')
        self.bSetting = button.Button(870,380,'Img/Buttons/Setting1.png','Img/Buttons/Setting2.png')
        self.bInquiry = button.Button(870,490,'Img/Buttons/Inquiry1.png','Img/Buttons/Inquiry2.png')
        self.bExit = button.Button(870,600,'Img/Buttons/Exit1.png','Img/Buttons/Exit2.png')
        self.menuVisible = 1
        self.place ='Menu'

        self.cA = catAnimation.CatAnimation()




    def exit(self,stat):
        if self.bExit.retrunRect().collidepoint(self.mouse_x,self.mouse_y) and stat == 'CLICK':
            pygame.quit()
            sys.exit() 

    def play(self,stat):
        if self.bPlay.retrunRect().collidepoint(self.mouse_x,self.mouse_y) and stat == 'CLICK':
            self.menuVisible = 2
            self.place =' '

    def setting(self,stat):
        if self.bSetting.retrunRect().collidepoint(self.mouse_x,self.mouse_y) and stat == 'CLICK':
            self.menuVisible = 3

    def inq(self,stat):
        if self.bInquiry.retrunRect().collidepoint(self.mouse_x,self.mouse_y) and stat == 'CLICK':
            self.menuVisible = 4

    def nextLine(self):
        self.story.nextLine()
    
    def vMenu(self,stat):
        match self.menuVisible:
            case 1:
                self.back.run()
                self.bPlay.run()
                self.bSetting.run()
                self.bInquiry.run()
                self.bExit.run()
                
                self.exit(stat)
                self.play(stat)
                self.setting(stat)
                self.inq(stat)
            
            case 2:
                self.story.run(stat)

            case 3:
                self.menuVisible = self.menuS.stm(stat)
                self.menuS.run(stat)

            case 4:
                self.menuVisible = self.inquiry.itm(stat)
                self.inquiry.run(stat)

    def hideHUD(self):
        self.story.hideHUD()
        
    def bestMethodToReturnHUDStatus(self):
        return self.story.returnHUDStatus()
     

    def run(self,stat):
        self.mouse_x,self.mouse_y = pygame.mouse.get_pos()
        self.vMenu(stat)
        self.cA.run(self.place)