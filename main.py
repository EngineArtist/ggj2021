import os
import sys
import ctypes
import math
from sdl2 import *
from sdl2.sdlimage import *
from map import Map


class State:
    '''
    A class used for storing global variables, including the map.
    '''
    def __init__(self):
        self.tex = {}
        self.window = None
        self.renderer = None
        self.running = True # Whether game is running or not
        self.map = None # The full state of the map
        self.screen_x = 1200
        self.screen_y = 900
        self.map_x_offset = 50 # Map render offset from the left side of the screen
        self.map_y_offset = 75 # Map render offset from the top of the screen
        self.tex_x_size = 128 # Triangle texture width
        self.tex_y_size = 128 # Triangle texture height
        self.tex_x_displace = 70 # Triangle spacing, horizontal
        self.tex_y_displace = 128 # Triangle spacing, vertical


# This is where all the global variables are
_gb = State()


def game_init():
    '''
    Initialization of SDL, the window, the renderer and textures.
    A call to game_term is required at the end of execution to
    free all allocated resources.
    '''
    # All calls prefixed by SDL_ are actual calls to the SDL-library, for which you can find
    # documentation here: https://www.libsdl.org/
    # The SDL-api reference is here: https://wiki.libsdl.org/APIByCategory
    SDL_Init(SDL_INIT_VIDEO)
    _gb.window = SDL_CreateWindow(
        b'Trilemma', # Since we're calling straight into a C-api, we need to pass strings as bytes
        SDL_WINDOWPOS_CENTERED,
        SDL_WINDOWPOS_CENTERED,
        _gb.screen_x,
        _gb.screen_y,
        SDL_WINDOW_SHOWN
    )

    # A renderer is something that can perform a range of drawing operations on a window framebuffer.
    # An SDL_Renderer interfaces directly with the GPU, so hardware acceleration can be used if enabled.
    # Renderers can render on screen, but also onto textures.
    # More documentation on SDL_Renderers can be found here: https://wiki.libsdl.org/CategoryRender
    # Note: see the SDL_RenderDrawLine -function for drawing lines, and other SDL_Render* -functions
    # for performing other drawing operations.
    _gb.renderer = SDL_CreateRenderer(_gb.window, -1, SDL_RENDERER_ACCELERATED | SDL_RENDERER_PRESENTVSYNC)
    textures_init()


def game_term():
    textures_term()
    SDL_DestroyRenderer(_gb.renderer)
    SDL_DestroyWindow(_gb.window)
    SDL_Quit()


def textures_init():
    '''
    Load all png-files in the resources-directory and make textures from each one.
    Store the loaded textures in a dictionary in _gb with their filenames as keys (without file extentions).
    For example, resources/test.png would be stored as a texture in _gb.tex['test'].
    '''
    for f in os.listdir('resources'):
        img = IMG_Load(bytes('resources/' + f, 'UTF8')) # This is an extension to SDL called SDL-image.
        # SDL-image -functions are prefixed with IMG_, and also require strings to be passed as bytes.

        # So IMG_Load returns what is called an SDL_Surface, which is a buffer of pixels.
        # SDL_CreateTextureFromSurface takes in an SDL_Surface and creates an SDL_Texture.
        # What's the difference between SDL_Surface and SDL_Texture? Internal data format and memory
        # location. An SDL_Texture is most probably a piece of memory located on the GPU, whereas
        # an SDL_Surface is a piece of memory in RAM. Also, an SDL_Renderer renders SDL_Textures
        # really efficiently, making use of GPU acceleration if enabled.
        _gb.tex[f.split('.')[0]] = SDL_CreateTextureFromSurface(_gb.renderer, img)

        # Since we don't need the SDL_Surface after the SDL_Texture has been created, free it.
        SDL_FreeSurface(img)


def textures_term():
    for v in _gb.tex.values():
        SDL_DestroyTexture(v)


def map_read():
    _gb.map = Map(5, 10, 6)
    for x in range(len(_gb.map.map)):
        for y in range(len(_gb.map.map[0])):
            _gb.map.setActiveStateAt(x, y, True)


def map_render():
    '''
    Render the currently loaded Map on screen, along with the background image.
    '''
    # Render the background image
    SDL_RenderCopy(_gb.renderer, _gb.tex['bg'], None, None)
    for x in range(len(_gb.map.map)):
        for y in range(len(_gb.map.map[0])):
            t = _gb.map.map[x][y]
            if not t.active: continue
            tx = _gb.tex['triangle01'] if t.coloured else _gb.tex['triangle05']
            f = x%2
            # SDL_RenderCopy and SDL_RenderCopyEx(tended) are functions for rendering a texture on screen.
            # Here we render Triangle (x, y) using the designated SDL_Renderer stored in _gb.renderer
            # using the SDL_Texture tx.
            SDL_RenderCopyEx(
                _gb.renderer,
                tx,
                None,
                SDL_Rect( # Position and size of texture on screen
                    x*_gb.tex_x_displace + _gb.map_x_offset + y*_gb.tex_x_displace,
                    y*_gb.tex_y_displace + _gb.map_y_offset,
                    _gb.tex_x_size,
                    _gb.tex_y_size
                ),
                0 if (f == 1) else 180, # Every other triangle needs to be flipped 180 degrees
                None,
                SDL_FLIP_NONE # This is if you want to mirror the texture horizontally or vertically (we don't)
            )
    # Finally call SDL_RenderPresent on an SDL_Renderer to display the new frame on screen.
    SDL_RenderPresent(_gb.renderer)


def dist(tx, ty, mx, my):
    return math.sqrt((mx - tx)**2 + (my - ty)**2)


def input_handle(event):
    mx = event.motion.x
    my = event.motion.y
    # If a triangle is clicked, toggle its state between unused/uncolored/colored
    for x in range(len(_gb.map.map)):
        for y in range(len(_gb.map.map[0])):
            tx = x*_gb.tex_x_displace + _gb.map_x_offset + y*_gb.tex_x_displace + _gb.tex_x_size/2
            ty = y*_gb.tex_y_displace + _gb.map_y_offset + _gb.tex_y_size/2
            if dist(tx, ty, mx, my) < 35:
                if not _gb.map.map[x][y].active:
                    _gb.map.map[x][y].setActive()
                    _gb.map.map[x][y].setUncoloured()
                else:
                    if not _gb.map.map[x][y].coloured:
                        _gb.map.map[x][y].setColoured()
                    else:
                        _gb.map.map[x][y].setInactive()


def game_loop():
    event = SDL_Event()
    while _gb.running:
        # Read all input events and handle each one accordingly
        while SDL_PollEvent(ctypes.byref(event)) != 0:
            # If the user presses the X on the window, exit program
            if event.type == SDL_QUIT:
                _gb.running = False
                break
            elif event.type == SDL_KEYDOWN: # Also exit if ESC is pressed
                if event.key.keysym.sym == SDLK_ESCAPE:
                    _gb.running = False
                    break
            elif event.type == SDL_MOUSEBUTTONDOWN:
                # If the player presses a mouse button, handle the input
                input_handle(event)
                # And just in case something has changed on screen, render everything
                map_render()
                break


def main():
    global _gb
    game_init()
    map_read()
    map_render()
    game_loop()
    game_term()
    return 0


if __name__ == "__main__":
    sys.exit(main())