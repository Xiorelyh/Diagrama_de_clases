#No modifiicar
from usuario import Usuario
from alternativas import Alternativa
from preguntas import Preguntas
from encuesta import (Encuesta, EncuestaLimitadaEdad, EncuestaLimitadaRegion)

def main():
    nombre_usuario = input("Indica tu nombre:\n> ")
    edad = int(input("Indica tu edad:\n> "))
    print("Region:\n1. Tarapaca\n2. Antofagasta\n3. Atacama\n4.Coquimbo\n5.Valparaiso")
    region = int(input("Indica tu region, por favor:\n> "))

    usuario = Usuario(nombre_usuario, edad, region)


    #creamos alternativas para probar
    alternativa1 = Alternativa("1. Si")
    alternativa2 = Alternativa("2. No", "Esto significa que no te gustan las toras")

    #creamos preguntas para probar
    pregunta1 = Preguntas("¿Te gustan las tortas?", "Escoge 1, si te gustan las tortas, y 2 si no te gustan")
    pregunta1.agregar_alternativas(alternativa1)
    pregunta1.agregar_alternativas(alternativa2)

    #Edad minima y maxima para encuesta limitada por edad
    edad_minima = 18
    edad_maxima = 30

    #Tipo de encuesta
    #1. Encuesta de edad
    #2. Encuesta Region
    tipo_encuesta = 1

    if tipo_encuesta == 1:
        #creamos una encuesta
        encuesta = EncuestaLimitadaEdad("Catacion de Tortas", edad_minima, edad_maxima)
        encuesta.agregar_pregunta(pregunta1)

        respuesta_usuario = 0
        if edad < edad_minima or edad > edad_maxima:
            print("Lo sentimos, no cumples con los requisitos de edad para esta encuesta.")
        else:
            #mostramos la encuesta
            print(encuesta.mostrar())
            respuesta_usuario = int(input("Responde indicando el numero de la respuesta:\n> "))
            while respuesta_usuario < len(pregunta1.alternativas) or respuesta_usuario > len(pregunta1.alternativas):
                respuesta_usuario = int(input(f"Responde indicando una respuesta valida.\n{encuesta.mostrar()}\nIndica una respuesta:\n> "))
            usuario.contestar_encuesta(encuesta, respuesta_usuario)
            print("\nMuchas gracias por participar\nHasta la proxima!")
    
    elif tipo_encuesta == 2:
        #creamos una encuesta
        encuesta = EncuestaLimitadaRegion("Catacion de Tortas")
        encuesta.agregar_pregunta(pregunta1)

        if region not in encuesta.regiones:
            print("Lo sentimos, tu región no es elegible para esta encuesta.")
        else:
            #mostramos la encuesta
            print(encuesta.mostrar())
            respuesta_usuario = int(input("Responde indicando el numero de la respuesta:\n> "))
            while respuesta_usuario < len(pregunta1.alternativas) or respuesta_usuario > len(pregunta1.alternativas):
                respuesta_usuario = int(input(f"Responde indicando una respuesta valida.\n{encuesta.mostrar()}\nIndica una respuesta:\n> "))
            usuario.contestar_encuesta(encuesta, respuesta_usuario)
            print("\nMuchas gracias por participar\nHasta la proxima!")
main()