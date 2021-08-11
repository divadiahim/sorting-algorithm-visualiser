import pygame
pygame.init()
pygame.font.init()
import winsound
from array import array
from time import sleep
from pygame.mixer import Sound, get_init, pre_init
WHITE = (255,255,255)
BLACK = (0,0,0)
GREY = (53,53,53)
BUTTON = (71, 95, 119)
RED = (255,0,0)
WIDTH,HEIGHT = 600,700
GREEN = (0,255,0)
FPS = 144
ROWS = COLS = 100
TOOLBAR_HEIGHT = HEIGHT-WIDTH
PIXEL_SIZE = 6
DRAW_LINES = False
LIST_LEN = 100


BG_COLOR = GREY

# def get_font(size):
#     return pygame.font.sysfont("helvetica",size)