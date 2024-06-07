#eleaborar unprograma que jenera la nota definitiva que saca un estudiante al relizar los parciales de una asignatura
#sabiendo que la nota maxima es 5.0
# primer parcial= 2.5%
# segundo parcial=2.0%
#tercer parcial= 5.5%

nombre=input("ingrese su nombre: ")
area=input("ingrese una area: ")
nota1= float(input("ingrse su primera nota\n ")) 
# nota2= float(input("ingrse su nota\n ")) 
# nota3= float(input("ingrse su nota\n ")) 

if(float(nota1 > 5.0)):
    print("Ingrese un numero valido")
else:
    nota2 = float(input("Ingresar su segundo nota:\n "))        
    if(float(nota2 > 5.0)):
        print("Ingrese un numero valido")
    else:    
            nota3 = float(input("Ingresar su tercer nota:\n "))
            if(float(nota3 > 5.0)):
                print("Ingrese un numero valido")  
            else:
                nota1 = nota1
                nota2 = nota2
                nota3 = nota3
                parcialfinal=(nota1*2.5)+(nota1*2.0)+(nota3*5.5)

                print("Su Nombre es: ", nombre, "Su area es: ", area, "Su nota final es de: ", parcialfinal)

                
# if(float(Parcial1 > 5.0 or Parcial2 > 5.0 or Parcial3 > 5.0)):
#     print("Ingrese un numero valido")
# else:        
#     Parcial1 = Parcial1
#     Parcial2 = Parcial2
#     Parcial3 = Parcial3

#     Nota_Final = (Parcial1 * 0.25) + (Parcial2 * 0.20) + (Parcial3 * 0.55)

#     print("Su Nombre es: ", Nombre_Del_Estudiante, "Su Asignatura es: ", Asignatura, "Su nota final es de: ", Nota_Final)
