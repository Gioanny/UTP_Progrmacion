import random as rd
Vingreso = [] #lista vacia
for i in range(10): #inicio de un bucle es con el : el identado es clave
    Vingreso.append(rd.randint(1,10)) #apppend añede a la lista
print(Vingreso)
Vmayor = []
Vmenor = []
for i in Vingreso:
    if i >= 5:
        Vmayor.append(i)
    else:
        Vmenor.append(i)
print(Vmayor)
print(Vmenor)