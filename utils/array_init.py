from .settings import *
import random
import time

class init_random_array:
    def __init__(self,grid):
        self.grid=grid
        
    def init_random_array(self):
        self.randomlist = []
        for i in range (0,LIST_LEN):
            n = random.randint(1,100)
            self.randomlist.append(n)
        self.randomlist_len=len(self.randomlist)
        return self.randomlist 
    def fiil_grid(self):
        pixels=[]       
        for z in range(self.randomlist_len):
            pygame.time.delay(2)
            curr=self.randomlist[z]
            # print(curr)
            # print(z)
            for j in range(curr):
                pixels.append(tuple((j,z)))
                # self.grid[j][z]=BLACK
            pygame.display.update()        
        return pixels           
    # def fiil_grid_test(self,j,z):
    #     self.grid[j].append((BLACK))
    #     return  
    # def fiil_grid_recc(self):
    #     if LIST_LEN<self.z:
    #         return 0 
    #     self.grid[]       
    #     self.fill_grid_recc(self.randomlist[self.z+1])    
                
            
              
def reset_array(grid):
    for i in range(ROWS):
        for j in range(COLS):
            grid[i][j]=WHITE     
            


