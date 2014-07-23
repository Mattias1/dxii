from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from MattyControls import *
from PIL import Image, ImageTk
import urllib
import io

import maps.mapparser

class Simulation(Frame):
    """The frame for the game simulation"""

    def __init__(self, master, log, game):
        frame_init(self, master, True)

        self.log = log
        self.game = game

        # Hardcoded map for now
        self.map = maps.mapparser.MapParser.fromURL('http://dominating12.com/lib/ajax/api/map-info?map_id=1')

        self.img = self.loadImgFromWeb(self.map.imageUrl)

        self.territoryCircle = ImageTk.PhotoImage(Image.open('../gfx/territory_circles.png').crop((180,0,216,36)))

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
        
        self.drawImg(0, 0, self.img)
        
        # Connection lines
        #for t in self.map.territories.values():
        #    for c in t.connections:
        #        self.g.create_line(t.y, t.x, c.y, c.x, fill="gray")

        # Territory names
        #for t in self.map.territories.values():
        #    self.g.create_text(t.y, t.x, anchor="center", text=t.name, fill="black", font="Consolas 10")
        
        for t in self.map.territories.values():
            self.drawImg(t.y, t.x, self.territoryCircle)

    def click_left(self, event):
        pass

    def click_right(self, event):
        pass

    def loadImg(self, path):
        return ImageTk.PhotoImage(Image.open("../gfx/" + path))

    def loadImgFromWeb(self, url):
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        bytes = io.BytesIO(response.read())
        return ImageTk.PhotoImage(Image.open(bytes))

    def drawImg(self, x, y, img):
        self.g.create_image(x, y, image=img, anchor="nw")

if __name__ == '__main__':
    import main
    main.main()
