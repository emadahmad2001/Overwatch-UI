from tkinter import *
from tkinter import ttk
import tkinter as tk
from Pages import PageOne
from apicollect import Overwatch


class FirstGUI(tk.Tk):
    """
    This is pertaining to Overwatch only, Remember that in the apicollect.py file,
    Overwatch API requires you to put in platform, region and battle id of the player.
    """

    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("720x360")
        self.title("Statistical Tracker for:")
        self._frame = None
        self.change_frame(PageOne)
        self.all_players = []
        self.game_filters = {}
        self.displayed_stats = []
        self.compared_stats = []
        self.game_mode = None

    def change_frame(self, change_frame, *player_info):
        """
        Needed to handle frame changes so that the user can move from one window to the other
        """
        new_frame = change_frame(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


if __name__ == "__main__":
    """
    Runs the application
    """
    app = FirstGUI()
    app.mainloop()
