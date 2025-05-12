import tkinter

from tkintermapview import *
from saveMap import *

# Constants
MAX_SIZE = 640

# Function which activates when the export button is clicked
def exportPressed(map):
    saveMap(map.get_position()[1], map.get_position()[0])