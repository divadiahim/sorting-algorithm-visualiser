import pygame
pygame.init()
pygame.font.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
GREY = (53,53,53)
BUTTON = (71, 95, 119)

WIDTH,HEIGHT = 600,700

FPS = 144
ROWS = COLS = 100
TOOLBAR_HEIGHT = HEIGHT-WIDTH
PIXEL_SIZE = 6
DRAW_LINES = True

BG_COLOR = GREY

# def get_font(size):
#     return pygame.font.sysfont("helvetica",size)