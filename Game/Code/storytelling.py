import pygame
from setting import *
import character,background,button,deathScreen


class Storytelling:
    def __init__(self,startFile,startBack):
        self.screen = SCREEN
        self.rf = pygame.font.Font('Font\Segoe Print/segoeprint.ttf', FONTSIZE)

        self.mouse_x,self.mouse_y = pygame.mouse.get_pos()

        self.cv1 =0
        self.cv2 =0
        self.cv3 =0
        
        
        self.char1 = character.Character(300,0,'none')
        self.char2 = character.Character(300,0,'none')
        self.char3 = character.Character(300,0,'none')
        
        self.back = background.Background(startBack)

        self.i1 =1
        self.i2 =1
        self.buttonVisible =0
        self.visionName = 0

        self.bv = ' '

        self.d = 0

        self.openTxt(startFile)

        self.rect1 = pygame.Rect(80,555,1280,30)
        self.rect2 = pygame.Rect(80,580,1280,30)

        self.nextLine()

        self.dialogPanel = pygame.image.load('Img/Other/DialogPanel.png').convert_alpha()

        self.HUDStatus =1

    def openTxt(self,file):
        self.f = open(f'Story/{file}.txt', 'r',encoding='UTF-8')

    def nextLine(self):
        self.text1 = self.f.readline()[0:-1]
        self.text2 = ' '+self.f.readline()[0:-1]
        self.i1=1
        self.i2=1
        

    def showText(self):
        if self.HUDStatus:
            self.display()

            self.line1 = self.rf.render(self.text1[0:self.i1],1,(255,255,255))
            self.screen.blit(self.line1,self.rect1)
            self.line2 = self.rf.render(self.text2[1:self.i2],1,(255,255,255))
            self.screen.blit(self.line2,self.rect2)
        
            if self.i1 > len(self.text1):
                self.i2 +=TEXTSPEED
            self.i1 +=TEXTSPEED

            if self.i2 == len(self.text2):
                self.visionName = 0

    def display(self):
        self.displayM()
        self.display1()

    def display1(self):
        if self.text1[0:1] == '~':

            match self.text1[1:2]:
                case 'C':

                    match self.text1[2:3]:
                        case '1':
                            if self.text1[3:7] !='none':
                                self.char1 = character.Character(self.char1.img_rect.x,self.char1.img_rect.y,self.text1[3:7])
                                self.visionName = 1
                                self.cv1 =1
                            else: self.cv1 =0
                        case '2':
                            if self.text1[3:7] !='none':
                                self.char2 = character.Character(self.char2.img_rect.x,self.char2.img_rect.y,self.text1[3:7])
                                self.visionName = 2
                                self.cv2 =1
                            else: self.cv2 =0
                        case '3':
                            if self.text1[3:7] !='none':
                                self.char3 = character.Character(self.char3.img_rect.x,self.char3.img_rect.y,self.text1[3:7])
                                self.visionName = 3
                                self.cv1 =1
                            else: self.cv3 =0
                        case _:
                            pass

                case 'B':
                    self.back = background.Background(self.text1[2:6])

                case 'K':
                    self.bv = self.text1
                    self.buttonVisible =1
                    match self.text1[2:3]:
                        case '1':
                            self.nextLine()
                            self.b1 = button.Button(250,100,'Img/Buttons/Choise1.png','Img/Buttons/Choise2.png',self.text1[0:-1])

                        case '2':
                            self.nextLine()
                            self.b1 = button.Button(250,100,'Img/Buttons/Choise1.png','Img/Buttons/Choise2.png',self.text1[0:-1])
                            self.nextLine()
                            self.b2 = button.Button(250,170,'Img/Buttons/Choise1.png','Img/Buttons/Choise2.png',self.text1[0:-1])
                        
                        case '3':
                            self.nextLine()
                            self.b1 = button.Button(250,100,'Img/Buttons/Choise1.png','Img/Buttons/Choise2.png',self.text1[0:-1])
                            self.nextLine()
                            self.b2 = button.Button(250,170,'Img/Buttons/Choise1.png','Img/Buttons/Choise2.png',self.text1[0:-1])
                            self.nextLine()
                            self.b3 = button.Button(250,250,'Img/Buttons/Choise1.png','Img/Buttons/Choise2.png',self.text1[0:-1])
                        
                        case _:
                            pass
                
                case 'D':
                    self.dethScreen = deathScreen.DeathScreen(self.text1[2:6])
                    self.d =1

                case _:
                    pass


            self.nextLine()
    
    def displayM(self):
        if self.text1[0:1] == '*':
            match self.text1[1:2]:
                case '1':
                    match self.text1[2:3]:
                        case 'L': self.char1.l=1
                        case 'R': self.char1.r=1
                        case 'C': self.char1.cen = 1
                        case _:
                            pass

                case '2':
                    match self.text1[2:3]:
                        case 'L': self.char2.l=1
                        case 'R': self.char2.r=1
                        case 'C': self.char2.cen = 1
                        case _:
                            pass

                case '3':
                    match self.text1[2:3]:
                        case 'L': self.char3.l=1
                        case 'R': self.char3.r=1
                        case 'C': self.char3.cen = 1
                        case _:
                            pass
                case _:
                    pass

            self.nextLine()

    def buttonAct(self,stat):
        if self.buttonVisible:

            if self.bv[0:2] == '~K':

                match self.bv[2:3]:
                    case '1':
                        self.b1.run()

                        if self.b1.retrunRect and stat == 'CLICK':
                            self.buttonVisible =0
                            self.openTxt(self.bv[3:6])

                    case '2':
                        self.b1.run()
                        self.b2.run()

                        if self.b1.retrunRect().collidepoint(self.mouse_x,self.mouse_y) and stat == 'CLICK':
                            self.buttonVisible =0
                            self.openTxt(self.bv[3:6])

                        elif self.b2.retrunRect().collidepoint(self.mouse_x,self.mouse_y) and stat == 'CLICK':
                            self.buttonVisible =0
                            self.openTxt(self.bv[6:9])

                    case '3':
                        self.b1.run()
                        self.b2.run()
                        self.b3.run()

                        if self.b1.retrunRect().collidepoint(self.mouse_x,self.mouse_y) and stat == 'CLICK':
                            self.buttonVisible =0
                            self.openTxt(self.bv[3:6])
        
                        elif self.b2.retrunRect().collidepoint(self.mouse_x,self.mouse_y) and stat == 'CLICK':
                            self.buttonVisible =0
                            self.openTxt(self.bv[6:9])

                        elif self.b3.retrunRect().collidepoint(self.mouse_x,self.mouse_y) and stat == 'CLICK':
                            self.buttonVisible =0
                            self.openTxt(self.bv[9:12])

    def vName(self):
        if self.HUDStatus:
            match self.visionName:
                case 1:
                    self.char1.dName()
                case 2:
                    self.char2.dName()
                case 3:
                    self.char3.dName()


    def displayDethScreen(self,v):
        if v: self.dethScreen.run()

    def displayDialogPanel(self):
        if self.HUDStatus:
            self.screen.blit(self.dialogPanel,(70,510,1280,30))

    def displayCharacter(self):
        if self.cv1:
            self.char1.run()
            self.char1.moveL()
            self.char1.moveR()
            self.char1.moveC()
        if self.cv2:
            self.char2.run()
            self.char2.moveL()
            self.char2.moveR()
            self.char2.moveC()
        if self.cv3:
            self.char3.run()
            self.char3.moveL()
            self.char3.moveR()
            self.char3.moveC()

    def hideHUD(self):
        if self.HUDStatus ==1 : self.HUDStatus=0
        else: self.HUDStatus=1

    def returnHUDStatus(self):
        return self.HUDStatus

    def run(self,stat):
        self.mouse_x,self.mouse_y = pygame.mouse.get_pos()

        self.back.run()

        self.displayCharacter()

        self.displayDialogPanel()
        
        self.showText()

        self.buttonAct(stat)

        self.vName()

        self.displayDethScreen(self.d)
        




