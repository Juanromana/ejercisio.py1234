# variables acumuladoras y controladoras
Con_Admin = 0
Con_Derecho = 0
Con_Sistema = 0
Con_Medicina = 0
MujerSiste = 0
SalAdmini = 0
SalMedic = 0
EdadMaysale = 0
P = 0
# ciclo que repite para encuestar varios alumnos
while (P != 2):
    conta = 0
    while(conta == 0):
        try:
            Cedula = input("Ingrese su cedula: \n")
            conta = 1
        except:
            print("Porfavor, Ingresar una cedula valida.")

    Nombre = input("Ingrese su nombre: \n")
    conta = 0
    while(conta == 0):
        try:
            Salario = int(input("Ingrese su salario: \n"))
            conta = 1
        except:
            print("Porfavor, Ingresar un valor valido.")
    conta = 0

    while(conta == 0):   
        try:     
            Edad = int(input("Ingrese su Edad: \n"))
            conta = 1
        except:
            print("Porfavor, Ingresar un valor valido.")

    conta = 0
    while(conta == 0):
        try:
            Sexo = int(input("Ingrese su sexo, 1 Para Femenino, 2 Para Masculino: \n"))
            conta = 1
        except:
            print("Porfavor, Ingresar una opcion valida.")
    conta = 0
    while(conta == 0):
        try:
            Estado_Civil = int(input("Ingrese su estado civil | 1 Para casado | 2 Para Soltero | 3 Para divorciado: \n"))
            conta = 1
        except:
            print("Porfavor, Ingresar una opcion valida.")
    Carrera = int(input("1 para administracion 2 para derecho 3 para medicina y 4 para sistema: \n"))
    # ciclo para calcular y aunmentar el numero de alumnos por carreras
    conta=0
    while(conta ==0):
        if(Carrera == 1):
            Con_Admin = Con_Admin + 1
            SalAdmini=Salario + SalAdmini
            conta = 1
        elif(Carrera == 2):
            Con_Derecho= Con_Derecho + 1
            conta = 1
        elif(Carrera == 3):
            Con_Medicina = Con_Medicina + 1
            if(Salario > SalMedic):
                SalMedic= Salario + SalMedic
                EdadMaysale= Edad
            conta = 1
        elif(Carrera==4):
            Con_Sistema = Con_Sistema + 1
            if(Sexo == 1):
                MujerSiste = MujerSiste + 1
            conta = 1
        else:
            Carrera=int(int("por favor escoja una odcion valida"))
    P = int(input("desea continuar? 1 si 2 no: \n" ))
    if(P == 2):
        P = 2 

# Mostrar total de alumnos por carrera
if(Con_Admin > 0):
    print("Total de alumnos en administración: ", Con_Admin) 
else:
    print("No hubieron alumnos en la carrera de administración")

if(Con_Derecho > 0):
    print("Total de alumnos en derecho: ", Con_Derecho) 
else:
    print("No hubieron alumnos en la carrera de Derecho")

if(Con_Medicina > 0):
    print("Total de alumnos en medicina: ", Con_Medicina) 
else:
    print("No hubieron alumnos en la carrera de medicina")

if(Con_Sistema > 0):
    print("Total de alumnos en sistema: ", Con_Sistema) 
else:
    print("No hubieron alumnos en la carrera de sistema")

# mostrar crrera con mas alunnos
if(Con_Admin > Con_Derecho and Con_Admin > Con_Sistema and Con_Admin > Con_Medicina):
    print("Administracion es la carrera com mas alumno, con:", Con_Admin, "Alumnos")
elif(Con_Derecho > Con_Admin and Con_Derecho > Con_Medicina and Con_Derecho > Con_Sistema):
    print("Derecho es la carrera com mas alumno, con:", Con_Derecho, "Alumnos")
elif(Con_Sistema > Con_Admin and Con_Sistema > Con_Derecho and Con_Sistema > Con_Medicina):
    print("Sistemas es la carrera com mas alumno, con:", Con_Sistema, "Alumnos")
elif(Con_Medicina > Con_Derecho and Con_Medicina > Con_Admin and Con_Medicina > Con_Sistema):
    print("Medicinaes la carrera com mas alumno, con:", Con_Medicina, "Alumnos")
else:
    print("las correras estan igual de alumnos")

# salrio de los alumnos de administracion
if(Con_Admin > 0):
    print("promedio de los alumnos de administracion es de: ", SalAdmini/Con_Admin, "$")
else:
    print("no hay alumnos de administacion")
# porcentaje de mujeres en la carrera de sistemas
if(MujerSiste > 0):
    print("El porcentaje de mujeres en la carrera de sistemas es de un: ", (MujerSiste/Con_Sistema)*100, "%")
else:
    print("No hubieron mujeres en la carrera de sistemas")
# edad de los alumnos de medicina
if(Con_Medicina > 0):
    print("La edad de la persona con mayor salario en medicina es de: ", EdadMaysale, "Años")
else:
    print("No hubieron alumnos en medicina")
