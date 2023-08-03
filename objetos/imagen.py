class Imagen:
    def __init__(self, imagenes_nombre, imagenes_texto, imagenes_ruta):
        self.imagenes_nombre = imagenes_nombre
        self.imagenes_texto = imagenes_texto
        self.imagenes_ruta = imagenes_ruta

    def __str__(self):
        return f"{self.imagenes_nombre}({self.imagenes_ruta})"
