from .settings import *
import random

def init_random_array(grid):
    randomlist = []
    for i in range (0,100):
        n = random.randint(1,30)
        randomlist.append(n)
    print(randomlist)
    for z in range(len(randomlist)):
        curr=randomlist[z]
        # print(curr)
        print(z)
        for j in range(curr):
            grid[j][z]=BLACK  
           
            


