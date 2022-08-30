from DispositivoEntrada import DEntrada

class Teclado(DEntrada):

    cont_teclado = 0

    @classmethod
    def aumentoTeclado(cls) -> int:
        cls.cont_teclado += 1
        return cls.cont_teclado

    def __init__(self, marca, tentrada) -> None:
        super().__init__(tentrada, marca)
        self._id_teclado = Teclado.aumentoTeclado()
    
    # Get of id
    def get_id(self) -> int:
        return self._id_teclado

    # Other methods
    def __str__(self) -> str:
        return super().__str__() + f' teclado[{self._id_teclado}]'