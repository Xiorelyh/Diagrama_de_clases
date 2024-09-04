from alternativas import Alternativa

class Preguntas:
    """
    Extrae el enunciado de la pregunta, si la pregunta es obligatoria de responder, y una ayuda para entender la pregunta, si esto se le pasara.
    """
    def __init__(self, enunciado: str, requerida: None, ayuda = None):
        self.enunciado = enunciado
        self.requerida = requerida
        self.ayuda = ayuda
        self.alternativas = []

    @property
    def enunciado(self):
        return self._enunciado

    @property
    def requerida(self):
        return self._requerida

    @property
    def ayuda(self):
        return self._ayuda

    @enunciado.setter
    def enunciado(self, nuevo_enunciado):
        self._enunciado = nuevo_enunciado

    @requerida.setter
    def requerida(self, nuevo_requerida):
        self._requerida = nuevo_requerida

    @ayuda.setter
    def ayuda(self, nuevo_ayuda):
        self._ayuda = nuevo_ayuda


    def agregar_alternativas(self, alternativa):
        """
        Agrega las alternativas a la pregunta correspondiente
        """
        self.alternativas.append(alternativa)

    def mostrar(self):
        """
        Muestra el enunciado de la pregunta, con las alternativas correspondientes.
        """
        alternativa_mostrada = "\n".join([alt.mostrar() for alt in self.alternativas])
        return f"{self.enunciado}\n{self.ayuda if self.ayuda else ''}\nAlternativas:\n{alternativa_mostrada}"