import math

class Kwadrat:
    def __init__(self, bok):
        self.bok = bok

    def powierzchnia_kwadratu(self):
        return self.bok ** 2
    
    
class Kolo:
    def __init__(self, promien,):
        self.promien = promien
    
    def powierzchnia_kola(self):
        return math.pi * (self.promien ** 2)
