import tkinter
import math

from tkintermapview import *
from controllers import *

# Setup the window
def setup():
    window = tkinter.Tk()

    # Create a frame for the information contained in the sidebar
    sideBar = tkinter.Frame(window, width=400)
    sideBar.pack(side=tkinter.LEFT, fill=tkinter.Y, padx=10, pady=10)

    # Setup the map widget
    map = TkinterMapView(window, width=600, height=600)
    map.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
    map.place(relx=1.0, rely=0.5, anchor=tkinter.E)

    # Setup the export button
    button = tkinter.Button(sideBar, text="Export", command=lambda: exportPressed(map))
    button.pack()

    # Setup the window itself
    window.geometry("1000x600")
    window.title("MineMap")
    window.resizable(False, False)
    window.mainloop()

setup()