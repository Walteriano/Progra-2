import numpy as np


def comparar_rendimiento(datos:list)  ->dict:
    matrizObtenida=np.array(datos)

    nombresUnicos=np.unique(matrizObtenida[:,1])
    resultadosObtenidos={}
    for nombre in nombresUnicos:
        operacion=matrizObtenida[:,1]==nombre
        filaRobot=matrizObtenida[operacion]
        
        
        baterias=filaRobot[:,4].astype(float)
        basura=filaRobot[:,5].astype(float)
        
        
        ultimoValorBATERIA=baterias[-1]
        consumoBateria=100-ultimoValorBATERIA
        basuraTotal=basura[-1]
        if consumoBateria==0:
            eficiencia=0
        else:
            eficiencia=basuraTotal/consumoBateria
        resultadosObtenidos[nombre]={
            "consumo_bateria":float(consumoBateria),
            "basura_total":float(basuraTotal),
            "eficiencia":float(eficiencia)
            }
    return resultadosObtenidos
