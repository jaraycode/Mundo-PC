from Computadora import Computer

class Orden:
    
    cont_orden = 0

    @classmethod
    def aumentoOrden(cls):
        cls.cont_orden += 1
        return cls.cont_orden

    def __init__(self, computer) -> None:
        self._id_orden = self.aumentoOrden()
        self._lista = list(computer)

    def agregarComputer(self, computer):
        if isinstance(computer, Computer):
            self._lista.append(computer)

    def __str__(self) -> str:
        orden_str = ''
        for x in self._lista:
            orden_str += '\t' + x.__str__() + '\n'
        return f'Orden #{self._id_orden} Computadoras: \n{orden_str}'
