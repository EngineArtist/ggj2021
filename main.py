import os
import sys
import ctypes
from sdl2 import *
from sdl2.sdlimage import *


tex = {}

def load_textures(renderer):
    for f in os.listdir('resources'):
        img = IMG_Load(bytes('resources/' + f, 'UTF8'))
        tex[f.split('.')[0]] = SDL_CreateTextureFromSurface(renderer, img)
        SDL_FreeSurface(img)


def free_textures():
    for v in tex.values():
        SDL_DestroyTexture(v)


def main():
    SDL_Init(SDL_INIT_VIDEO)
    window = SDL_CreateWindow(
        b'Hello World',
        SDL_WINDOWPOS_CENTERED,
        SDL_WINDOWPOS_CENTERED,
        640,
        480,
        SDL_WINDOW_SHOWN
    )
    windowsurface = SDL_GetWindowSurface(window)

    renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED | SDL_RENDERER_PRESENTVSYNC)
    load_textures(renderer)

    state = False

    SDL_SetRenderDrawColor(renderer, 255, 255, 255, 255)
    SDL_RenderClear(renderer)
    SDL_RenderCopy(renderer, tex['test'], None, SDL_Rect(0, 0, 128, 128))
    SDL_RenderPresent(renderer)

    running = True
    event = SDL_Event()
    while running:
        while SDL_PollEvent(ctypes.byref(event)) != 0:
            if event.type == SDL_QUIT:
                running = False
                break
            elif event.type == SDL_KEYDOWN:
                if event.key.keysym.sym == SDLK_ESCAPE:
                    running = False
                    break
            elif event.type == SDL_MOUSEBUTTONDOWN:
                state = not state
                SDL_SetRenderDrawColor(renderer, 255, 255, 255, 255)
                SDL_RenderClear(renderer)
                SDL_RenderCopy(renderer, tex['triangle01'] if state else tex['test'], None, SDL_Rect(0, 0, 128, 128))
                SDL_RenderPresent(renderer)
                break
    
    free_textures()
    SDL_DestroyRenderer(renderer)
    SDL_DestroyWindow(window)
    SDL_Quit()
    return 0


if __name__ == "__main__":
    sys.exit(main())