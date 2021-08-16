from abc import ABC, abstractproperty


class Nature(ABC):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Nature, cls).__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        pass

    @abstractproperty
    def good_vs(self) -> "Nature":
        pass

    @abstractproperty
    def bad_vs(self) -> "Nature":
        pass


class Fire(Nature):
    def __init__(self) -> None:
        pass

    @property
    def good_vs(self) -> Nature:
        return Flora()

    @property
    def bad_vs(self) -> Nature:
        return Water()


class Water(Nature):
    def __init__(self) -> None:
        pass
    
    @property
    def good_vs(self) -> Nature:
        return Fire()

    @property
    def bad_vs(self) -> Nature:
        return Flora()


class Flora(Nature):
    def __init__(self) -> None:
        pass
    
    @property
    def good_vs(self) -> Nature:
        return Water()

    @property
    def bad_vs(self) -> Nature:
        return Fire()