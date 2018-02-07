import tkinter as tk
from tkinter import *
import os
import platform
if platform.system == "Windows":
    os.environ['SDL_VIDEODRIVER'] = 'windib'

class Embed(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        # creates embed frame for pygame window using tkinter
        tk.Tk.__init__(self, *args, **kwargs)
        embed = tk.Frame(self, width=80, height=80)
        embed.grid(columnspan=(600), rowspan=500)  # Adds grid
        embed.pack(side=LEFT)  # packs window to the left
        os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
        


