from typing import NewType
from utils.array_init import init_random_array
from utils.button import Button
from pygame import Color, init
from utils import *

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Sorting algorithm visualiser")
img_run = pygame.image.load("img/play.png").convert_alpha()


def init_grid(rows,cols,color):
    grid=[]
    for i in range(rows):
        grid.append([])
        for j in range(cols):
            grid[i].append(color)

    return grid       

def draw_grid(win,grid):
    for i,row in enumerate(grid):
        for j, pixel in enumerate(row):
            pygame.draw.rect(win,pixel,(j*PIXEL_SIZE,i*PIXEL_SIZE,PIXEL_SIZE,PIXEL_SIZE))          

    #draw a grid around the pixels
    if(DRAW_LINES):
        for i in range(ROWS+1):
            pygame.draw.line(win,BLACK,(0,i*PIXEL_SIZE),(WIDTH,i*PIXEL_SIZE))

        for j in range(COLS+1):
            pygame.draw.line(win,BLACK,(j*PIXEL_SIZE,0),(j*PIXEL_SIZE,HEIGHT-TOOLBAR_HEIGHT))


def draw(win,grid):
    win.fill(BG_COLOR)
    draw_grid(win,grid)
    if(run_button.draw(WIN)):
        init_random_array(grid)
    create_button.draw(WIN)    
    pygame.display.update()

running = True #create the running var
clock = pygame.time.Clock() #create the game clock so that it`s running at capped fps
grid = init_grid(ROWS,COLS,WHITE)#create the grid of pixels to be filled 


# create button instances #
run_button=button.Button_img(img_run,10,615,0.15,None)
create_button=button.Button('create',200,40,(400,630))


while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    draw(WIN,grid)
    # grid[0][6]=BLACK
    
pygame.quit()            