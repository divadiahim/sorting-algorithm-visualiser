from .settings import *
import random

def init_random_array(grid):
    randomlist = []
    for i in range (0,100):
        n = random.randint(1,100)
        randomlist.append(n)
    print(randomlist)
    for z in range(len(randomlist)):
        curr=randomlist[z]
        # print(curr)
        print(z)
        for j in range(curr):
            grid[j][z]=BLACK

def reset_array(grid):
    for i in range(ROWS):
        for j in range(COLS):
            grid[i][j]=WHITE     
            


