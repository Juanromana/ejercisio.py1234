dias_laborados = int(input("Ingrese el número de días laborados: "))    
salario = 136000* dias_laborados

if (salario >= 1088000 and dias_laborados <=14):
    salario = salario + 60000
if (dias_laborados > 15):
    salario = (salario * 0.10) + salario
if dias_laborados == 30:
    salario = (salario * 0.20 ) + salario

print("por sus ",dias_laborados ,'dias laborates su salario es:')
print("Salario Total:" ,salario)