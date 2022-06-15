from aws import AWS
from EntradaSalida.io import IO
from EntradaSalida.archivo_de_texto import ArchivoDeTexto


nube = AWS("probando1.txt")
nube2 = AWS("probando2.txt")
archivo: IO = ArchivoDeTexto("probando1.txt")
archivo.modificar_archivo("A ver que pasa")
archivo1: IO = ArchivoDeTexto("probando2.txt")
archivo1.modificar_archivo("Segundo intento")
nube.subir()
nube2.subir()


if id(nube) == id(nube2):
    print("Son iguales")
