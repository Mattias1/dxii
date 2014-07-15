from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from MattyControls import *


class LogStatistics(Frame):
    """The frame for the log statistics"""

    def __init__(self, master, log):
        frame_init(self, master, True)
        self.createWidgets()

    def createWidgets(self):
        """Create all the buttons and other widgets"""
        self.btnAnalyse = Btn(self, text="Analyse log", command=self.analyse)
        self.btnAnalyse.locateInside(self, H_LEFT, V_TOP)

    def analyse(self):
        """Analyse the log data"""
        for i in range(len(self.log)):
            if self.log.getLog(i).log_type in { ATTACK_STOP_EARLY, ATTACK_SUCCEED }:
                pass


if __name__ == '__main__':
    import main
    main.main()
