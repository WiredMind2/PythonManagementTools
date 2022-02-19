import ctypes
import os
from tkinter import *
from time import sleep

pics = os.listdir("C:/Users/willi/Pictures/FondEcran")

def Update(i,alone):
    #print(i,pics)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:/Users/willi/Pictures/FondEcran/" + pics[i] , 0)
    if(alone):
        idx.config(text=i+1)
        crt.config(text=pics[i])#.split('.',1)[0] pour enlever la terminaison
    f = open("C:/Users/willi/Pictures/MiscBg/index.txt","w")
    f.write(str(i))
    f.close()

def Next(alone = True):
    f = open("C:/Users/willi/Pictures/MiscBg/index.txt","r")
    i = int(f.read())
    if i == len(pics)-1:
        i = 0
    else:
        i += 1
    Update(i,alone)
    #Animate(fwd)
    f.close()
        
def Back(alone = True):
    f = open("C:/Users/willi/Pictures/MiscBg/index.txt","r")
    i = int(f.read())
    if i == 0:
        i = len(pics)-1
    else:
        i -= 1
    Update(i,alone)
    #Animate(bck)
    f.close()

def Animate(frames, ind=0):
    frame = frames[ind]
    if ind < len(frames)-1:
        ind += 1
        nxt.configure(image=frame)
        fen.after(100, Animate, frames, ind)
    else:
        nxt.configure(image=frames[0])
def Run():
    global idx,crt
    fen = Tk()
    fen.overrideredirect(True)
    fen.config(bg="white")
    fen.wm_attributes("-transparentcolor", "white")
    fen.wm_attributes("-topmost", 1)

    fwd = [PhotoImage(file='C:/Users/willi/Pictures/MiscBg/skip-forward/skip-forwards.gif',format = 'gif -index %i' %(i)) for i in range(28)]
    bck = [PhotoImage(file='C:/Users/willi/Pictures/MiscBg/skip-backwards/skip-backwards.gif',format = 'gif -index %i' %(i)) for i in range(28)]

    nxt = Button(fen,text="Next",command=Next,bd=0)
    nxt.grid(column=2,sticky=E+W,row=0)
    ext = Button(fen,text = "Quit",command=fen.destroy,bd=0,bg="#303030")
    ext.grid(column=1,sticky=E+W,row=0)
    bck = Button(fen,text="Back",command=Back,bd=0)
    bck.grid(column=0,sticky=E+W,row=0)

    fen.grid_columnconfigure(0, minsize=40)
    fen.grid_columnconfigure(1, minsize=40)
    fen.grid_columnconfigure(2, minsize=40)

    idx = Label(fen,bd=2,bg="#303030")
    idx.grid(column=0,sticky=E+W,row=1)
    crt = Label(fen,bd=2,bg="#303030")
    crt.grid(column=1,columnspan=2,sticky=E+W,row=1)

    Next()
    Back()
    fen.mainloop()

if __name__ == "__main__":
    Run()
