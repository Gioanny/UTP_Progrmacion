valor_txt = input("Introduce los valores de Temperatura en C: ")
try:
    t=float(valor_txt)
    if t >= 30: #condicion if "condicion 1" :
        print("!Alerta! hace mucho calor")
    elif t < 0: #condicion 2" 
        print("temperature bajo 0")
    else:
        print("temperatura normal")
except ValueError:
    print("Entrada invalida. Use numeros (ejemplo: 25.5).")