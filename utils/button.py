from .settings import *


class Button_img:
    def __init__(self, image, x, y, scale,text):
        width = image.get_width()
        height = image.get_height()
        self.text=text
        self.image = pygame.transform.scale(
            image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, win):
        smallfont = pygame.font.SysFont('Corbel', 35)
        text = smallfont.render(self.text, True, WHITE)
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        # draw button on screen
        win.blit(self.image, (self.rect.x, self.rect.y))
        win.blit(text, (self.rect.x+30, self.rect.y+5))
        # print(self.rect.x,self.rect.y)
        return action

class Button:
    def __init__(self,text,width,height,pos):
        # top rectangle
        self.top_rect=pygame.Rect(pos,(width,height))
        self.top_color=BUTTON
        # text
        smallfont = pygame.font.SysFont('Corbel', 35)
        self.text_surf = smallfont.render(text, True, WHITE)
        self.text_rect=self.text_surf.get_rect(center=self.top_rect.center)

    def draw(self,win):
        pygame.draw.rect(win,self.top_color,self.top_rect,border_radius=12)
        win.blit(self.text_surf,self.text_rect)
        pos = pygame.mouse.get_pos()
        action=False
        if self.top_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        return action    