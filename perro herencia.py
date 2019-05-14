class Dog():
    def __init__(self):
        self.nombre = ""
        self.edad = None
        self.peso = None
        
    def ladrar(self):
        if self.peso == None:
            print("Soy un fantasma")
            
        if self.peso >=8:
            print("GUAO...GUAO...!!!")
        else:
            print("guau...guan...!!!!")
            
            
        
class Perro():
    def __init__(self, nombre, edad, peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        
    def ladrar(self):
        if self.peso >=8:
            print("GUAO...GUAO...!!!")
        else:
            print("guau...guan...!!!!")
            
    def __str__(self):
        return "Perro {}, e: {}, p: {}".format(self.nombre, self.edad, self.peso)
    
    
            
class PerroAsistencia(Perro):
    def __init__(self, nombre, edad, peso, amo, trabajando):
        Perro.__init__(self, nombre, edad, peso)
        self.amo = amo
        self.trabajando = False
        
    def __str__(self):
        return "Perro de Asistencia de {}".format(self.amo)
    
    def pasear(self):
        print("{} ayuda a su dueño : {} a pasear".format(self.nombre, self.amo))
        
    def ladrar(self):
        if self.trabajando:
            print("shhhh, no puedo ladrar")
        else:
            Perro.ladrar(self)
        