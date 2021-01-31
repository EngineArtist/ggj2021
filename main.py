import os
import sys
import ctypes
import math
from sdl2 import *
from sdl2.sdlimage import *
from map import Map
from render import *
from logic import *
from levels import Levels
from global_variables import _gb


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
    _gb.renderer = SDL_CreateRenderer(_gb.window, -1, SDL_RENDERER_ACCELERATED)
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
    #_gb.map = Map(5, 10, 6)
    # This is now read at initialization
    #for x in range(len(_gb.map.map)):
    #    for y in range(len(_gb.map.map[0])):
    #        _gb.map.setActiveStateAt(x, y, True)
    # Read first map upon launch
    _gb.map = _gb.levels.getCurrentLevel()


def main():
    game_init()
    map_read()
    map_render()
    game_loop()
    game_term()
    return 0


if __name__ == "__main__":
    sys.exit(main())
