import ctypes
import time
from sdl2 import *
from render import *
from global_variables import _gb
from tmath import *


def mouse_button_down(event):
    mx = event.motion.x
    my = event.motion.y
    jmp = False
    for x in range(int(len(_gb.map.map)/2) + 10):
        for y in range(len(_gb.map.map[0]) + 10):
            tx = x*2*_gb.tex_x_displace + _gb.map_x_offset + y*_gb.tex_x_displace
            ty = y*_gb.tex_y_displace + _gb.map_y_offset
            if dist(tx, ty, mx, my) < 80:
                _gb.line_draw = True
                _gb.line_coord_x = x
                _gb.line_coord_y = y
                _gb.line_orientation = 0
                _gb.line_start_x = int(tx)
                _gb.line_start_y = int(ty)
                _gb.line_end_x = _gb.line_start_x + 2*_gb.tex_x_displace
                _gb.line_end_y = _gb.line_start_y
                jmp = True
                break
        if jmp: break


def corrected_coord(x, y):
    return x + y


def mouse_button_up(event):
    _gb.line_draw = False
    if _gb.line_orientation >= 0:
        if (_gb.line_orientation == 0) or (_gb.line_orientation == 3):
            _gb.map.line(0, _gb.line_coord_y, _gb.line_orientation == 3)
        elif (_gb.line_orientation == 1) or (_gb.line_orientation == 4):            
            _gb.map.line(1, corrected_coord(_gb.line_coord_x, _gb.line_coord_y), _gb.line_orientation == 1)
        elif (_gb.line_orientation == 2) or (_gb.line_orientation == 5):
            _gb.map.line(2, _gb.line_coord_x, _gb.line_orientation == 2)


def mouse_motion(event):
    if not _gb.line_draw: return
    mx = event.motion.x
    my = event.motion.y
    jmp = False
    for x in range(int(len(_gb.map.map)/2) + 10):
        for y in range(len(_gb.map.map[0]) + 10):
            tx = int(x*2*_gb.tex_x_displace + _gb.map_x_offset + y*_gb.tex_x_displace)
            ty = int(y*_gb.tex_y_displace + _gb.map_y_offset)
            if (dist(tx, ty, mx, my) < 80) and check_60(_gb.line_start_x,_gb.line_start_y,tx,ty):
                _gb.line_orientation = orientation(_gb.line_start_x,_gb.line_start_y,tx,ty)
                _gb.line_end_x = tx
                _gb.line_end_y = ty
                break
        if jmp: break
    if (_gb.line_start_x == _gb.line_end_x) and (_gb.line_start_y == _gb.line_end_y):
        _gb.line_end_x = _gb.line_start_x + 2*_gb.tex_x_displace


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
                mouse_button_down(event)
                # After a mouse click we might've solved the level, see if we should progress to next
                if(_gb.map.validate()):
                    _gb.map = _gb.levels.getNextLevel()
                # And just in case something has changed on screen, render everything
                map_render()
                break
            elif event.type == SDL_MOUSEBUTTONUP:
                mouse_button_up(event)
                # After a mouse click we might've solved the level, see if we should progress to next
                if(_gb.map.validate()):
                    # Successfully finished map; render map last time with the solution, and then                    
                    map_render()
                    text_render_naive(_gb.finished_text_x, _gb.finished_text_y, _gb.finished_text)
                    SDL_RenderPresent(_gb.renderer)
                    time.sleep(_gb.finished_sleep_time)
                    _gb.levels.runMapifyList() # Re-do levels to clear their colour status to original
                    _gb.map = _gb.levels.getNextLevel()
                # And just in case something has changed on screen, render everything
                map_render()
                break
            elif event.type == SDL_MOUSEMOTION:
                mouse_motion(event)
                map_render()
                break

        
