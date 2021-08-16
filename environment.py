from sys import platform
from ursina import *

app = Ursina()
window.fullscreen_size = (1920, 1080)
window.fullscreen = True


class PlayerStand(Entity):
    def __init__(self, position):
        super().__init__(
            model="quad",
            position=position,
            color=color.white,
            scale=(3, 1),
            )


class AbilityButton(Button):
    def __init__(self, x):
        super().__init__(
            parent=scene,
            color=color.lime,
            position=(x, 3.5),
            )

    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                pass


class Player(Entity):
    def __init__(self, position):
        super().__init__(
            model="quad",
            position=position,
            color=color.orange,
            scale=(2, 3),
        )


stand_x = 3.5
stand_y = -3
p1 = Player((stand_x, stand_y + 2))
p2 = Player((-stand_x, stand_y + 2))
PlayerStand((stand_x, stand_y))
PlayerStand((-stand_x, stand_y))

for x in range(-45, 60, 15):
    AbilityButton(x / 10)
