from monsters import Flee, Cordelia
from gui import BattleGui
from utilities import get_resolution
import pygame as pg
import pygame_gui as pg_gui

 
class Game:
    '''
    scene management class
    '''
    FPS = 60
    def __init__(self) -> None:
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode(get_resolution(), pg.FULLSCREEN)
        self.manager = pg_gui.UIManager((500, 500))
        self.clock = pg.time.Clock()
        self.running = True
        self.scene = Battle(self)
 
    def run(self):
        while self.running:
            self.time_delta = self.clock.tick(60) / 1000.0
            self.clock.tick(self.FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pg.event.get():
            self.scene.gui.events(event)
            if event.type == pg.QUIT:
                self.running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.running = False

    def update(self):
        self.scene.update()
        self.scene.gui.update(self.time_delta)
        pg.display.update()
 
    def draw(self):
        self.scene.draw()
        self.scene.gui.draw(self.screen)
 
 
class Scene:
    BGCOLOR = (255,0,0)
    def __init__(self, game):
        self.game = game
        self.sprites = pg.sprite.LayeredUpdates()
 
    def events(self):
        pass
 
    def update(self):
        pass
 
    def draw(self):
        self.game.screen.fill(self.BGCOLOR)
        #self.sprites.draw(self.game.screen)
 
 
class Battle(Scene):
    BGCOLOR = (255,100,100)
    def __init__(self, game):
        super().__init__(game)
        self.gui = BattleGui()
    
    def events(self):
        pass


if __name__ == '__main__':
    g = Game()
    g.run()