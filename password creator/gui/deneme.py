import sys

import Draw
import Window
import Constant

Surface = Window.Window(200,200,"deneme")


while True:

    for event in Constant.Get():
        if event.type == Constant.QUIT:
            sys.exit()


    rect = Draw.rect(Surface.Window,(255,0,0),50,10,10,10)
    Window.Update()