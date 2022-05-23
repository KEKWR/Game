import pygame,sys
from setting import *
import menu

class Game:

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = SCREEN
        pygame.display.set_caption('Game')
        self.status = 'None'


    def run(self):
        self.screen = SCREEN

        self.menu = menu.Menu('MenuBack','001','laba')

        while 1:

            self.clock.tick(FPS)

            self.menu.run(self.status)
            
            self.status = 'None'
                      
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONDOWN and self.menu.place == 'Menu':
                    self.status = 'CLICK'

                elif event.type == pygame.MOUSEBUTTONDOWN :
                    self.menu.nextLine()
                    self.status = 'CLICK'

                elif event.type == pygame.KEYDOWN :
                    if pygame.key.get_pressed()[pygame.K_h]:
                        self.menu.hideHUD()
                    else:
                        if self.menu.bestMethodToReturnHUDStatus():    
                            self.menu.nextLine()
            
            pygame.display.update()
            
            

        
            

if __name__ == '__main__':
    game = Game()
    game.run()