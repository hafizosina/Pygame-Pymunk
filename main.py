import pygame as pg
import pymunk as pm
import pymunk.pygame_util
from random import randint

from setting import *


debugFPS = 0


class Game:
    def __init__(self, width, height):
        self.Running = True
        pg.init()
        pg.mixer.init()
        pg.key.set_repeat(100,100)
        
        self.width = width
        self.height = height
        self.screen = pg.display.set_mode((self.width,self.height))
        self.draw_options = pm.pygame_util.DrawOptions(self.screen)
        self.space = pm.Space()
        self.space.gravity = 0, -900
        pg.display.set_caption('Pymunk Test')
        
        self.begin()
        
    def begin(self):
        b0 = self.space.static_body
        '''
        heres the problem point 0,0 in pymunk is in bottom left corner not in top left corner
        '''
        self.segment1 = pm.Segment(b0, (0, 0), (self.width, 0), 4)
        self.segment1.elasticity = 0
        self.segment2 = pm.Segment(b0, (0, 0), (0, self.height), 4)
        self.segment2.elasticity = 0
        self.segment3 = pm.Segment(b0, (0, self.height), (self.width, self.height), 4)
        self.segment3.elasticity = 0
        self.segment4 = pm.Segment(b0, (self.width, 0), (self.width, self.height), 4)
        self.segment4.elasticity = 0
        self.space.add(self.segment1, self.segment2, self.segment3, self.segment4)
        for i in range(20):
            self.body = pm.Body(mass=10, moment=10)
            # remember position in pyunk start at bottom left corner
            self.body.position = randint(20,self.width-20), randint(100, self.height-20)
            self.circle = pm.Circle(self.body, radius=50)
            self.circle.elasticity = 0
            self.space.add(self.body, self.circle)
        self.clock = pg.time.Clock()
        self.run()
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
        self.screen.fill(RED)
        self.space.debug_draw(self.draw_options)
        pg.display.update()
        '''
        What out for this. some time if delta time > 1  colliusion will crashh.
        so lest waht i can to fix it
        '''
        self.space.step(self.dt)
        pg.display.set_caption(str(1/self.dt))
        # pg.display.flip()
        
    def run(self):
        while self.Running:
            self.dt = self.clock.tick(FPS) /1000
            if 1/self.dt< FPStolerance:
                self.dt = 1/FPStolerance
            if debugFPS:
                print('FPS: ',1/(self.dt),'\tDt: ',self.dt)
            self.event()
            self.update()
            self.draw()
        

if __name__ == '__main__':
    g = Game(WIDTH, HEIGHT)
    pg.quit()