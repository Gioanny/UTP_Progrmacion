import random as rd
Vmayor = [] #lista vacia
Vmenor = []
for i in range(10): #inicio de un bucle es con el : el identado es clave
    num = rd.randint(1,10) #numero aleatorio entre 1 y 100
    if num >= 5:
        Vmayor.append(num)
    else:
        Vmenor.append(num)
print(Vmayor)
print(Vmenor)