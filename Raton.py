from DispositivoEntrada import DEntrada

class Raton(DEntrada):

    cont_raton = 0

    @classmethod
    def aumentoRaton(cls) -> int:
        cls.cont_raton += 1
        return cls.cont_raton

    def __init__(self, marca, tentrada) -> None:
        super().__init__(tentrada, marca)
        self._id_raton = Raton.aumentoRaton()

    # Get of id
    def get_id(self) -> int:
        return self._id_raton

    # Other methods
    def __str__(self) -> str:
        return super().__str__() + f' raton[{self._id_raton}]'