from ast import Assert
import menuSetting
from setting import *

class Test_MenuSetting:
    def __init__(self):
        self.test = menuSetting.MenuSetting('MenuBack')

    def stm_none__1Returned(self):
        res = self.test.stm('CLICK')
        if res == 1: return True
        else: return False

    def fullscreen_none__fullscreen_Returned(self):
        self.test.fullScreen('CLICK')
        return Assert.AreEqual(SCREEN, pygame.display.set_mode((WIDTH,HEIGHT), pygame.FULLSCREEN))
    
    def windowScreen_none__fullscreen_Returned(self):
        self.test.windowScreen('CLICK')
        return Assert.AreEqual(SCREEN, pygame.display.set_mode((WIDTH,HEIGHT)))
        