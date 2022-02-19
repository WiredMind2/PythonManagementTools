from tkinter import *
from time import sleep

class Diviseur():
    def window(self):
        self.pop1 = Tk()
        self.entry1 = Entry(self.pop1)
        self.entry1.grid(row=0,column=0,sticky=E+W)
        self.entry1.focus()
        self.cmptBttn = Button(self.pop1,text="Compute",command=self.testValid)
        self.cmptBttn.grid(row=1,column=0)
        self.pop1.bind("<Return>", self.testValid)
        self.pop1.mainloop()

    def result(self):
        self.number1 = int(self.number1)
        self.number2 = int(self.number2)
        
        self.compute()
        if hasattr(self, 'commonLabels'):
            for i in self.commonLabels:
                i.grid_forget()
                self.commonLabels.remove(i)
        else:
            self.commonLabels = []

        if hasattr(self, 'smallestFracLbl'):
            self.smallestFracLbl.grid_forget()
            self.smallestFracLbl = ""
            
        if len(self.common) >= 1:
            self.entry1.grid(columnspan=len(self.common))
            self.cmptBttn.grid(columnspan=len(self.common))
            Label(self.pop1,text = str(self.number1) + " and " + str(self.number2) + " have " + str(len(self.common)) + " dividers:").grid(row=2,columnspan=len(self.common),sticky=E+W)
            for i in range(len(self.common)):
                self.pop1.grid_columnconfigure(i, weight=1)
                lbl = Label(self.pop1, text = self.common[i])
                lbl.grid(row=3,column=i)
                self.commonLabels.append(lbl)
                
            smallestFrac = str(int(self.number1/int(self.common[len(self.common)-1])))+"/"+str(int(self.number2/int(self.common[len(self.common)-1])))

            self.pop1.clipboard_clear()
            self.pop1.clipboard_append(smallestFrac)
            self.pop1.update()
            
            self.smallestFracLbl = Label(self.pop1, text = "The smallest fraction is : " + smallestFrac)
            self.smallestFracLbl.grid(row=4,columnspan=len(self.common),sticky=E+W)
        else:
            Label(self.pop1, text = str(self.number1) + " and " + str(self.number2) + " don't have any dividers").grid(row=2,sticky=E+W)
        
    def testValid(self,event = None):
        if hasattr(self, 'number1'):
            self.number2 = self.number1
            
        self.number1 = self.entry1.get()
        self.entry1.delete(0,END)
        if self.number1 == "":
            self.pop1.destroy()
            if hasattr(self, 'lastPop'):
                self.lastPop.destroy()
        elif "/" in self.number1:
            self.number1,self.number2 = self.number1.split("/")
            self.result()
        elif hasattr(self, 'number1') and hasattr(self, 'number2'):
            self.result()
        
    def shell(self):
        self.number1 = input("Calc => ")
        if("/" in self.number1):
            self.number1,self.number2 = self.number1.split("/")
        else:
            self.number2 = input("/ par : ")

        self.number1 = int(self.number1)
        self.number2 = int(self.number2)
            
        self.common = []
        self.compute(self.number1,self.number2)

        if len(self.common) >= 1:
            print(str(self.number1) + " and " + str(self.number2) + " have " + str(len(self.common)) + " dividers:")
            for i in self.common:
                print(i)

    def compute(self):
        self.common = []
        if self.number1 < self.number2:
            self.number1,self.number2 = self.number2,self.number1

        for i in range(1,self.number1):
            if self.number1/i == int(self.number1/i) and self.number2/i == int(self.number2/i):
                if i != 1:
                    self.common.append(str(i))

Diviseur().window()
