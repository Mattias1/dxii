from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from MattyControls import *
import urllib.request
import main
import log


class InputData(Frame):
    """The frame for the input (game log, game info, map info)"""

    def __init__(self, master, log, game):
        frame_init(self, master, True)
        self.log = log
        self.game = game
        self.initControls()

    def initControls(self):
        """Create all the buttons and other widgets"""
        self.tbGameNr = Tb(self)
        self.tbGameNr.locateInside(self, H_LEFT, V_TOP)
        self.tbGameNr.addLabel("Game number:")

        self.btnGetData = Btn(self, text="Get data", command=self.getFromWeb)
        self.btnGetData.locateFrom(self.tbGameNr, H_COPY_LEFT, V_BOTTOM)
        self.btnGetData.x -= self.btnGetData.width // 2

        self.lblFeedback = Lbl(self, text="No data present")
        self.lblFeedback.locateFrom(self.btnGetData, H_CENTER, V_BOTTOM)
        self.lblFeedback.width = 200
        self.lblFeedback.x = 10

    def getFromWeb(self):
        """Get the data from the D12 API's"""
        try:
            game_id = int(self.tbGameNr.value)
        except:
            self.lblFeedback.text = "Error: Invalid game id"
            return

        urls = ["http://dominating12.com/lib/ajax/api/log-info.php?game_id=" + str(game_id), 
                "http://dominating12.com/lib/ajax/api/game-info.php?game_id=" + str(game_id)]
        #       "http://dominating12.com/lib/ajax/api/map-info.php?map_id=?"
        for url in urls:
            data = self.ajaxCall(url)
            self.updateData(data)

    def ajaxCall(self, url):
        """Return the contents of a given URL"""
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        return response.read().decode('utf-8')

    def updateData(self, data):
        self.lblFeedback.text = "Parsing data..."
        try:
            s = data.split('<br />')
            if len(s) < 2:
                return

            if s[0][:3] == 'LOG':
                for i in range(1, len(s)):
                    self.log.addLog(s[i])
                self.lblFeedback.text = "Parsing data... (log done)"

            elif s[0][:4] == 'GAME':
                self.game.initFromString(s[1])
                for i in range(2, len(s)):
                    self.game.addPlayer(s[i])
                self.lblFeedback.text = "Parsing data... (game done)"
        except:
            self.lblFeedback.text = "Error: can't read data"
        self.lblFeedback.text = "Data received succesfully"


if __name__ == '__main__':
    import main
    main.main()
