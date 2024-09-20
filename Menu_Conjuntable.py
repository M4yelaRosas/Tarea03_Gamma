def menu_conjuntable() -> str:
    """
    Metodo auxiliar que despliega las opciones que podemos realizar con la clase Conjuntable
    :return: opcion: Str - La opcion deseada a realizar
    :rtype: Str
    """
    while True:
        opcionn = input('Que deseas hacer:\n'
                        '1. Agregar elemento\n'
                        '2. Eliminar elemento\n'
                        '3. Consultar elemento\n'
                        '4. Consultar Secuencia\n'
                        '5. Modificar Secuencia\n'
                        'S. Salir \n').upper()
        if opcionn not in '1,2,3,4,5,S' or len(opcionn) != 1:
            print('Opcion incorrecta')
            continue
        else:
            break
    return opcionn

def menu_agregar() -> str:
    """
    Metodo auxiliar que despliega las opciones que podemos realizar al agregar un elemento
    :return: opcion: Str - La opcion deseada a realizar
    :rtype: Str
    """
    while True:
        opcionn = input('Que deseas hacer:\n'
                        '1. Agregar un elemento\n'
                        '2. Agregar un elemento un número de veces especificado\n'
                        'S. Salir \n').upper()
        if opcionn not in '1,2,S' or len(opcionn) != 1:
            print('Opcion incorrecta')
            continue
        else:
            break
    return opcionn

def menu_eliminar() -> str:
    """
    Metodo auxiliar que despliega las opciones que podemos realizar al eliminar un elemento
    :return: opcion: Str - La opcion deseada a realizar
    :rtype: Str
    """
    while True:
        opcionn = input('Que deseas hacer:\n'
                        '1. Eliminar todas las repeticiones de un elemento\n'
                        '2. Eliminar un número especificado de repeticiones de un elemento\n'
                        'S. Salir \n').upper()
        if opcionn not in '1,2,S' or len(opcionn) != 1:
            print('Opcion incorrecta')
            continue
        else:
            break
    return opcionn

def menu_consultar_elemento() -> str:
    """
    Metodo auxiliar que despliega las opciones que podemos realizar al consultar un elemento
    :return: opcion: Str - La opcion deseada a realizar
    :rtype: Str
    """
    while True:
        opcionn = input('Que deseas hacer:\n'
                        '1. Verificar si un elemento se encuentra en la Secuencia\n'
                        '2. Contar el número de repeticiones de un elemento en la Secuencia\n'
                        'S. Salir \n').upper()
        if opcionn not in '1,2,S' or len(opcionn) != 1:
            print('Opcion incorrecta')
            continue
        else:
            break
    return opcionn

def menu_consultar_secuencia() -> str:
    """
    Metodo auxiliar que despliega las opciones que podemos realizar al consultar la Secuencia
    :return: opcion: Str - La opcion deseada a realizar
    :rtype: Str
    """
    while True:
        opcionn = input('Que deseas hacer:\n'
                        '1. Verificar si la Secuencia está vacía\n'
                        '2. Obtener la cardinalidad de la Secuencia (número de elementos)\n'
                        'S. Salir \n').upper()
        if opcionn not in '1,2,S' or len(opcionn) != 1:
            print('Opcion incorrecta')
            continue
        else:
            break
    return opcionn

def menu_modificar_secuencia() -> str:
    """
    Metodo auxiliar que despliega las opciones que podemos realizar al modificar la Secuencia
    :return: opcion: Str - La opcion deseada a realizar
    :rtype: Str
    """
    while True:
        opcionn = input('Que deseas hacer:\n'
                        '1. Vaciar la Secuencia de elementos\n'
                        '2. Obtener la Secuencia de elementos únicos (sin repeticiones)\n'
                        '3. Ordenar la Secuencia de elementos\n'
                        'S. Salir \n').upper()
        if opcionn not in '1,2,3,S' or len(opcionn) != 1:
            print('Opcion incorrecta')
            continue
        else:
            break
    return opcionn