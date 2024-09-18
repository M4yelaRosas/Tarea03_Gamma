# Programa: PruebaSecuencia.py
# Objetivo: Prueba de los metodos de la clase conjunto.
# Autores: Milena Rivera, Carlos Barrera, Isaac Garrido, Mayela Rosas
# Version: 18-09-2024


import ConjuntoEmpleado as c
import Empleado as e
from datetime import datetime
import csv



def leer_archivo(archivo: str) -> c.Conjunto:
    """
    Método para leer un archivo y construir un conjunto con dichos datos
    :param archivo: El nombre del archivo que se va a leer
    :return: Un Conjunto con los datos leídos
    """
    conjunto = None
    existe = False  # El archivo no existe
    while not existe:
        try:
            with open(archivo, encoding="UTF8", newline="") as file:
                lector = csv.reader(file)
                size = sum(1 for row in lector)  # Saber el número de líneas
                conjunto = c.Conjunto(size)  # Creamos el Conjunto de tamaño ad-hoc
            with open(archivo, encoding="UTF8", newline="") as file:
                lector = csv.reader(file)
                lector.__next__()  # Salta la primera línea
                for fila in lector:
                    conjunto.agregar(e.Empleado(fila[1],  # Nombre
                                                fila[2],  # Apellidos
                                                datetime.strptime(fila[3], "%d/%m/%Y").date(),  # Nacimiento
                                                fila[4],  # Correo
                                                int(fila[0]),  # Número Empleado
                                                float(fila[5])))  # Salario
                existe = True
                print(f"El archivo {archivo} se leyó exitosamente!\n")
        except FileNotFoundError:
            print("El archivo no existe!\n")
            archivo = input("Escribe el nombre del archivo CSV: ")
    return conjunto