import tkinter

from tkintermapview import *
from saveMap import *
from imageConverter import *

# Constants
MAX_SIZE = 640

# Function which activates when the export button is clicked
def exportPressed(map):
    saveMap(map.get_position()[1], map.get_position()[0], 200)
    print("Original map saved to 'temp.png'")
    convertImage("temp.png", "map.png")
    print("Converted map saved to 'map.png'")