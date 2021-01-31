from global_variables import _gb
from sdl2 import *


def triangle_render(x, y, f, coloured):
    '''
    Render a single triangle on screen
    '''
    # SDL_RenderCopy and SDL_RenderCopyEx(tended) are functions for rendering a texture on screen.
    # Here we render Triangle (x, y) using the designated SDL_Renderer stored in _gb.renderer
    # using the SDL_Texture tx.
    SDL_RenderCopyEx(
        _gb.renderer,
        _gb.tex['triangle01'] if coloured else _gb.tex['triangle05'],
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


def line_render(start_x, start_y, end_x, end_y):
    SDL_SetRenderDrawColor(_gb.renderer, 80, 80, 80, 100)
    SDL_SetRenderDrawBlendMode(_gb.renderer, SDL_BLENDMODE_BLEND)
    SDL_RenderDrawLine(
        _gb.renderer,
        start_x,
        start_y,
        end_x,
        end_y
    )


def flip_line_render(start_x, start_y, end_x, end_y):
    dx = end_x - start_x
    dy = end_y - start_y
    start_x -= dx*100
    start_y -= dy*100
    end_x += dx*100
    end_y += dy*100
    line_render(start_x, start_y, end_x, end_y)
    line_render(start_x + 1, start_y, end_x + 1, end_y)
    line_render(start_x, start_y + 1, end_x, end_y + 1)


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
            triangle_render(x, y, f, t.coloured)
    # If the player is dragging a line, draw it
    if _gb.line_draw:
        SDL_SetRenderDrawColor(_gb.renderer, 80, 80, 80, 100)
        SDL_SetRenderDrawBlendMode(_gb.renderer, SDL_BLENDMODE_BLEND)
        flip_line_render(
            _gb.line_start_x,
            _gb.line_start_y,
            _gb.line_end_x,
            _gb.line_end_y,
        )
    # Finally call SDL_RenderPresent on an SDL_Renderer to display the new frame on screen.
    SDL_RenderPresent(_gb.renderer)

def target_render():
    '''
    Render the target of desired white triangles in final solution
    '''
    numnames = ['num_0', 'num_1', 'num_2', 'num_3', 'num_4', 'num_5', 'num_6', 'num_7', 'num_8', 'num_9']
    SDL_RenderCopy(_gb.renderer,
                   _gb.tex[numnames[_gb.map.getTarget()]],
                           None,
                           SDL_Rect(
                               _gb.target_x,
                               _gb.target_y,
                               62, # Hard coded size of the num textures
                               62
                            ),
                           0,
                           None,
                           SDL_FLIP_NONE
                    )
    SDL_RenderPresent(_gb.renderer)    
