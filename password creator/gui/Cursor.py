import pygame as pg

class Cursor:
    def __init__(self,Window,Width=5,Heigth=5):
        self.Width = Width
        self.Heigth = Heigth
        self.Window = Window
        self.X = 0
        self.Y = 0
        self.Active = False
        self.Cursor = pg.Rect(self.X,self.Y,self.Width,self.Heigth) 

    def Draw(self):
        
        self.Cursor = pg.draw.rect(self.Window,(255,255,255),(self.X,self.Y, self.Width, self.Heigth),1)


    def Get_pos(self):

        self.X, self.Y = pg.mouse.get_pos()



       