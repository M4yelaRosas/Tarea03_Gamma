from abc import abstractmethod, ABCMeta
from typing import TypeVar

T = TypeVar('T')


class Conjuntable(metaclass=ABCMeta):
    @abstractmethod
    def agregar(self, elemento: T):
        pass

    @abstractmethod
    def agregar_nveces(self, elemento: T, nveces: int):
        pass

    @abstractmethod
    def eliminar(self, elemento: T):
        pass

    @abstractmethod
    def eliminar_nrep(self, elemento: T, nrep: int):
        pass

    @abstractmethod
    def contiene(self, elemento: T) -> bool:
        pass

    @abstractmethod
    def repeticiones(self, elemento: T) -> int:
        pass

    @abstractmethod
    def esta_vacia(self) -> bool:
        pass

    @abstractmethod
    def cardinalidad(self) -> int:
        pass

    @abstractmethod
    def vaciar(self):
        pass

    @abstractmethod
    def secuencia_unica(self):
        pass

    @abstractmethod
    def ordenar(self):
        pass
