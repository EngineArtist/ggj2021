import time
from global_variables import _gb
from sdl2 import *
from tmath import *


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
    SDL_SetRenderDrawBlendMode(_gb.renderer, SDL_BLENDMODE_BLEND)
    SDL_SetRenderDrawColor(_gb.renderer, 100, 90, 80, 70)
    SDL_RenderDrawLine(
        _gb.renderer,
        int(start_x),
        int(start_y),
        int(end_x),
        int(end_y)
    )


def flip_line_render(start_x, start_y, end_x, end_y):
    sx = start_x
    sy = start_y
    dx = end_x - start_x
    dy = end_y - start_y
    nx = -dy
    ny = dx
    mn = magn(nx, ny)
    nx /= mn
    ny /= mn
    nx *= 75
    ny *= 75
    start_x -= dx*100
    start_y -= dy*100
    end_x += dx*100
    end_y += dy*100
    line_render(sx, sy, sx + nx, sy + ny)
    line_render(sx + 1, sy, sx + nx + 1, sy + ny)
    line_render(sx, sy + 1, sx + nx, sy + ny + 1)
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
        flip_line_render(
            _gb.line_start_x,
            _gb.line_start_y,
            _gb.line_end_x,
            _gb.line_end_y,
        )
    # Naive UI drawn on bottom-left
    number_render_naive(500, 750, _gb.map.getFlipcount())
    text_render_naive(10, 750, "flips")
    number_render_naive(500, 800, _gb.map.getLinecount())
    text_render_naive(10, 800, "lines")
    number_render_naive(500, 850, _gb.map.getTarget())
    text_render_naive(10, 850, "target")
    # Finally call SDL_RenderPresent on an SDL_Renderer to display the new frame on screen.
    SDL_RenderPresent(_gb.renderer)

def number_render_naive(x, y, number):
    '''
    Render the target of desired white triangles in final solution
    '''
    # Note: Quick and dirty hard-coded locations into serve as the user interface
    numnames = ['num_0', 'num_1', 'num_2', 'num_3', 'num_4', 'num_5', 'num_6', 'num_7', 'num_8', 'num_9']
    for index in range(len(list(str(number)))):
        SDL_RenderCopy(_gb.renderer,
                   _gb.tex[numnames[int(list(str(number))[index])]],
                           None,
                           SDL_Rect(
                               x + index*60,
                               y,
                               62, # Hard coded size of the num textures
                               62
                            ),
                           0,
                           None,
                           SDL_FLIP_NONE
                    )

def text_render_naive(x, y, text):
    '''
    Naive rendering of text using 62x62 sprites
    '''
    letnames = ['let_a', 'let_b', 'let_c', 'let_d', 'let_e', 'let_f', 'let_g', 'let_h', 'let_i', 'let_j', 'let_k', 'let_l', 'let_m', 'let_n', 'let_o', 'let_p', 'let_q', 'let_r', 'let_s', 'let_t', 'let_u', 'let_v', 'let_w', 'let_x', 'let_y', 'let_z']
    for index in range(len(list(text))):
        SDL_RenderCopy(_gb.renderer,
            # 97th element in ordered characters is 'a'                       
            _gb.tex[letnames[ord(list(text)[index])-97]],
                None,
                    SDL_Rect(
                    x + index*60,
                    y,
                    62, # Hard coded size of the num textures
                    62
                    ),
                0,
                None,
                SDL_FLIP_NONE
        )

def splash_render_naive(sleeptime):
    '''
    Function that renders a naive splash screen and sleeps for a short period of time
    '''
    SDL_RenderCopy(_gb.renderer,
        _gb.tex["trilemma_cover"],
        None,
        SDL_Rect(
            0,
            0,
            #1200,
            1920,
            #900
            1080
            ),
        0,
        None,
        SDL_FLIP_NONE
    )    
    SDL_RenderPresent(_gb.renderer)
    time.sleep(sleeptime)
