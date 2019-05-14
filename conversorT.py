class Termometro():
    def __init__(self):
        self.unidadM = 'C'
        self.temperatura = 0
        
    def conversor(self, temperatura, unidad):
        if unidad == 'C':
           return "{}ºF".format(temperatura * 9/5 + 32)
        elif unidad == 'F':
            return "{}ºC".format((temperatura - 32) * 5/9)
        else:
            return "unidad incorrecta"
     
    def __str__(self):
        return "La temperatura en Madrid es: {}º {}".format(self.temperatura, self.unidadM)
        