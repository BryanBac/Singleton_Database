from abc import ABCMeta, abstractmethod


class IO(metaclass=ABCMeta):
    @abstractmethod
    def modificar_archivo(self, texto: str):
        raise NotImplementedError

    @abstractmethod
    def eliminar_archivo(self):
        raise NotImplementedError
