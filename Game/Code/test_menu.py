import menu

class Test_menu:
    def __init__(self):
        self.menu = menu.Menu('MenuBack','001','laba')

    def init_none__1Returned(self):
        res = self.menu.menuVisible
        if res == 1: return True
        else: return False
    
    def play_none__2Returned(self):
        self.menu.play()
        res = self.menu.menuVisible
        if res == 2: return True
        else: return False

    def setting_none__3Returned(self):
        self.menu.setting()
        res = self.menu.menuVisible
        if res == 3: return True
        else: return False

    def inq_none__4Returned(self):
        self.menu.inq()
        res = self.menu.menuVisible
        if res == 4: return True
        else: return False