import pygame
from setting import *
class DeathScreen:
    def __init__(self,img):
        self.screen = SCREEN
        self.image = pygame.image.load(f'Img/Backgrounds/{img}.jpg').convert()
        self.i =1

    def run(self):
        self.image.set_alpha(self.i)
        self.screen.blit(self.image,(0,0))     
        pygame.time.delay(20)
        self.i+=1
