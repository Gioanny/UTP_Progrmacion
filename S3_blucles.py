import random as rd 
lista =[] #lista vacia
for i in range(5): #inicio de un bucle es con el : el identado es clave
    num = rd.randint(1,10) #numero aleatorio entre 1 y 100
    lista.append(num) #el identado es el espaciado
print(lista) 

vol_sqrt=[]
V = [4.5, 2.32, 4.88]
for i in V:
    vol_sqrt.append(i*i)
print(f"voltaje al cuadrado: {vol_sqrt}")

lecturas = [4.95, 5.10, 4.88]
for idx, vol in enumerate(lecturas,start=1):
    print(f"{idx}: {vol:.2f} V")

#primero crear la lista aleatoria de 10 valores menores a 10V
#verificar si los valores son mayores o menores a 5V
#imprimir en cada caso voltaje alto o bajo