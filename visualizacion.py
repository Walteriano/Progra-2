import numpy as np
import matplotlib.pyplot as plt
def graficar_recoleccion_vs_bateria(resultadosObtenidos:dict):
    nombreRobots=list(resultadosObtenidos.keys())
    basura_total=[resultadosObtenidos[robot]["basura_total"] for robot in nombreRobots]
    consumo_bateria=[resultadosObtenidos[robot]["consumo_bateria"]for robot in nombreRobots]
    
    
    x=np.arange(len(nombreRobots))
    ancho=0.35

    fig,ax=plt.subplots()

    barraBasura=ax.bar(x+ancho/2, basura_total,ancho,label="Basura recolectada", color="green")
    barraConsumo=ax.bar(x-ancho/2, consumo_bateria,ancho,label="Consumo de Bateria",color="red")
    ax.set_title("Rendimiento: Recolección vs Consumo Energético")
    ax.set_ylabel("Cantidad")

    ax.set_xticks(x)
    ax.set_xticklabels(nombreRobots)
    ax.grid()
    ax.legend()
    plt.show()