from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from MattyControls import *
import main


class Simulation(Frame):
    """The frame for the game simulation"""

    def __init__(self, master, log, game):
        frame_init(self, master, True)

        self.log = log
        self.game = game

        self.initControls(master)

        self.draw()

    def initControls(self, master):
        """Create all the buttons and other widgets"""
        self.g = Cnvs(self)
        self.g.bind("<Button-1>", self.click_left)
        self.g.bind("<Button-3>", self.click_right)
        self.g.width = main.WIDTH - 20
        self.g.height = main.HEIGHT - 20
        self.g.locateInside(self, H_LEFT, V_TOP)

        self.btnQuit = Btn(self, text="Quit", command=self.quit)
        self.btnQuit.locateInside(self, H_RIGHT, V_BOTTOM, 10)

    def draw(self):
        self.g.delete(ALL) # Because the tkinter canvas stores all the objects, so it's nothing like the HTML5 canvas where you draw and forget. Now we can draw and delete though, so sort of OK.
        self.g.create_rectangle(10, 10, 90, 50, fill="red", width=1)
        self.g.create_text(20, 20, anchor="nw", text="Hi Tom, this is some test text", fill="black", font="Consolas 12")

    def click_left(self, event):
        pass

    def click_right(self, event):
        pass

if __name__ == '__main__':
    import main
    main.main()
