class DEntrada:

    def __init__(self, tentrada, marca) -> None:
        self._tentrada = tentrada
        self._marca = marca

    # Gets of each atribute
    def get_marca(self) -> str:
        return self._marca

    def get_tentrada(self) -> str:
        return self._tentrada

    # Sets of each atribute
    def set_marca(self, marca) -> None:
        self._marca = marca

    def set_marca(self, tentrada) -> None:
        self._tentrada = tentrada

    # Other methods
    def __str__(self) -> str:
        return f'Dispositivo de entrada: marca[{self._marca}] tipo de entrada[{self._tentrada}]'