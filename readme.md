from listado_respuestas import ListadoRespuestas

class Usuario:
    """
    Genera los datos del usuario, correo, edad y region.
    """
    def __init__(self, correo: str, edad: int, region: int):
        self.correo = correo
        self.edad = edad
        self.region = region


    @property
    def correo(self):
        return self._correo

    @property
    def edad(self):
        return self._edad

    @property
    def region(self):
        return self._region
    
    @correo.setter
    def correo(self, nuevo_correo):
        self._correo = nuevo_correo

    @edad.setter
    def edad(self, nueva_edad):
        self._edad = nueva_edad

    @region.setter
    def region(self, nueva_region):
        self._region = nueva_region

    def contestar_encuesta(self, encuesta, respuestas):
        """
        Contesta la encuesta y agrega las respuestas al listado de respuestas.
        Parametros:
        - encuesta: recibe los parametros de la encuesta, como el nombre de la encuesta, y las definiciones
        - respuestas: recibe la respuesta del usuario y la agrega al listado de respuestas.
        """
        listado_respuestas = ListadoRespuestas(self, respuestas)
        encuesta.agregar_listado_respuestas(listado_respuestas)