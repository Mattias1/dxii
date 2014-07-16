from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from MattyControls import *
import textwrap
import main
import log


class LogStatistics(Frame):
    """The frame for the log statistics"""

    def __init__(self, master, log, game):
        frame_init(self, master, True)

        self.log = log
        self.game = game

        self.btnAnalyse = Btn(self, text="Analyse log", command=self.analyse)
        self.btnAnalyse.locateInside(self, H_LEFT, V_TOP)

        self.btnCopy = Btn(self, text="Copy to clipboard", command=self.copy)
        self.btnCopy.width = 120
        self.btnCopy.locateFrom(self.btnAnalyse, H_RIGHT, V_COPY_TOP)

        self.lblStats = []
        for i in range(3):
            self.lblStats.append(Lbl(self, anchor=NW))
            self.lblStats[i].height = 450
            self.lblStats[i].width = 250
            if i == 0: self.lblStats[i].locateFrom(self.btnAnalyse, H_COPY_LEFT, V_BOTTOM)
            else:      self.lblStats[i].locateFrom(self.lblStats[i - 1], H_RIGHT, V_COPY_TOP)

    def copy(self):
        """Copy the log data to clipboard"""
        r = Tk()
        r.withdraw()
        r.clipboard_clear()
        r.clipboard_append("Game " + str(self.game.game_id) + " statistics\n\n")
        for lbl in self.lblStats:
            r.clipboard_append(lbl.text)
        r.destroy()

    def analyse(self):
        """Analyse the log data"""
        # Reset player stats
        for p in self.game.players:
            p.stats = PlayerStats(p)

        # Analyse the log and update the player stats
        for i in range(len(self.log)):
            try:
                l = self.log.getLog(i)                                      # The current log item
                s = self.game.players[l.log_player_id - 1].stats            # The statistics object of the 'acting player'
                sa = self.game.players[l.log_against_player_id - 1].stats   # The statistics object of the 'passive player'
                t = l.log_type                                              # The type of the current log item
            except:
                continue

            if t in { log.ATTACK_SUCCEED, log.ATTACK_STOP_EARLY }:
                # Attack
                s.killed_attack += l.log_num
                s.lost_attack += l.log_num2
                # Defence
                sa.killed_defence += l.log_num2
                sa.lost_defence += l.log_num

            elif t == log.PLACE_TROOPS:
                # Place troops
                s.placed += l.log_num
        self.printStats()

    def printStats(self):
        """Update the statistics label"""
        text = ['' for i in range(len(self.lblStats))]
        for i in range(self.game.nr_of_players):
            text[i % len(self.lblStats)] += self.game.players[i].stats.toString()
        for i in range(len(self.lblStats)):
            self.lblStats[i].text = text[i]


class PlayerStats():
    """The stats for one player"""

    def __init__(self, player):
        self.player = player
        self.killed_attack = 0
        self.lost_attack = 0
        self.killed_defence = 0
        self.lost_defence = 0
        self.conquerors_vs_1 = 0
        self.placed = 0

    def toString(self):
        """Output the statistics in a nicely formatted string"""
        return textwrap.dedent("""\
            {}:
              Total killed in attack: {}
              Total lost in attack: {}
              Total killed in defence: {}
              Total lost in defence: {}
              Total placed: {}\n
              """.format(self.player.player_name, self.killed_attack, self.lost_attack, self.killed_defence, self.lost_defence, self.placed))


if __name__ == '__main__':
    import main
    main.main()
