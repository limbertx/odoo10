# esta linea de abajo importa todo lo que hay dentro del archivo
#import module

#e = module.Ejemplo();
#e.imprime()
# tambien puedo usar una funcion
# que esta dentro del modulo
#module.fEjemplo()



# esto solo importa la clase
from module import Ejemplo

# con lo de abajo se importa todo lo que hay en el archivo
#from module import *
e = Ejemplo()
e.imprime()