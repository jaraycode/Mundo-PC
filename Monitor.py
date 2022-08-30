class Monitor:

    # Static Variable
    cont_Monitor = 0

    @classmethod
    def aumentoMonitor(cls) -> int:
        cls.cont_Monitor += 1
        return cls.cont_Monitor

    def __init__(self, marca, size) -> None:
        self._id_monitor = Monitor.aumentoMonitor()
        self._marca = marca
        self._size = float(size)

    # Gets of each atribute
    def get_marca(self) -> str:
        return self._marca

    def get_size(self) -> float:
        return self._size
    
    # Sets of each atribute
    def set_marca(self, marca) -> None:
        self._marca = marca

    def set_size(self, size) -> None:
        self._size = size

    def __str__(self) -> str:
        return f'Monitor: marca[{self._marca}] tamaño[{self._size} pulgadas]'