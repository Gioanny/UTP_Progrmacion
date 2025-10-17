import matplotlib.pyplot  as plt
import numpy as np

def aleatorio(n=20):
        #Docstring
    """permite generar numeros aleatorios de valor entero entre 1 y 30 y da de salida una lista de valores

    Args:
        n (int, optional): numero el datos ingresados. Defecto 20.
    """
    import random as rd
    Value=[] #lista vacia
    for i in range (n): #incio de un bucle es con el : el identado es importante
        Value.append(rd.randint(1,30)) #append añade a la lista\
    return(Value) #lo que devuelve la funcion

ejex=[i for i in range (30)]
ejey=np.sin(aleatorio(30))
ejey2=np.cos(aleatorio(30))
ejey3=np.array(ejey)-np.array(ejey2)

fig,axs = plt.subplots(2,2)
figtitle="grafico comparativo de valores aleatorios"
fig.suptitle(figtitle.upper(),fontdict={'fontweight': 'bold'})
axs[0,0].plot(ejex,ejey,'go--')
axs[0,0].set_title("datos aleatorios 1")
axs[0,1].plot(ejex,ejey2,"rx:")
axs[1,1].set_xlabel("cantidad")
axs[1,1].grid()
plt.show()