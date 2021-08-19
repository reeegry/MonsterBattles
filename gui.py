import pygame as pg
import pygame_gui as pg_gui
from utilities import get_resolution


class Gui:
    def __init__(self):
        self.manager = pg_gui.UIManager(get_resolution())
    
    def events(self, event):
        pass
        
    def update(self, time_delta):
        self.manager.update(time_delta)

    def draw(self, screen):
        self.manager.draw_ui(screen)


class BattleGui(Gui):
    def __init__(self):
        super().__init__()
        self.hello_button = pg_gui.elements.UIButton(relative_rect=pg.Rect((350, 275), (100, 50)),
                                             text='Test button',
                                             manager=self.manager)

    def events(self, event):
        if event.type == pg.USEREVENT:
            if event.user_type == pg_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.hello_button:
                    print('Test button pressed')
        
        self.manager.process_events(event)
