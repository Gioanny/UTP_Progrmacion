Codigo21211=["Juan",35,"Ingenieria de Sistemas",976555555,]#lista CAMBIA
print(f"la edad de {Codigo21211[0]} es :  {Codigo21211[1]}  y su numero es el {Codigo21211[3]}")

CodJefe=("Pedro",45,"Administrador",976222225,)#tupla no cambia
print(f"la edad de {CodJefe[0]} es :  {CodJefe[1]}  y su numero es el {CodJefe[3]}")

Codnuevo={"nombre":"Ricardo" ,"edad":30,"Carrera":"Programador","telefono":976333333,}
print(Codnuevo["nombre"])
print(Codnuevo["edad"])
Codnuevo["nombre"]="Juaneco"
print(Codnuevo["nombre"])
Cod001={"nombre":"Ricardo" ,"edad":30,"Carrera":"Programador","telefono":976333333,}
Cod002={"nombre":"Luis" ,"edad":32,"Carrera":"Contador","telefono":976555555,}
Central={"Ricardo":Cod001,"Luis":Cod002}
Empresa=(Central["Luis"])
print(Empresa)