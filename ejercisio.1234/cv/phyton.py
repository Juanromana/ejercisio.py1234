# numero1 = 30
# numero2 = 20
# total =numero1 + numero2
# print("la suma de numero1 y numero2 es", total)
# # # Condiciones
# x = 0
# if x > 0:
#     print("x es positivo")
# elif x == 0:
#     print("x es cero")
# else:
#     print("x es negativo")
# while
# i = 1
# while i <= 5:
#     print(i)
#     i += 1
# else:
#     i -= 1 
#     print("terminado") 
#     while i >= 1: 
#         print(i) 
#         i -= 1 
# # for
# for i in range(1, 6):
#     print(i)
#     i = 1
# for NUM in range(1, 6, 1):
#     print(NUM)
    
# # # Simular un do-while
# while True:
#     print(i)
#     i += 1  # Incrementar el contador
#     if i > 5:  # Condición para salir del ciclo
#         break

# # Crear un diccionario vacío
# mi_diccionario = {}
# # Crear un diccionario con algunos elementos

# mi_diccionario = {
#     "nombre": "Python",
#     "edad": 30,
#     "version": 3.9
# }# Acceder a valores
# print(mi_diccionario["nombre"])  # Salida: Python
# print(mi_diccionario["edad"])    # Salida: 30
# print(mi_diccionario.get("version"))  # Salida: 3.9
# # print(list(mi_diccionario))
# # print(sorted(mi_diccionario))
# del mi_diccionario["version"]
# print(mi_diccionario)
# print(mi_diccionario.get("pais", "No especificado"))  # Salida: No especificado

# Crear un diccionario
# mi_diccionario = {
#     "nombre": "Python",
#     "edad": 30,
#     "version": 3.9
# }

# # Acceder a un valor
# print(mi_diccionario["nombre"])  # Salida: Python

# # Modificar un valor
# mi_diccionario["edad"] = 31

# # Añadir un nuevo par clave-valor
# mi_diccionario["pais"] = "Global"

# # Iterar sobre claves y valores
# for clave, valor in mi_diccionario.items():
#     print(f"{clave}: {valor}")
# del mi_diccionario["version"]

# print(mi_diccionario)

# listas

# lista = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
# mostrar
# print(lista[1])

# eliminar pop remove del
# lista.remove(3) 
# print(lista)

# modificar
# lista[1:4] = ["martes festivo", "miercoles festivo"]
# print(lista)
# lista.insert(4, "martes festivo")
# lista[2]= "martes festivo"
# print(lista)

# agregar append insert
# lista.append("martes")
# print(lista)
# lista.insert(1, "lunes")
# print(lista)
# lista.extend([3,4])
# print(lista)

# lista2
# lista2=[3, "true", "hola", False, "keiler", "hola"]
# print(lista2.count("hola"))

# listanum=[3,4,1,5,7,2,8,0,9]
# listanum.sort(reverse=True)
# print(listanum)

#bucles en listas
# frut = ["manzana", "banana", "pera"]
# for x in frut:
#   print(x)
# # i = 0
# while i < len(frut):
#   print(frut[i])
#   i = i + 1

#swich def optiones funciones 
# def mesanio(mes):
#     meses ={
#         1:"enero", 
#         2:"febrero",
#         3:"marzo",
#         4:"abril",
#         5:"mayo",
#         6:"junio",
#         7:"julio",
#         8:"agosto",
#         9:"septiembre",
#         10:"octubre",
#         11:"noviembre",
#         12:"diciembre"
#     }
#     return meses.get(mes)
# mese = int(input("ingrese un número del uno al 12 para indicar el mes año: \n ")) 
# print(mesanio(mese))

