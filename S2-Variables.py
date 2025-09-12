NOMBRE = "gioanny" #constante por convencion - str
edad = 20          #int
voltaje = 3.14159  #float
activo = True      #bool
#f- string (formato para cadenas de caracteres, letras)
print(f"nombre: {NOMBRE}, edad: {edad}")
#para float se usa {:.5f} para definir el numero de decimales
print(f"voltaje: {voltaje:.5f} V, activo: {activo}")

print(f"tipos -> edad: {type(edad).__name__}, voltaje: {type(voltaje).__name__}")