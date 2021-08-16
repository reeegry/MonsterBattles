from abc import ABC, abstractmethod, abstractproperty
from monsters import Monster
from utilities import transform_class_name
import natures
from attributes import Power, Powerpoints

class Ability(ABC):
    def __init__(self, owner) -> None:
        self.name = transform_class_name(self.__class__.__name__)
        self.owner = owner
        self.multiplier = 1.0
        self.power = Power(0)
        self.powerpoints = Powerpoints(0)
        self.nature = natures.Normal()

    @abstractmethod
    def use(self):
        pass
    
    '''
    #For future
    @abstractmethod
    def draw(self):
        pass
    '''

    @staticmethod
    def attack(ability: "Ability", defender: Monster):
        if defender.nature is ability.nature.good_vs:
            defender.hp -= round(ability.power.current * ability.multiplier)
        elif defender.nature is ability.nature.bad_vs:
            defender.hp -= round(ability.power.current / ability.multiplier)
        else:
            defender.hp -= ability.power.current

    @property
    def nature(self):
        return self._nature
    
    @nature.setter
    def nature(self, value):
        self._nature = value if isinstance(value, natures.Nature) else natures.Normal


class FireTunder(Ability):
    def __init__(self, owner) -> None:
        super().__init__(owner)
        self.power = Power(range(10, 15), ranged=True)
        self.powerpoints = Powerpoints(30)
        self.nature = natures.Fire()
        self.multiplier = 1.2

    def use(self):
        Ability.attack(ability=self, defender=self.owner.enemy)

class BubbleStorm(Ability):
    def __init__(self, owner) -> None:
        super().__init__(owner)
        self.power = Power(range(5, 12), ranged=True)
        self.powerpoints = Powerpoints(30)
        self.multiplier = 1.25
        self.nature = natures.Water()
    
    def use(self):
        Ability.attack(ability=self, defender=self.owner.enemy)


class Revoluton(Ability):
    def __init__(self, owner) -> None:
        super().__init__(owner)
        self.power = Power(range(1, 20), ranged=True)
        self.powerpoints = Powerpoints(50)
        self.nature = natures.Normal()
    
    def use(self):
        Ability.attack(ability=self, defender=self.owner.enemy)