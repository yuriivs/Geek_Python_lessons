from abc import ABC, abstractmethod

import self as self


class Clothes(ABC):
    def __init__(self, name: str = None):
        self.name = name

    @property
    @abstractmethod
    def clothes_type(self):
        pass

    @abstractmethod
    def get_tissue_consumption(self):
        pass


class Coat(Clothes):
    clothes_type = 'пальто'

    def __init__(self, size: float, name: str = None):
        super().__init__(name)
        self.size = size

    @property
    def get_tissue_consumption(self):
        result = round(self.size / 6.5 + 0.5, 2)
        return result


class Suit(Clothes):
    clothes_type = 'костюм'

    def __init__(self, height: float, name: str = None):
        super().__init__(name)
        self.height = height

    @property
    def get_tissue_consumption(self):
        result = round(2 * self.height + 0.3)
        return result


newCoat = Coat(42)
print(
    f'Расход ткани для типа одежды {newCoat.clothes_type}, размер {newCoat.size}: {newCoat.get_tissue_consumption} условных единиц.')

newSuit = Suit(175)
print(
    f'Расход ткани для типа одежды {newSuit.clothes_type}, рост {newSuit.height}: {newSuit.get_tissue_consumption} условных единиц.')
