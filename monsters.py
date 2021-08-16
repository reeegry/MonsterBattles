from abc import ABC, abstractmethod
from utilities import transform_class_name
from enum import auto, Enum
from popo_fsm import transition
import natures
import abilities
from attributes import Hitpoints, Speed

class MonsterStates(Enum):
    DEFAULT = auto()
    DEAD = auto()
    ESCAPING = auto()

class MonsterLocations(Enum):
    DEFAULT = auto()
    IN_BAG = auto()
    IN_BATTLE = auto()

class Monster(ABC):
    def __init__(self) -> None:
        self.name = transform_class_name(self.__class__.__name__)
        self.enemy = NoEnemy()
        self.hp = Hitpoints(100)
        self.speed = Speed(0)
        self.abilities_list = []
        self.state = MonsterStates.DEFAULT
        self.location = MonsterLocations.DEFAULT
        self.nature = natures.Normal()
        
    def update(self):
        self.kill()
        self.draw()
    
    '''
    #For future
    @abstractmethod
    def draw(self):
        pass
    '''

    def is_dead(self):
        return self.hp.current == 0
    
    @transition('state', '*', MonsterStates.DEAD, [is_dead], before=True)
    def kill(self):
        print(f'{self.name} killed!')
    
    @property
    def state(self):
        return self._state
    
    @state.setter
    def state(self, value):
        self._state = value if isinstance(value, MonsterStates) else MonsterStates.DEFAULT
    
    @property
    def location(self):
        return self._location
    
    @location.setter
    def location(self, value):
        self._location = value if isinstance(value, MonsterStates) else MonsterLocations.DEFAULT

    @property
    def nature(self):
        return self.nature

    @nature.setter
    def nature(self, value):
        self._nature = value if isinstance(value, natures.Nature) else natures.Normal()
    
    @property
    def enemy(self):
        return self._enemy

    @enemy.setter
    def enemy(self, value):
        self._enemy = value if isinstance(value, Monster) else NoEnemy()
    
class NoEnemy(Monster):
    pass

class Flee(Monster):
    def __init__(self) -> None:
        super().__init__()
        self.abilities_list = [abilities.FireTunder(self)]
        self.hp = Hitpoints(range(100, 121), ranged=True)
        self.speed = Speed(range(5, 9), ranged=True)
        self.nature = natures.Fire()


class Cordelia(Monster):
    def __init__(self) -> None:
        super().__init__()
        self.abilities_list = [abilities.BubbleStorm(self)]
        self.hp = Hitpoints(140)
        self.speed = Speed(range(8, 10), ranged=True)
        self.nature = natures.Water()

        
class PotatoKing(Monster):
    def __init__(self) -> None:
        super().__init__()
        self.abilities_list = [abilities.Revoluton(self)]
        self.hp = Hitpoints(100)
        self.speed = Speed(range(10, 20), ranged=True)
        self.nature = natures.Flora()
