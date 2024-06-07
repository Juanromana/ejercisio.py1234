estudiante={
    'masculino':['juan', 'david', 'pedro'],
    'femenino':['heidi', 'yulieth', 'marta']
}
for i in estudiante.keys():
    for nombre in estudiante[i]:
        if 'a' in nombre:
            print(nombre)