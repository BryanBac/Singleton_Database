from EntradaSalida.io import IO
from os import remove
from datetime import datetime


class ArchivoDeTexto(IO):
    def __init__(self, nombre_archivo: str):
        self.nombre_archivo: str = nombre_archivo

    def modificar_archivo(self, texto: str):
        data = open(self.nombre_archivo, 'a')
        fecha: datetime = datetime.now().date()
        hora: datetime = datetime.now().time()
        data.write(texto + f" --- {fecha} --- {hora} \n")
        data.close()

    def eliminar_archivo(self):
        remove(self.nombre_archivo)
