import pygame as pg

class player:

    def __init__(self, display, sprite, pos_X = 0, pos_y = 0):
        
        self.display = display
        self.sprite = sprite
        self.pos_X = pos_X
        self.pos_Y = pos_y


        pass

        def render(self):
            #MAGIC NUMBErS LOL(    bad code :(   )
            pg.draw.rect(display, (255, 0, 0), (pos_X, pos_y, 50, 50))
        
        def 




