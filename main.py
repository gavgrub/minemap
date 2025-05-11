import tkinter
import tkintermapview

# Function to calculate map dimensions in meters
def getDimensions(zoom_level, map_width_px, map_height_px):
    # Earth's circumference in meters
    EARTH_CIRCUMFERENCE = 40075017
    
    # Calculate the meters per pixel at this zoom level
    meters_per_pixel = EARTH_CIRCUMFERENCE / (TILE_SIZE * (2 ** zoom_level))
    
    # Calculate map dimensions in meters
    map_width_meters = meters_per_pixel * map_width_px
    map_height_meters = meters_per_pixel * map_height_px
    
    return map_width_meters, map_height_meters

# Setup the window
def setup():
    window = tkinter.Tk()

    # Setup the map widget
    map = tkintermapview.TkinterMapView(window, width=600, height=600)
    map.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
    map.place(relx=1.0, rely=0.5, anchor=tkinter.E)

    # Setup the window itself
    window.geometry("1000x600")
    window.title("MineMap")
    window.resizable(False, False)
    window.mainloop()

setup()