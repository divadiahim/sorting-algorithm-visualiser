from .settings import *
import random
import winsound

class init_random_array:
    def __init__(self,grid,win):
        self.grid=grid
        self.win=win

    def init_random_array(self):
        self.randomlist = []
        for i in range (0,LIST_LEN):
            n = random.randint(1,100)
            self.randomlist.append(n)
        self.randomlist_len=len(self.randomlist)
        return self.randomlist 

    def fiil_grid(self):
        reset_array(self.win,self.grid)      
        for z in range(self.randomlist_len):
            #pygame.time.delay(1)
            curr=self.randomlist[z]
            # print(curr)
            # print(z)
            # for _ in range(curr):
                #pixels.append(tuple((j,z)))
                # self.grid[j][z]=BLACK
                
            pygame.draw.rect(self.win,BLACK,(z*PIXEL_SIZE,0,PIXEL_SIZE,PIXEL_SIZE*curr))               
            # pygame.display.update()
            # 
            # winsound.Beep(curr*15+137, 40)
     
    
              
def reset_array(win,grid):
    for i,row in enumerate(grid):
        for j, pixel in enumerate(row):
            pygame.draw.rect(win,pixel,(j*PIXEL_SIZE,i*PIXEL_SIZE,PIXEL_SIZE,PIXEL_SIZE))
            


