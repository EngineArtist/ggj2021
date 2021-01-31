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
        self.line_rect = SDL_Rect(0, 0, 0, 0) # The starting and ending points for the line        


# An instance of the global state storage
_gb = State()
