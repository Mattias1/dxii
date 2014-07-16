from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from MattyControls import *
import main
import log


TB_PASTE_LABEL = "Paste API content here:" + ''.join([' '] * 99)


class InputData(Frame):
    """The frame for the input (game log, game info, map info)"""

    def __init__(self, master, log, game):
        frame_init(self, master, True)
        self.log = log
        self.game = game
        self.initControls()

    def initControls(self):
        """Create all the buttons and other widgets"""
        sv1 = StringVar()
        sv1.trace("w", lambda name, index, mode, sv1=sv1: self.updateAPILinks(sv1))
        self.tbGameNr = Tb(self, textvariable=sv1)
        self.tbGameNr.width = 70
        self.tbGameNr.locateInside(self, H_LEFT, V_TOP)
        self.tbGameNr.addLabel("Game number:")

        self.tbAPIs = []
        for i in range(4):
            self.tbAPIs.append(Tb(self, state="readonly"))
            if i == 0:      self.tbAPIs[i].locateFrom(self.tbGameNr, H_RIGHT, V_COPY_TOP)
            elif i == 1:    self.tbAPIs[i].locateFrom(self.tbGameNr.label, H_COPY_LEFT, V_BOTTOM)
            else:           self.tbAPIs[i].locateFrom(self.tbAPIs[i - 1].label, H_COPY_LEFT, V_BOTTOM)
            self.tbAPIs[i].width = 310 if i == 0 else 500
            self.tbAPIs[i].addLabel(["          Game link:", "Gamelog API:", "Game settings API:", "Map API:"][i])

        self.tbPaste = TbM(self)
        self.tbPaste.addLabel(TB_PASTE_LABEL, 10, False, 600)
        self.tbPaste.label.locateFrom(self.tbAPIs[3].label, H_COPY_LEFT, V_BOTTOM)
        self.tbPaste.locateFrom(self.tbPaste.label, H_COPY_LEFT, V_BOTTOM)
        self.tbPaste.height = main.HEIGHT - self.tbPaste.y - 35
        self.tbPaste.width = main.WIDTH - self.tbPaste.x - 15
        self.tbPaste.onChange = self.updateData

    def updateAPILinks(self, sv):
        self.tbPaste.label.text = TB_PASTE_LABEL
        try: int(sv.get())
        except ValueError: return
        for tb in self.tbAPIs:
            tb.configure(state="normal")
        self.tbAPIs[0].value = "http://dominating12.com/?cmd=" + sv.get()
        self.tbAPIs[1].value = "http://dominating12.com/lib/ajax/api/log-info.php?game_id=" + sv.get()
        self.tbAPIs[2].value = "http://dominating12.com/lib/ajax/api/game-info.php?game_id=" + sv.get()
        self.tbAPIs[3].value = "http://dominating12.com/lib/ajax/api/map-info.php?map_id=?"
        for tb in self.tbAPIs:
            tb.configure(state="readonly")

    def updateData(self, event):
        self.tbPaste.label.text = TB_PASTE_LABEL
        try:
            s = self.tbPaste.value.split('\n')
            if len(s) < 3: # The tkinter text widget adds a newline, so <3 instead of <2 .... I think
                return

            if s[0][:3] == 'LOG':
                for i in range(1, len(s)):
                    self.log.addLog(s[i])
                self.tbPaste.label.text = TB_PASTE_LABEL + '(Log data received)'

            elif s[0][:4] == 'GAME':
                self.game.initFromString(s[1])
                for i in range(2, len(s)):
                    self.game.addPlayer(s[i])
                self.tbPaste.label.text = TB_PASTE_LABEL + '(Game data received)'
        except:
                self.tbPaste.label.text = TB_PASTE_LABEL + '(Error)'


if __name__ == '__main__':
    import main
    main.main()
