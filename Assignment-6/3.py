n = float(input("Enter length: "))
print("Possible Units:\nINCHES, FEET,YARDS,MILES,KILOMETRES,METRES,CENTIMETRES,MILLIMETRES")
unit = input("Enter unit: ").lower()
class Converter:
    def __init__(self,n,unit):
        self.factors = {
            'centimetres':0.01,
            'kilometres':1000,
            'inches':0.0254,
            'feet':0.3048,
            'yards':0.9144,
            'miles':1609.34,
            'metres':1,
            'millimetres':0.001
        }
        if unit not in self.factors:
            print("ENter correct Unit!")
            return False
        self.n = n
        self.unit = unit
        self.length_metres = n*self.factors[unit]
    def feet(self):
        print(self.length_metres/self.factors['feet'])
    def inches(self):
        print(self.length_metres/self.factors['inches'])
    def yards(self):
        print(self.length_metres/self.factors['yards'])
    def miles(self):
        print(self.length_metres/self.factors['miles'])
    def kilometres(self):
        print(self.length_metres/self.factors['kilometres'])
    def metres(self):
        print(self.length_metres)
    def centimetres(self):
        print(self.length_metres/self.factors['centimetres'])
    def millimetres(self):
        print(self.length_metres/self.factors['millimetres'])

c = Converter(n,unit)
c.feet()
