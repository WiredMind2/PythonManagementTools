from tkinter import *
from PIL import Image, ImageTk
from time import sleep
import Background
import Diviseur
import os
import keyboard
import threading

fenSize = [200,200,40,40]
tileSize = 50
fenButtons = []
fenButtonsImage = []

shorcutKey = "F8"

theme = "Gray"

iconsPath = os.getcwd()+"/Icons/"+theme+"/"

#---------------------------------------------Resizing-----------------------------------------

def updateFenPos():
    fenSize[:2] = [tileSize*len(fenLayout[0]),tileSize*len(fenLayout)]

    #mouse position relative to the upper-left corner
    x = fen.winfo_pointerx() - fen.winfo_vrootx()
    y = fen.winfo_pointery() - fen.winfo_vrooty()
    #test if mouse position is out of the borders
    #print(x,y)
    if x+int(fenSize[0]/2) > mngr.winfo_screenwidth():
        x = mngr.winfo_screenwidth() - int(fenSize[0]/2)
    elif x-int(fenSize[0]/2) < 0:
        x = int(fenSize[0]/2)
    if y+int(fenSize[1]/2) > mngr.winfo_screenheight():
        y = mngr.winfo_screenheight() - int(fenSize[1]/2)
    elif y-int(fenSize[1]/2) < 0:
        y = int(fenSize[1]/2)

    fen.geometry("{}x{}+{}+{}".format(fenSize[0],fenSize[1],x-int(fenSize[0]/2),y-int(fenSize[1]/2)))

def configureButtonsImage():
    for x in range(len(fenLayout)):
        fenButtonsImage.append([])
        for y in range(len(fenLayout[x])):
            if fenIcons[x][y] == "":
                fenIcons[x][y] = "empty"
            img = ImageTk.PhotoImage(Image.open(iconsPath+fenIcons[x][y]+".gif").resize((tileSize, tileSize)))
            #fenButtonsImage[x].append(PhotoImage(file = iconsPath+fenIcons[x][y]+".gif").subsample(3, 3))
            fenButtonsImage[x].append(img)

def configureButtons():
    configureButtonsImage()
    fenButtons = []
    for x in range(len(fenLayout)):
        fenButtons.append([])
        for y in range(len(fenLayout[x])):
            #fenButtons[x]
            fenButtons[x].append(Button(frame, text=fenLayout[x][y], image=fenButtonsImage[x][y]))
            pos = [x,y]
            fenButtons[x][y].configure(command=lambda pos=[x,y]: actionManager(pos))
            fenButtons[x][y].grid(row=x, column=y, sticky="nsew")
            if(fenLayout[x][y] == ""):
                color = "white"
                bdSize = 0
            elif theme == "Transparent":
                color = "#fefefe"
                bdSize = 2
            elif theme == "Gray":
                color = "#404040"
                bdSize = 2
            fenButtons[x][y].configure(bg=color,bd=bdSize)
    for x in range(len(fenLayout[x])):
        frame.columnconfigure(x, weight=1)

    for y in range(len(fenLayout)):
        frame.rowconfigure(y, weight=1)

#-------------------------Buttons Functions-----------------------------------------------

def mediaKey(key):
    os.system("python "+os.getcwd()+"/MediaKeys/MediaKeys.py {}".format(key))

def Quit():
    #exitButton.configure(bg="#404040", borderwidth=2, fg="black")
    exitButton.pack_forget()
    mngr.geometry("1x1")
    fen.withdraw()
    print("quit")
    #while not keyboard.is_pressed('F10'):
    #    sleep(0.1)
    keyboard.wait(shorcutKey)
    Show()
    

def Destroy():
    fen.destroy()
    mngr.destroy()

def QuickView():
    keyboard.press_and_release('win+d')

def DivideThread():
    Diviseur.Diviseur().window()
    
def Divide():
    fen = threading.Thread(target=DivideThread)
    fen.start()
    
def Spotify():
    os.system("START spotify")

def e():
    print("a")

def actionManager(pos):
    #print(pos[0],pos[1])
    mngr.focus_force()
    x = pos[0]
    y = pos[1]
    if fenArgs[x][y] is None:
        fenActions[x][y]()
    else:
        fenActions[x][y](fenArgs[x][y])

#-------------------------Fen Lists-----------------------------------------------

fenLayout = [["","","QuickView","",""],
             ["","Back","Quit","Next",""],
             ["Diviseur","Down","","Up","Spotify"],
             ["","Back","Play","Next",""],
             ["","","Destroy","",""]]

fenIcons = [["","","fullscreen","",""],
            ["","skip-backwards","menu","skip-forwards",""],
            ["add","mute","","volume-up","spotify"],
            ["","skip-backwards","play","skip-forwards",""],
            ["","","delete","",""]]

fenActions = [[e,e,QuickView,e,e],
              [e,Background.Back,Quit,Background.Next,e],
              [Divide,mediaKey,e,mediaKey,Spotify],
              [e,mediaKey,mediaKey,mediaKey,e],
              [e,e,Destroy,e,e]]

fenArgs = [[None,None,None,None,None],
           [None,False,None,False,None],
           [None,"d",None,"u",None],
           [None,"pp","p","n",None],
           [None,None,None,None,None]]

#--------------------------Main----------------------------------------------------

mngr = Tk()
exitButton = Button(mngr, text="Exit", command=mngr.destroy, bg="#404040", borderwidth=2, fg="black")
exitButton.pack(fill=BOTH, expand=1)

def Show(a = 1):
    #exitButton.configure(bg="white", borderwidth=0, fg="white")
    print("show")
    exitButton.pack(fill=BOTH, expand=1)
    mngr.geometry("{}x{}".format(fenSize[2],fenSize[3]))
    fen.deiconify()
    updateFenPos()
    return

def init():
    global frame,fen
    mngr.overrideredirect(True)
    screenX = mngr.winfo_screenwidth()
    screenY = mngr.winfo_screenheight()
    mngr.geometry("{}x{}+{}+{}".format(fenSize[2],fenSize[3],screenX-fenSize[2],screenY-fenSize[3]))
    mngr.config(bg="white")
    mngr.wm_attributes("-transparentcolor", "white")
    mngr.wm_attributes("-topmost", 1)
    #Label(mngr, text="Input").pack(fill=BOTH, expand=1)
    mngr.withdraw()
    #mngr.bind("<"+shorcutKey+">", Show)
    keyboard.wait(shorcutKey)

    fen = Toplevel()
    fen.overrideredirect(True)
    fen.config(bg="white")
    fen.wm_attributes("-transparentcolor", "white")
    fen.wm_attributes("-topmost", 1)

    frame=Frame(fen,bg="pink")
    Grid.rowconfigure(fen, 0, weight=1)
    Grid.columnconfigure(fen, 0, weight=1)
    frame.grid(row=0, column=0, sticky=N+S+E+W)

    configureButtons()
        
    updateFenPos()
    
    mngr.mainloop()

init()

#keyboard.on_press_key(shortcutKey, Show)
#Quit(False)
