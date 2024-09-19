# Programa: PruebaSecuencia.py
# Objetivo: Prueba de los metodos de la clase conjunto.
# Autores: Milena Rivera, Carlos Barrera, Isaac Garrido, Mayela Rosas
# Version: 18-09-2024


import ClassSecuencia as Cs
import Empleado as Em
from datetime import datetime
import csv


def leer_archivo(archivo: str) -> Cs.Secuencia:
    """
    Metodo para leer un archivo y construir una secuencia con dichos datos
    :param archivo: El nombre del archivo que se va a leer
    :return: Una Secuencia con los datos leidos
    """
    secuencia = None
    existe = False  # El archivo no existe
    while not existe:
        try:
            with open(archivo, encoding="UTF8", newline="") as file:
                lector = csv.reader(file)
                size = sum(1 for _ in lector)  # Saber el numero de lineas
                secuencia = Cs.Secuencia(size)  # Creamos el Conjunto de tamanio ad-hoc
            with open(archivo, encoding="UTF8", newline="") as file:
                lector = csv.reader(file)
                lector.__next__()  # Salta la primera línea
                for fila in lector:
                    secuencia.agregar(Em.Empleado(fila[1],  # Nombre
                                                  fila[2],  # Apellidos
                                                  datetime.strptime(fila[3], "%d/%m/%Y").date(),  # Nacimiento
                                                  fila[4],  # Correo
                                                  int(fila[0]),  # Numero Empleado
                                                  float(fila[5])))  # Salario
                existe = True
                print(f"El archivo {archivo} se leyo exitosamente!\n")
        except FileNotFoundError:
            print("El archivo no existe!\n")
            archivo = input("Escribe el nombre del archivo CSV: ")
    return secuencia
