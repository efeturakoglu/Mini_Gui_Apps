import pygame as pg

class İmage:
    def __init__(self,Window,Path,X,Y):
        self.Path = Path
        self.İmage = pg.image.load(self.Path)
        Window.Window.blit(self.İmage,(X,Y))


    def ReScale(self, Scale):
        self.İmage = pg.transform.scale((Scale))



def Load_image(path):
    return pg.image.load(path)

