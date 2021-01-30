import os
import sys
import ctypes
import math
from sdl2 import *
from sdl2.sdlimage import *
from map import Map


class State:
    def __init__(self):
        self.tex = {}
        self.window = None
        self.renderer = None
        self.running = True
        self.map = None
        self.map_x_offset = 50
        self.map_y_offset = 75
        self.tex_x_size = 128
        self.tex_y_size = 128
        self.tex_x_displace = 70
        self.tex_y_displace = 128


_gb = State()


def game_init():
    SDL_Init(SDL_INIT_VIDEO)
    _gb.window = SDL_CreateWindow(
        b'Hello World',
        SDL_WINDOWPOS_CENTERED,
        SDL_WINDOWPOS_CENTERED,
        1200,
        900,
        SDL_WINDOW_SHOWN
    )
    _gb.renderer = SDL_CreateRenderer(_gb.window, -1, SDL_RENDERER_ACCELERATED | SDL_RENDERER_PRESENTVSYNC)
    textures_init()


def game_term():
    textures_term()
    SDL_DestroyRenderer(_gb.renderer)
    SDL_DestroyWindow(_gb.window)
    SDL_Quit()


def textures_init():
    for f in os.listdir('resources'):
        img = IMG_Load(bytes('resources/' + f, 'UTF8'))
        _gb.tex[f.split('.')[0]] = SDL_CreateTextureFromSurface(_gb.renderer, img)
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
    SDL_RenderCopy(_gb.renderer, _gb.tex['bg'], None, None)
    for x in range(len(_gb.map.map)):
        for y in range(len(_gb.map.map[0])):
            t = _gb.map.map[x][y]
            if not t.active: continue
            tx = _gb.tex['triangle01'] if t.coloured else _gb.tex['triangle05']
            f = x%2
            SDL_RenderCopyEx(
                _gb.renderer,
                tx,
                None,
                SDL_Rect(
                    x*_gb.tex_x_displace + _gb.map_x_offset + y*_gb.tex_x_displace,
                    y*_gb.tex_y_displace + _gb.map_y_offset,
                    _gb.tex_x_size,
                    _gb.tex_y_size
                ),
                0 if (f == 1) else 180,
                None,
                SDL_FLIP_NONE
            )
    SDL_RenderPresent(_gb.renderer)


def dist(tx, ty, mx, my):
    return math.sqrt((mx - tx)**2 + (my - ty)**2)


def input_handle(event):
    mx = event.motion.x
    my = event.motion.y
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
        while SDL_PollEvent(ctypes.byref(event)) != 0:
            if event.type == SDL_QUIT:
                _gb.running = False
                break
            elif event.type == SDL_KEYDOWN:
                if event.key.keysym.sym == SDLK_ESCAPE:
                    _gb.running = False
                    break
            elif event.type == SDL_MOUSEBUTTONDOWN:
                input_handle(event)
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