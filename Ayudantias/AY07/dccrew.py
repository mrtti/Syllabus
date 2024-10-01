import threading
from random import choice, randint
from time import sleep


class DCCrew:

    def __init__(self, meta):
        self.meta = meta
        self.__actual = 0
        self.evento_terminar = threading.Event()
        self.lata_plateada = threading.Lock() 

    @property
    def actual(self):
        return self.__actual

    @actual.setter
    def actual(self, valor):
        if valor > self.meta:
            self.__actual = self.meta
            self.terminar() # Se levanta la señal de fin
        else:
            self.__actual = valor

    def terminar(self):
        # Levanta la señal para avisar a los threads que deben terminar
        self.evento_terminar.set()



# completar
class Graffitero(threading.Thread):
    lock_imprimir = threading.Lock()

    def __init__(self, nombre, descanso, crew):
        super().__init__(name=nombre, daemon=True)
        self.crew = crew
        self.nombre = nombre
        self.contador = 0
        self.descanso = descanso
        self.mensajes = []
        self.leer_mensajes("mensajes.txt")


    def leer_mensajes(self, ruta):
        with open(ruta, "r") as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                self.mensajes.append(linea.rstrip("\n"))


    def leer_mensajes(self, ruta):
        with open(ruta, "r") as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                self.mensajes.append(linea.rstrip("\n"))


    def bomba(self):
        self.imprimir(f"{self.nombre} BOMBA!: ¡DCCrew!")


    def mensaje(self):
        escogido = choice(self.mensajes)
        self.imprimir(f"{self.nombre} MENSAJE!: {escogido}")


    def graff(self):
        escogido = choice(["bomba", "mensaje"])
        if escogido == "bomba":
            self.bomba()
        elif escogido == "mensaje":
            self.mensaje()


    def especial(self):
        with self.crew.lata_plateada:
            sleep(randint(1,10))
            self.imprimir(f"\n{self.nombre} ESPECIAL CHROMADO!: DCCrew {self.crew.meta}GRAFFS!!\n")


    def imprimir(self, string):
        with self.lock_imprimir:
            print(string)
            
            
    def run(self):
        # Se verifica que la señal no ha sido levantada
        while not self.crew.evento_terminar.is_set():
            self.crew.actual += 1
            self.contador += 1

            if (self.contador % 10) == 0:
                self.especial()
            else:
                self.graff()
            # descansa
            sleep(self.descanso)


def gira(crew):
    print(f"INICIANDO LA GIRA GRAFFITERA META: {crew.meta} graffs\n")

    julio = Graffitero("BigJules", 0.7, crew)
    felipe = Graffitero("LilPeepe", 0.8, crew)
    diego = Graffitero("McToledo", 0.7, crew)
    ale = Graffitero("SupaMax", 0.8, crew)
    cleme = Graffitero("Demente", 0.7, crew)

    julio.start()
    felipe.start()
    diego.start()
    ale.start()
    cleme.start()

    julio.join()
    felipe.join()
    diego.join()
    ale.join()
    cleme.join()

    # Solo para que se vea bonito
    mensaje1 = f" !!! META LOGRADA {crew.meta} GRAFFITIS HECHOS !!! "
    mensaje2 = " !!! LARGA VIDA A LA DCCREW !!! "
    print(f"\n\n{mensaje1.center(50)}\n")
    print(f"{mensaje2.center(45)}\n")


crew = DCCrew(10)
principal = threading.Thread(target=gira, args=(crew,))
principal.start()