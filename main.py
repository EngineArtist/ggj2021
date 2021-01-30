import os
import sys
import ctypes
from sdl2 import *
from sdl2.sdlimage import *


TRI_NULL = 0
TRI_ON   = 1
TRI_OFF  = 2


class State:
    def __init__(self):
        self.tex = {}
        self.window = None
        self.renderer = None
        self.running = True
        self.map_width = 8
        self.map_height = 4
        self.map = [TRI_ON for x in range(self.map_height*self.map_width)]


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


def map_render():
    SDL_RenderCopy(_gb.renderer, _gb.tex['bg'], None, None)
    for i in range(len(_gb.map)):
        t = _gb.map[i]
        if t == TRI_NULL: continue
        t = _gb.tex['triangle01'] if (t == TRI_ON) else _gb.tex['test']
        x = i%_gb.map_width
        f = x%2
        y = int(i/_gb.map_width)
        SDL_RenderCopyEx(_gb.renderer, t, None, SDL_Rect(x*64 + 200 + y*64, y*128 + 200, 128, 128), 0 if (f == 1) else 180, None, SDL_FLIP_NONE)
    SDL_RenderPresent(_gb.renderer)


def input_handle(event):
    pass


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
    map_render()
    game_loop()
    game_term()
    return 0


if __name__ == "__main__":
    sys.exit(main())