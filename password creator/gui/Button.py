import pygame as pg
from pygame.constants import *

Black = (0,0,0)

class Button:
    def __init__(self, Window, Cursor, X, Y, Heigth, Width, Color,Transparency = False, Font_size = 18 ,Text="None",) -> None:
        self.Window = Window
        self.X = X
        self.Y = Y
        self.Heigth = Heigth
        self.Width = Width        
        self.Color = Color
        self.Cursor = Cursor
        self.Font_size = Font_size
        self.Text= Text
        self.Transparency = Transparency
        self.Button_is= False

    def Draw(self,Font_name = "consolas",  Color = Black):


        if self.Transparency:
            self.Shape = pg.Rect(self.X, self.Y, self.Width, self.Heigth)


        else:
            self.Shape = pg.draw.rect(self.Window.Window, self.Color, (self.X, self.Y, self.Width, self.Heigth))

        
        Font = pg.font.SysFont(Font_name, self.Font_size, False)

        if Font.size(self.Text)[0] >= self.Width:
            self.Font_size = (self.Font_size - 1 ) - 2


        Text_render = Font.render(self.Text, True, Color)

        self.Window.Window.blit(Text_render, (self.X + (self.Width * (1 / 10)), self.Y + (self.Heigth * (3/10))))


    def Collide(self, event):

        if self.Shape.colliderect(self.Cursor.Cursor):
            self.Color = (0,0,255)
            if event.type == MOUSEBUTTONDOWN:       
                self.Button_is = True
            else:
                self.Button_is = False
            
           

   


    
