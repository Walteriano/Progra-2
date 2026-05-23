import math

Bateria = 100


class RobotBase:
    def __init__(self, nombre= str, capacidad_carga= float, Xinicial= 0.0, Yinicial= 0.0, YAWinicial=0.0):
        #atributos privados
        self.__nombre = nombre
        self.__capacidad_carga= capacidad_carga
        self.__pos_x = Xinicial
        self.__pos_y = Yinicial
        self.__yaw = YAWinicial
        self.__basura_recolectada =  0.0
        self.__step_dt = 0.1
        self.__Bateria = Bateria
        #atributos publicos
        self.target_x = 5.0 
        self.target_y = 5.0
    
    #Ahora para acceder a los atributos privados
    def get_nombre(self):
        return self.__nombre
    def get_bateria(self):
        return self.__Bateria
    def get_pos_x(self):
        return self.__pos_x
    def get_pos_y(self):
        return self.__pos_y
    def get_yaw(self):
        return self.__yaw
    def get_basura_recolectada(self):
        return self.__basura_recolectada
    
    #para actualizar pose
    def _actualizar_pose(self, x, y, yaw):
        self.__pos_x = x
        self.__pos_y= y
        self.__yaw = yaw

    #resta bateria para que nunca sea 0
    cantidad : float

    def _reducir_bateria(self, cantidad):
        self.__Bateria -= cantidad
        if self.__Bateria < 0:
            self.__Bateria= 0

    #agregar basura
    def _recolectar_basura(self, cantidad):
        if self.__basura_recolectada + cantidad > self.__capacidad_carga:
            cantidad = self.__capacidad_carga - self.__basura_recolectada

        self.__basura_recolectada += cantidad
        
#metodos estaticos 
#utilice IA para crear las formulas por phyton en el modelo estatico

#modelo estatico 1
    @staticmethod
    def calc_dist_to_goal( pos_x, pos_y, target_x, target_y):
        return math.sqrt((target_x - pos_x)**2 + (target_y - pos_y)**2)

    #modelo estatico 2
    @staticmethod
    def calc_yaw_error(pos_x, pos_y, yaw, target_x, target_y):
        theta= math.atan2(target_y - pos_y, target_x - pos_x)
        err = theta - yaw
        err_norm = ((err + math.pi) % (2 * math.pi)) - math.pi
        return err_norm



    #modelo cinematico
    #use IA para la implementacion de las ecuaciones
    def step(self, v:float, w:float)  ->tuple:
        if self.__Bateria <= 0:
            return 0.0, True
        
        yaw_nuevo = self.__yaw + w * self.__step_dt
        yaw_nuevo = ((yaw_nuevo + math.pi) % (2 * math.pi)) - math.pi
        nuevo_x = self.__pos_x + v * math.cos(yaw_nuevo) * self.__step_dt
        nuevo_y = self.__pos_y + v * math.sin(yaw_nuevo) * self.__step_dt
        self._actualizar_pose(nuevo_x, nuevo_y, yaw_nuevo)

        distancia = self.calc_dist_to_goal(nuevo_x, nuevo_y, self.target_x, self.target_y)
        error_angular = self.calc_yaw_error(nuevo_x, nuevo_y, yaw_nuevo, self.target_x, self.target_y)

        reward = -distancia - abs(error_angular)
        llegamos = False
        if distancia < 0.5:
            llegamos = True
            reward += 100.0  

        return reward, llegamos





    def mover(self):
            raise NotImplementedError("Las clases hijas deben implementar el método mover().")
    def limpiar(self):
            raise NotImplementedError("Las clases hijas deben implementar el método limpiar().") 
            