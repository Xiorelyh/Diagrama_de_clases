class Usuario:
    def __init__(self, nombre, edad, region):
        self.nombre = nombre
        self.edad = edad
        self.region = region
        self.respuestas = []

    def contestar_encuesta(self, encuesta, respuesta_usuario):
        # Suponiendo que "encuesta" tiene un método para procesar la respuesta.
        encuesta.recibir_respuesta(self, respuesta_usuario)
        self.respuestas.append(respuesta_usuario)  # Guardamos la respuesta del usuario
        print(f"Gracias {self.nombre}, has respondido la encuesta con la opción {respuesta_usuario}.")


        