#Importamos libreria random
import random


#Importamos la clase padre
from robot_base import RobotBase


#Creamos clase que hereda nombre y radio_rueda de la clase padre

class RobotTresRuedas(RobotBase):

    def __init__(self, nombre, radio_rueda):
        super().__init__(nombre = nombre,capacidad_carga=20) #Llama a la clase padre
        self.ruedas_calibradas= False
        self.radio_rueda= radio_rueda

    #Definimos metodo calibrar giro
    #     
    def calibrar_giro(self):
        print(f"Se esta calibrando el triciclo con su radio de rueda...")
        self.ruedas_calibradas= True


    #Definimos metodo step
    def mover(self) ->tuple:
        return self.step(v=0.8, w=0.2)
    
    #Definimos limpiar 
    def limpiar(self):
        self._reducir_bateria(2.0) #Reduce la bateria en 2.0
        cantidad_basura = random.uniform(0.5, 1.5) #Cantidades al azar entre 0.5 y 1.5 kg
        self._recolectar_basura(cantidad_basura) 
    

class RobotOruga(RobotBase):

    def __init__(self, nombre, tension_oruga):
        super().__init__(nombre = nombre,capacidad_carga=50.0)
        self.tension_oruga = tension_oruga

    def ajustar_tension(self):
        print (f"Tension actual:{self.tension_oruga}")
    
    def mover(self) ->tuple:
        return self.step(v=0.3, w=0.8)
    
    def limpiar(self):
        self._reducir_bateria(4.5)
        cantidad_basura = random.uniform(2.0, 4.0)
        self._recolectar_basura(cantidad_basura)




class RobotDron(RobotBase):

    def __init__(self, nombre, altura_maxima):
        super().__init__(nombre = nombre,capacidad_carga=5.0)
        self.en_vuelo = False
        self.altura_maxima= altura_maxima



    def despegar(self):
        self.en_vuelo= True
        print (f"Altura maxima:{self.altura_maxima}")


    def mover(self)->tuple:
        if self.en_vuelo:
            return self.step(v=2.5, w=1.0)
        else:
            return 0.0, False
    


    def limpiar(self):
        if self.en_vuelo:
            self._reducir_bateria(3.0)
            cantidad_basura = random.uniform(0.1, 0.4)
            self._recolectar_basura(cantidad_basura)
        else:
            print("No se puede limpiar, el dron no esta en vuelo")







