#Busca la ruta donde esta el codigo y luego se añade la ruta del archivo de ingreso
from pathlib import Path
ROOT = Path(__file__).resolve().parents[0] # sube desde src/ a la raiz del proyecto C:\Users\Gioanny\UTPPHYTON\UTP_Progrmacion\
TXT = ROOT / "archivos" / "mediciones_basico.txt"

valores=[]
with open(TXT, 'r',encoding='"utf-8"') as f:
    for linea in f: #lee la linea del archivo ingresado
        s=linea.strip() 
        if not s or s.startswith("#"):
            continue
        if not s or s.startswith("!"):
            continue
        s= s.replace (",",".")  #cambia la coma por punto
        try:
                valores.append(float(s)) 
        except ValueError:
                #si no es mi linea mi numero, debe saltarlo
                pass
        

Vmayor = [] 
Vmenor = []
for i in valores:
    if i >= 5:
        Vmayor.append(i)
    else:
        Vmenor.append(i)
print(Vmayor)
print(Vmenor)

print(len(Vmayor))
print(len(Vmenor))