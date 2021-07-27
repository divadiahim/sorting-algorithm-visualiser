from utils import sound
from .settings import *
def bubble_sort(win,randomlist):
    pre_init(44100, -16, 1, 1024)
    n = len(randomlist)
    # Traverse through all randomlistay elements
    for i in range(n-1):
    # range(n) also work but outer loop will repeat one time more than needed.
          
        # Last i elements are already in place
       
        for j in range(0, n-i-1):
            # 
            # traverse the randomlistay from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            # 
            pygame.event.pump()
            curr=randomlist[j]
            curr_1=randomlist[j+1]
            pygame.draw.rect(win,RED,(j*PIXEL_SIZE,0,PIXEL_SIZE,PIXEL_SIZE*curr))
            pygame.draw.rect(win,RED,((j+1)*PIXEL_SIZE,0,PIXEL_SIZE,PIXEL_SIZE*curr_1))
            pygame.display.update()
            # pygame.time.delay(500)
            # winsound.Beep(curr*15+137, 10)
            sound.Note(curr_1*10).play(-1)
            # pygame.draw.rect(win,BLACK,(j*PIXEL_SIZE,0,PIXEL_SIZE,PIXEL_SIZE*curr))
            # pygame.draw.rect(win,BLACK,((j+1)*PIXEL_SIZE,0,PIXEL_SIZE,PIXEL_SIZE*curr_1))
            if randomlist[j] > randomlist[j + 1] :
                pygame.draw.rect(win,WHITE,((j+1)*PIXEL_SIZE,0,PIXEL_SIZE,PIXEL_SIZE*100))
                pygame.draw.rect(win,WHITE,(j*PIXEL_SIZE,0,PIXEL_SIZE,PIXEL_SIZE*100))
                pygame.display.update()
                # pygame.time.delay(1)
                pygame.draw.rect(win,BLACK,((j+1)*PIXEL_SIZE,0,PIXEL_SIZE,PIXEL_SIZE*curr))
                pygame.draw.rect(win,BLACK,(j*PIXEL_SIZE,0,PIXEL_SIZE,PIXEL_SIZE*curr_1))
                randomlist[j], randomlist[j + 1] = randomlist[j + 1], randomlist[j]
                pygame.display.update()
            else:
                # pygame.time.delay(1)
                pygame.draw.rect(win,BLACK,(j*PIXEL_SIZE,0,PIXEL_SIZE,PIXEL_SIZE*curr))
                pygame.draw.rect(win,BLACK,((j+1)*PIXEL_SIZE,0,PIXEL_SIZE,PIXEL_SIZE*curr_1))
                pygame.display.update()   
              
    return randomlist    