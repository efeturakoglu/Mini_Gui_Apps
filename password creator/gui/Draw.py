import pygame as pg



class rect:
    def __init__(self,Surface,Color,Width,Heigth,X,Y,Border = 0):
        self.Surface = Surface
        self.Color = Color
        self.Width = Width
        self.Heigth= Heigth
        self.X=X
        self.Y=Y

        if Border:
            pg.draw.rect(self.Surface,self.Color,(self.X,self.Y,self.Width,self.Heigth),Border)

        else:
            pg.draw.rect(self.Surface,self.Color,(self.X,self.Y,self.Width,self.Heigth))


class circle:
    def __init__(self, Surface, Color, Center,Radius, X, Y, Border=0):
        self.Surface = Surface
        self.Color = Color
        self.Center = Center
        self.Radius = Radius
        self.X = X
        self.Y = Y

        if Border:
            pg.draw.circle(self.Surface,self.Color,(self.Center,self.Radius),Border)
        else:
            pg.draw.circle(self.Surface,self.Color,(self.Center,self.Radius))

class line():
    def __init__(self,Surface,Color,Start,End,Width):
        self.Surface = Surface
        self.Color = Color
        self.start_point = Start
        self.end_point = End
        self.Width = Width


        pg.draw.line(self.Surface.Window,self.Color,self.start_point,self.end_point,self.Width)

