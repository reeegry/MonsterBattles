from abc import ABC, abstractmethod, abstractproperty
from utilities import transform_class_name
import natures
import random



class Ability(ABC):
    def __init__(self, owner) -> None:
        self.name = transform_class_name(self.__class__.__name__)
        self.owner = owner
        self.multiplier = 1.0

        self._damage = None
        self._nature = None

    @abstractmethod
    def _before_use(self):
        pass
    
    @abstractmethod
    def _after_use(self):
        pass
    
    @abstractmethod
    def use(self):
        pass
    
    @abstractproperty
    def nature(self):
        pass
    
    @property
    def damage(self):
        return random.choice(self._damage)

    @damage.setter
    def damage(self, value):
        self._damage = value if any(isinstance(value, type_) for type_ in [range, int]) else 0


class AttackingAbility(Ability):
    def use(self) -> None:
        self._before_use()
        if self.owner.enemy.nature is self.nature.good_vs:
            self.owner.enemy.hp -= round(self.damage * self.multiplier)

        elif self.owner.enemy.nature is self.nature.bad_vs:
            self.owner.enemy.hp -= round(self.damage / self.multiplier)
        else:
            self.owner.enemy.hp -= round(self.damage)
        self._after_use()

class FireTunder(AttackingAbility):
    def __init__(self, owner) -> None:
        super().__init__(owner)
        self.damage = range(15, 20)
        self.multiplier = 1.2
    
    def _before_use(self):
        pass

    def _after_use(self):
        pass

    @property
    def nature(self):
        return natures.Fire()

class BubbleStorm(AttackingAbility):
    def __init__(self, owner) -> None:
        super().__init__(owner)
        self.damage = range(5, 12)
        self.multiplier = 1.25
    
    def _before_use(self):
        pass

    def _after_use(self):
        self.owner.hp -= self.owner.enemy.hp * 0.1

    @property
    def nature(self) -> natures.Nature:
        return natures.Water()