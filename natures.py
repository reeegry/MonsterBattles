from abc import ABC, abstractproperty
from functools import wraps


class Nature(ABC):
    '''Singleton pattern realization '''
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Nature, cls).__new__(cls)
        return cls._instance

    @abstractproperty
    def good_vs(self) -> "Nature":
        pass

    @abstractproperty
    def bad_vs(self) -> "Nature":
        pass


class Fire(Nature):
    @property
    def good_vs(self) -> Nature:
        return Flora()

    @property
    def bad_vs(self) -> Nature:
        return Water()


class Water(Nature):
    @property
    def good_vs(self) -> Nature:
        return Fire()

    @property
    def bad_vs(self) -> Nature:
        return Flora()


class Flora(Nature):
    @property
    def good_vs(self) -> Nature:
        return Water()

    @property
    def bad_vs(self) -> Nature:
        return Fire()


class Normal(Nature):
    @property
    def good_vs(self) -> Nature:
        pass

    @property
    def bad_vs(self) -> Nature:
        pass
    