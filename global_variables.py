from sdl2 import *
from levels import Levels

class State:
    '''
    A class used for storing global variables, including the map.
    '''
    def __init__(self):
        self.tex = {}
        self.window = None
        self.renderer = None
        self.running = True # Whether game is running or not
        self.levels = Levels() # Load all available game maps
        self.map = None # The full state of the map
        self.screen_x = 1200
        self.screen_y = 900
        self.map_x_offset = 50 # Map render offset from the left side of the screen
        self.map_y_offset = 75 # Map render offset from the top of the screen
        self.tex_x_size = 128 # Triangle texture width
        self.tex_y_size = 128 # Triangle texture height
        self.tex_x_displace = 70 # Triangle spacing, horizontal
        self.tex_y_displace = 128 # Triangle spacing, vertical
        self.line_draw = False # Whether or not we are drawing a line
        self.line_start_x = 0
        self.line_start_y = 0
        self.line_end_x = 1200
        self.line_end_y = 900
        self.line_coord_x = 0
        self.line_coord_y = 0
        self.line_orientation = -1
        self.splash_sleep_time = 3 # Sleep time in seconds in initial splash screen
        self.finished_sleep_time = 2 # Sleep time in seconds after a map is successfully solved
        self.finished_text = "success"
        self.finished_text_x = 10
        self.finished_text_y = 10


# An instance of the global state storage
_gb = State()
