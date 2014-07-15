from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from MattyControls import *
import logStatistics
import inputData
import log


WIDTH = 750
HEIGHT = 500


class Application(Frame):
    def __init__(self, master=None):
        """The constructor"""
        Frame.__init__(self, master)
        master.title("Test")

        # Some objects we need everywhere
        self.log = log.Log()

        # The tab widgets
        tabHolder = Notebook(master)
        tabHolder.pack(fill='both', expand='yes')
        inputFrame = inputData.InputData(tabHolder, self.log)
        tabHolder.add(inputFrame, text='Input data')
        logStatsFrame = logStatistics.LogStatistics(tabHolder, self.log)
        tabHolder.add(logStatsFrame, text='Analyse game log')


def main():
    """The main entrypoint for this application"""
    root = Tk()
    root.geometry("{}x{}".format(WIDTH, HEIGHT))
    app = Application(master=root)
    app.mainloop()

if __name__ == '__main__':
    main()
