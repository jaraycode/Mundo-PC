from Monitor import Monitor
from Teclado import Teclado
from Raton import Raton

class Computer:

    #Static variable
    cont_computer = 0

    @classmethod
    def aumentoComputer(cls) -> int:
        cls.cont_computer += 1
        return cls.cont_computer

    def __init__(self, nombre, monitor, raton, teclado) -> None:
        self._id_computer = Computer.aumentoComputer()
        self._nombre = nombre
        if isinstance(monitor, Monitor):
            self._monitor = monitor
        if isinstance(teclado, Teclado):
            self._teclado = teclado
        if isinstance(raton, Raton):
            self._raton = raton

    # Gets of each atribute
    def get_nombre(self) -> str:
        return self._nombre

    def get_monitor(self) -> str:
        return self._monitor

    def get_id(self) -> int:
        return self._id_computer

    def get_teclado(self) -> str:
        return self._teclado
    
    def get_raton(self) -> str:
        return self._raton

    # Sets of each atribute
    def set_nombre(self, nombre) -> None:
        self._nombre = nombre

    def set_monitor(self, marca, size) -> None:
        self._monitor.set_marca(marca)
        self._monitor.set_size(size)

    def set_teclado(self) -> None:
        pass

    def set_raton(self) -> None:
        pass

    # Other methods
    def __str__(self) -> str:
        return f'{self._nombre}: #{self._id_computer} \n\t\t{self._monitor} \n\t\t{self._teclado} \n\t\t{self._raton}\n'