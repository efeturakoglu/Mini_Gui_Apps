import sys,random

from gui.Window import *
from gui.Button import *
from gui.Colors import *
from gui.Cursor import *
from gui.Text import *
from gui.Textbox import *
from gui.Draw import *
from gui.particle import *
from gui.ListMenu import *

from password_generator import password_generate

Surface = Window(1000,500,"Password Generator")

            
Password = ''
Counter = 0
particles = []
Cursor_ = Cursor(Surface.Window)
Event= ''

Title_Text = uneditable_Text(Surface,100,50,"Password Generator",Font_size=20,Font_name='Arial',Color=(44, 62, 80))
Text_1 = uneditable_Text(Surface,100,80,"password generator for users",Font_size=15,Font_name='Arial',Color=(44, 62, 90))


Sumbit_button = Button(Surface,Cursor_,100,150,50,100,(44, 62, 80),True,Text='Generate !')
List_menu_ = List_menu(Surface,Cursor_,300,165,30,20,['4','8','12','16','32'],Text= '-',Color=(200, 200, 200))

while True:

    Counter += 1

    Surface.Window.fill((200, 200, 200))
    add_particle(Surface.Window,Counter,volume = 10)
    Cursor_.Draw()
    Sumbit_button.Draw(Font_name= 'Arial',Color = (44, 62, 80))
    List_menu_.Draw()

    Line = line(Surface,(6, 32, 71),(90,185),(300,185),1)

    Line = line(Surface,(6, 32, 71),(90,75),(400,75),1)

    Line = line(Surface,(6, 32, 71),(600,185),(900,185),1)
    Line = line(Surface,(6, 32, 71),(650,195),(850,195),1)
    Line = line(Surface,(6, 32, 71),(720,205),(770,205),1)



    Title_Text.Draw()
    Text_1.Draw()
    # Cursor process
    Cursor_.Get_pos()


    # Get event 
    for event in pg.event.get():
    
        if event.type == pg.QUIT:
            sys.exit()

        
        List_menu_.Collide(event)
        Sumbit_button.Collide(event)

        if List_menu_.Active == 'Open':
            Password = ''
        try:

            if Sumbit_button.Button_is:
                Password = password_generate(List_menu_.Button_text)

        except:
            Password = 'Lütfen Sayı Seçiniz'

    if List_menu_.Button_text == '-':
        uneditable_Text(Surface,680,167,Password,15).Draw()
    if List_menu_.Button_text == '4':
        uneditable_Text(Surface,720,167,Password,15).Draw()
    if List_menu_.Button_text == '8':
        uneditable_Text(Surface,700,167,Password,15).Draw()
    if List_menu_.Button_text == '12':
        uneditable_Text(Surface,670,167,Password,15).Draw()
    if List_menu_.Button_text == '16':
        uneditable_Text(Surface,670,167,Password,15).Draw()
    if List_menu_.Button_text == '32':
        uneditable_Text(Surface,620,167,Password,15).Draw()

    if Counter >= 10:
        Counter = 0


    Update()