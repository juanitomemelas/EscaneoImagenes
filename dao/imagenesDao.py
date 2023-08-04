from objetos.imagen import Imagen
import utilerias

def insertarImagen(img: Imagen):
    utilerias.dbinsert(img)