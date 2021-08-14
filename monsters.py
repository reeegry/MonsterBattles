from abc import ABC, abstractproperty
from utilities import transform_class_name
import natures
import abilities

class Monster(ABC):
    def __init__(self) -> None:
        self.name = transform_class_name(self.__class__.__name__)
        self.enemy = None
        self.abilities_list = []

        self._hp = 0

    @abstractproperty
    def nature(self):
        pass
    
    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        self._hp = 0 if value <= 0 else value
    
    @property
    def enemy(self):
        return self._enemy

    @enemy.setter
    def enemy(self, value):
        self._enemy = value if isinstance(value, Monster) else None
    

class Flee(Monster):
    def __init__(self) -> None:
        super().__init__()
        self.abilities_list = [abilities.FireTunder(self)]
        self.hp = 100

    @property
    def nature(self):
        return natures.Fire()


class Cordelia(Monster):
    def __init__(self) -> None:
        super().__init__()
        self.abilities_list = [abilities.BubbleStorm(self)]
        self.hp = 140

    @property
    def nature(self):
        return natures.Water()
