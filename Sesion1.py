import datetime as dt #importar funciones - nodulo fecha
import random as rd #importar funciones - modulo aleatorio
nombre = "Gioanny" #constante
fecha= dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S") #salida de variable
#definir valores aleatorios
print("hola " + nombre)
print( fecha)#salida de variable
for i in range(10): #bucle for
    v=rd .randint(0, 1023) #valor aleatorio entre 1 y 100
    if v < 100: #condicional
        print("valor bajo: " + str (v)) #salida de variable
    elif v <500: #condicional
        print("valor medio: " + str (v))#salida de variable
