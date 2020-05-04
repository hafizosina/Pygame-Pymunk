import pygame as pg
import pymunk

from setting import *


debugFPS = 0


class Game:
    def __init__(self, width, height):
        self.Running = True
        pg.init()
        pg.mixer.init()
        self.clock = pg.time.Clock()
        pg.key.set_repeat(100,100)
        
        self.width = width
        self.height = height
        self.screen = pg.display.set_mode((self.width,self.height))
        pg.display.set_caption('Pymunk Test')
        
    def event(self):
        pressed = pg.key.get_pressed()
        alt_held = pressed[pg.K_LALT] or pressed[pg.K_RALT]
        ctrl_held = pressed[pg.K_LCTRL] or pressed[pg.K_RCTRL]
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.Running = False
                
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_F4 and alt_held:
                    self.Running = False
            
        
    def update(self):
        pass
        
    def draw(self):
        self.screen.fill(GREEN)
        pg.display.flip()
        
    def run(self):
        while self.Running:
            self.dt = self.clock.tick(FPS) / 100
            if debugFPS:
                print('FPS: ',1/(self.dt),'\tDt: ',self.dt)
            self.event()
            self.update()
            self.draw()
        

if __name__ == '__main__':
    g = Game(WIDTH, HEIGHT)
    g.run()
    pg.quit()