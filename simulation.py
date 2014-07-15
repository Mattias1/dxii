from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from MattyControls import *


class Simulation(Frame):
    """The frame for the game simulation"""

    def __init__(self, master):
        Frame.__init__(self, master)
        master.title("Test")
        frame_init(self, master, True)

        self.createWidgets()

    def createWidgets(self):
        """Create all the buttons and other widgets"""
        self.btnHi = Btn(self)
        self.btnHi.text = "Hello"
        self.btnHi.command = self.say_hi
        self.btnHi.locateInside(self, H_LEFT, V_TOP, 10)

        self.canvas = Cnvs(self)
        self.canvas.bind("<Button-1>", self.click_left)
        self.canvas.bind("<Button-3>", self.click_right)
        self.canvas.width = WIDTH - 20
        self.canvas.height = HEIGHT - 20 - self.btnHi.height
        self.canvas.locateFrom(self.btnHi, H_COPY_LEFT, V_BOTTOM, 10)

        self.btnQuit = Btn(self, text="Quit", command=self.quit)
        self.btnQuit.locateInside(self, H_RIGHT, V_BOTTOM, 10)

if __name__ == '__main__':
    import main
    main.main()
