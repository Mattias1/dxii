from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from MattyControls import *
#from PIL import Image, ImageTk

import maps.mapparser

class Simulation(Frame):
    """The frame for the game simulation"""

    def __init__(self, master, log, game):
        frame_init(self, master, True)

        self.log = log
        self.game = game

        # Hardcoded map for now
        self.map = maps.mapparser.MapParser.fromURL('http://dominating12.com/lib/ajax/api/map-info.php?map_id=27')
        #self.img = self.loadImg("space.png") # We must keep track of the reference ourselves, because tkinter is a C++ library and doesn't do it for us :S (this includes keeping track of the simulation object of course) - as soon as this reference is garbage collected the image dissapears.... :(:(:(

        self.initControls(master)

        self.draw()

    def initControls(self, master):
        """Create all the buttons and other widgets"""
        self.g = Cnvs(self)
        self.g.bind("<Button-1>", self.click_left)
        self.g.bind("<Button-3>", self.click_right)
        self.g.width = self.map.width
        self.g.height = self.map.height
        self.g.locateInside(self, H_LEFT, V_TOP)

    def draw(self):
        self.g.delete(ALL) # Because the tkinter canvas stores all the objects, so it's nothing like the HTML5 canvas where you draw and forget. Now we can draw and delete though, so sort of OK.
        
        #self.drawImg(100, 100, self.img)
        
        # Connection lines
        for t in self.map.territories.values():
            for c in t.connections:
                self.g.create_line(t.y, t.x, c.y, c.x, fill="gray")

        # Territory names
        for t in self.map.territories.values():
            self.g.create_text(t.y, t.x, anchor="center", text=t.name, fill="black", font="Consolas 10")

    def click_left(self, event):
        pass

    def click_right(self, event):
        pass

    def loadImg(self, path):
        return ImageTk.PhotoImage(Image.open("../img/" + path))

    def drawImg(self, x, y, img):
        self.g.create_image(x, y, image=img)

if __name__ == '__main__':
    import main
    main.main()
