from setting import *
import character

class Test_character:
    
    def __init__(self):
        self.char =character.Character(300,0,'none')



    
    def move_300_0__300_0Returned(self):
        self.char =character.Character(300,0,'none')
        self.char.move()
        res = (self.char.img_rect.x,self.char.img_rect.y)
        if res == (300,0): return True
        else: return False

    def move_200_0__300_0Returned(self):
        self.char =character.Character(200,0,'none')
        self.char.move()
        res = (self.char.img_rect.x,self.char.img_rect.y)
        if res == (200,0): return True
        else: return False

    def move_400_0__300_0Returned(self):
        self.char =character.Character(400,0,'none')
        self.char.move()
        res = (self.char.img_rect.x,self.char.img_rect.y)
        if res == (400,0): return True
        else: return False



    def moveL_300_0__minus100_0Returned(self):
        self.char =character.Character(300,0,'none')
        self.char.moveL()
        res = (self.char.img_rect.x,self.char.img_rect.y)
        if res == (-100,0): return True
        else: return False

    def moveL_200_0__minus100_0Returned(self):
        self.char =character.Character(200,0,'none')
        self.char.moveL()
        res = (self.char.img_rect.x,self.char.img_rect.y)
        if res == (-100,0): return True
        else: return False

    def moveL_400_0__minus100_0Returned(self):
        self.char =character.Character(400,0,'none')
        self.char.moveL()
        res = (self.char.img_rect.x,self.char.img_rect.y)
        if res == (-100,0): return True
        else: return False



    def moveR_300_0__720_0Returned(self):
        self.char =character.Character(300,0,'none')
        self.char.moveR()
        res = (self.char.img_rect.x,self.char.img_rect.y)
        if res == (720,0): return True
        else: return False

    def moveR_200_0__720_0Returned(self):
        self.char =character.Character(200,0,'none')
        self.char.moveR()
        res = (self.char.img_rect.x,self.char.img_rect.y)
        if res == (720,0): return True
        else: return False
    
    def moveR_400_0__720_0Returned(self):
        self.char =character.Character(400,0,'none')
        self.char.moveR()
        res = (self.char.img_rect.x,self.char.img_rect.y)
        if res == (720,0): return True
        else: return False



    def moveC_720_0__300_0Returned(self):
        self.char =character.Character(720,0,'none')
        self.char.moveC()
        res = (self.char.img_rect.x,self.char.img_rect.y)
        if res == (300,0): return True
        else: return False

    def moveC_minus100_0__300_0Returned(self):
        self.char =character.Character(-100,0,'none')
        self.char.moveC()
        res = (self.char.img_rect.x,self.char.img_rect.y)
        if res == (300,0): return True
        else: return False

    def moveC_300_0__300_0Returned(self):
        self.char =character.Character(300,0,'none')
        self.char.moveC()
        res = (self.char.img_rect.x,self.char.img_rect.y)
        if res == (300,0): return True
        else: return False



    def getName_none__noneReturned(self):
        self.char =character.Character(300,0,'none')
        self.char.getName()
        res = self.char.name
        if res == 'none': return True
        else: return False

    def getName_petr__petrReturned(self):
        self.char =character.Character(300,0,'petr')
        self.char.getName()
        res = self.char.name
        if res == 'Петруха': return True
        else: return False

    def getName_semn__semnReturned(self):
        self.char =character.Character(300,0,'semn')
        self.char.getName()
        res = self.char.name
        if res == 'Семёныч': return True
        else: return False
