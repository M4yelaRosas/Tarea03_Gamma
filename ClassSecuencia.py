# Programa: ClassSecuencia.py
# Objetivo: Mostrar la implementación de la "interfaz" Conjuntable, para
#           ilustrar la creación de un TAD de objetos.
# Autores: Milena Rivera, Carlos Barrera, Isaac Garrido, Mayela Rosas
# Version: 18-09-2024

import Interfaz_Conjuntable as Ic
import Empleado as Em
import numpy as np


class Secuencia(Ic.Conjuntable):
    def __init__(self, *params):
        """
        Constructor de la secuencia que contendra objetos del tipo Empleado.
        :param params: Si no recibe nada es el constructor por omision.
                       Si recibe un parametro, es el constructor por parametros
        """
        if len(params) == 0:  # Constructor por omision = conjunto de tamanio 20
            self.__datos = np.empty(20, dtype=Em.Empleado)
            self.__nd = 0
            print("Se creo una Secuencia para 20 elementos!\n")
        elif len(params) == 1:  # Constructor por parametros
            try:
                self.__datos = np.empty(params[0], dtype=Em.Empleado)
                self.__nd = 0
                print(f"Se creo una Secuencia para {params[0]} elementos!\n")
            except ValueError:
                print("El tamaño del arreglo debe ser positivo!\n")

    @property
    def datos(self):
        """
        Metodo GET para obtener la secuencia de datos
        :return: EL arreglo de datos
        :rtype: np.array
        """
        return self.__datos

    @property
    def nd(self) -> int:
        """
        Metodo GET para obtener el numero de datos de la secuencia
        :return: El numero de datos insertados en la Secuencia
        :rtype: int
        """
        return self.__nd

    def agregar(self, *params):
        """
        Metodo para agregar un elemento a la Secuencia, siempre
        que sea posible.
        :param params: Si solo recibe un parametro, este debera de ser el elemento a agregar
                       Si recibe dos parametros, estos seran el elemento a agregar y el numero
                       de veces que se desea agregar.
        """
        if len(params) == 1:
            try:
                self.__datos[self.__nd] = params[0]
                self.__nd += 1
            except IndexError:
                print("No es posible agregar mas elementos!\n")
        elif len(params) == 2:
            try:
                for i in range(params[1]):
                    self.__datos[self.__nd] = params[0]
                    self.__nd += 1
            except IndexError:
                print("No es posible agregar mas elementos!\n")

    def eliminar(self, *params):
        """
        Método que permite eliminar todas las repeticiones del elemento dentro
        de la Secuencia, siempre que esto sea posible.
        :param params: Si solo recibe un parametro, este debera de ser el elemento a eliminar.
                        (en caso de estar repetido en la secuencia, este metodo eliminara el
                        primero que se encuentre)
                       Si recibe dos parametros, estos seran el elemento a eliminar y el numero
                       de veces que se desea eliminar.
                       (en caso de estar repetido en la secuencia, este metodo eliminara los
                       primeros nrep que se encuentre)
        """
        if len(params) == 1:
            # Hay que asegurarnos que el arreglo no este vacio y el elemento exista
            if not self.esta_vacia() and self.contiene(params[0]):
                encontro = False
                it1 = iter(self)
                i = 0
                try:
                    while True:
                        elem = next(it1)
                        if elem == params[0]:  # Lo encontro
                            if i == self.__nd - 1:  # El elemento esta al final
                                self.__nd -= 1  # Dejamos innaccesible el elemento
                            else:  # El elemento no esta al final
                                self.__nd -= 1
                                self.__datos[i] = self.__datos[self.__nd]
                            print(f"El elemento {params[0]} fue eliminado!\n")
                            encontro = True
                            break # elimino el primero que encuentro
                        i += 1
                except StopIteration:
                    pass
                if not encontro:
                    print(f"El elemento {params[0]} no esta en la Secuencia!\n")

        elif len(params) == 2:
            # Hay que asegurarnos que el arreglo no este vacio y el elemento exista
            if not self.esta_vacia() and self.contiene(params[0]):
                aux = 0 # me ayudara a contar cuantos llevo eliminados
                encontro = False
                it1 = iter(self)
                i = 0
                try:
                    while True:
                        elem = next(it1)
                        if elem == params[0]:  # Lo encontro
                            if i == self.__nd - 1:  # El elemento esta al final
                                self.__nd -= 1  # Dejamos innaccesible el elemento
                            else:  # El elemento no esta al final
                                self.__nd -= 1
                                self.__datos[i] = self.__datos[self.__nd]
                            print(f"El elemento {params[0]} fue eliminado!\n")
                            encontro = True
                            aux += 1
                            if aux == params[1]:
                                break
                            else:# en teoria en la secuencia si hay que seguir buscando
                        i += 1
                except StopIteration:
                    pass
                if not encontro:
                    print(f"El elemento {params[0]} no esta en la Secuencia!\n")

    # carlos
    def contiene(self, elemento: Em.Empleado) -> bool:
        """
        Método que permite saber sí un elemento se encuentra contenido
        dentro de la Secuencia.
        :param elemento: El elemento a buscar
        :return: True si lo encontró, False en otro caso
        :rtype: bool
        """
        pass

    def repeticiones(self, elemento: Em.Empleado) -> int:
        """
        Método que determina el número de repeticiones que el elemento
        presenta dentro de la Secuencia.
        :param elemento: El elemento a determinar las repeticiones
        :return: El número de veces que aparece en la Secuencia
        :rtype: int
        """
        pass

    def esta_vacia(self) -> bool:
        """
        Método que permite saber sí la Secuencia está vacía.
        :return: True sí está vacía, False en otro caso.
        :rtype: bool
        """
        pass

    def cardinalidad(self) -> int:
        """
        Método que permite conocer la cardinalidad de la Secuencia.
        :return: La cantidad de elementos almacenados en la Secuencia
        :rtype: int
        """
        pass

    def vaciar(self):
        """
        Método que permite vaciar la Secuencia de elementos.
        """
        pass

    def secuencia_unico(self):
        """
        Método que permite devuelve la Secuencia de elementos únicos
        (sin repeticiones).
        :return: La Secuencia sin repetidos
        """
        pass

    def ordenar(self):
        """
        Método que permite devuelve la Secuencia de elementos ordenada.
        Utiliza Quick Sort o Merge Sort y habilita la existencia de dos comparadores
        por ejemplo, en el caso de los Empleados, se pueden ordenar por edad, por
        salario, por edad y nombre, salario y nombre, etc.
        :return: La Secuencia ordenada
        """
        pass

# Metodos extra

    def __str__(self):
        """
        Metodo que permite devolver una Secuencia como una cadena de caracteres
        :return: La secuencia en formato cadena
        """
        # Utilizando los iteradores
        it1 = iter(self)
        secuencia = "Secuencia: \n"
        try:
            while True:
                elem = next(it1)
                secuencia += str(elem) + "\n"
        except StopIteration:
            pass
        return secuencia

    def __eq__(self, otra_secuencia):
        """
        Metodo que permite determinar si dos secuencias son iguales
        :param otra_secuencia: La Secuencias con el que se va a comparar
        :return: True si son iguales, False en otro caso
        """
        respuesta = True  # Asumimos que las dos Secuencias son iguales
        # Utilizando los iteradores
        it1 = iter(self)
        # Verificamos que tengan la misma cardinalidad
        if self.cardinalidad() == otra_secuencia.cardinalidad():
            try:
                while True:
                    elem = next(it1)
                    if not otra_secuencia.contiene(elem):
                        respuesta = False
                        break
            except StopIteration:
                pass
        else:
            respuesta = False
        return respuesta

    def __iter__(self):
        """
        Metodo que permite inicializar el iterador de Secuencias
        :return: Un objeto iterable
        """
        self.pos = 0
        return self

    def __next__(self) -> Em.Empleado:
        """
        Metodo que permite obtener el siguiente elemento de la Secuencia
        :return: El siguiente elemento de la Secuencia
        :rtype: int
        """
        if self.pos < self.nd:
            a = self.datos[self.pos]
            self.pos += 1
            return a
        else:
            raise StopIteration
