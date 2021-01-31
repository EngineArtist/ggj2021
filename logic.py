import math
import ctypes
from sdl2 import *
from render import *
from global_variables import _gb


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
                # After a mouse click we might've solved the level, see if we should progress to next
                if(_gb.map.validate()):
                    _gb.map = _gb.levels.getNextLevel()
                # And just in case something has changed on screen, render everything
                map_render()
                target_render()
                break
        
