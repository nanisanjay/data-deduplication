from tkinter import *
import threading
from graphics import *
class Intro():
    def __init__(self,master):
        self.master = master
        self.master.geometry("800x600")
        self.master.title("Welcome")    
        self.label1 = Label(self.master,text ="Event Driven Programming Demonstration", fg = "blue", font = ("Purisa",22)).grid(row =6,column = 7)
        self.label2 = Label(self.master,text ="Program will auto-start in 5 seconds (or press the return key)", fg = "black").grid(row =7, column =7)
        self.master.bind("<Return>", self.goToDemo1)
    def goToDemo1(self):
        threading.Timer(5.0, goToDemo1).start()
        root2 = Toplevel(self.master)
        myGUI = Demo1(root2)
    def goToDemo1(self,event):
        root2 = Toplevel(self.master)
        myGUI = Demo1(root2)
    def finish(self):
        self.master.destroy()
def main():
    root = Tk()
    myGUIIntro = Intro(root)
    root.mainloop()
if __name__ =="__main__":
    main()
