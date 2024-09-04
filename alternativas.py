class Alternativa:
    """
    Muestra las alternativas y la ayuda para entender el contenido de la alternativa si se le agrega
    """

    def __init__(self, contenido: str, ayuda = None):

        self.contenido = contenido
        self.ayuda = ayuda

    @property
    def contenido(self):
        return self._contenido
        
    @property
    def ayuda(self):
        return self._ayuda
        
    @contenido.setter
    def contenido(self, nuevo_contenido):
        self._contenido = nuevo_contenido

    @ayuda.setter
    def ayuda(self, nuevo_ayuda):
        self._ayuda = nuevo_ayuda

    def mostrar(self):
        return f"{self.contenido} {'-' + self.ayuda + ')' if self.ayuda else ''}"