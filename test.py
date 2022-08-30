from Computadora import *
from DispositivoEntrada import *
from Orden import *
from Raton import *
from Teclado import *
from Monitor import *

ra1 = Raton('HP', 'usb')
te1 = Teclado('HP', 'usb')
mo1 = Monitor('HP', 15)

ra2 = Raton('Acer', 'bluetooth')
te2 = Teclado('Acer', 'bluetooth')
mo2 = Monitor('Acer', 27)

com1 = Computer('HP', mo1, ra1, te1)
com2 = Computer('Acer', mo2, ra2, te2)

computadoras = [com1, com2]
orden1 = Orden(computadoras)

print(orden1)