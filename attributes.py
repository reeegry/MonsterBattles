import random


class LimitedByMaximumAttrs:
    def __init__(self, value, ranged = False) -> None:
        self.maximum = random.choice(value) if ranged else value
        self.current = self.maximum
    
    @property
    def current(self):
        return self._current
    
    @current.setter
    def current(self, value):
        if 0 <= value <= self.maximum:
            self._current = value
        elif value < 0:
            self._current = 0
        else:
            self._current = self.maximum
    
    def reset(self):
        self.current = self.maximum


class Hitpoints(LimitedByMaximumAttrs):    
    def __init__(self, value, ranged = False) -> None:
        super().__init__(value, ranged)
    
class Powerpoints(LimitedByMaximumAttrs):
    '''
    How many times you can use abiities
    '''
    def __init__(self, value, ranged = False) -> None:
        super().__init__(value, ranged)

class Speed(LimitedByMaximumAttrs):
    '''
    I am speeeeeeeeeeeeeed
    '''
    def __init__(self, value, ranged = False) -> None:
        super().__init__(value, ranged)
        

class Power(LimitedByMaximumAttrs):
    '''
    Abilities damage
    '''
    def __init__(self, value, ranged = False) -> None:
        super().__init__(value, ranged)