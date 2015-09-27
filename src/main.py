from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from MattyControls import *

import game
import inputData
import log
import logStatistics
import simulation

WIDTH = 750
HEIGHT = 500


class Application(Frame):
    def __init__(self, master=None):
        """The constructor"""
        Frame.__init__(self, master)
        master.title("DXII log tools.")

        # Some objects we need everywhere
        self.log = log.Log()
        self.game = game.Game()

        # The tab widgets
        tabHolder = Notebook(master)
        tabHolder.pack(fill='both', expand='yes')
        inputFrame = inputData.InputData(tabHolder, self.log, self.game)
        tabHolder.add(inputFrame, text='Load game data')
        logStatsFrame = logStatistics.LogStatistics(tabHolder, self.log, self.game)
        tabHolder.add(logStatsFrame, text='Analyse game log')
        # simulationFrame = simulation.Simulation(tabHolder, self.log, self.game)
        # tabHolder.add(simulationFrame, text='Simulation')


def main():
    """The main entrypoint for this application"""
    root = Tk()
    root.geometry("{}x{}".format(WIDTH, HEIGHT))
    app = Application(master=root)
    app.mainloop()

if __name__ == '__main__':
    main()
