class Kalkulator:

    def __init__(self, a, b):
        self.a = a
        self.b = b  

    def mnozenie(self):
        return self.a * self.b
    
    def pierwiastek(self):
        return self.a ** 0.5
        return self.b ** 0.5
    
    def dodawanie(self):
        return self.a + self.b
    
    def odejmowanie(self):
        return self.a - self.b
    
    def dzielenie(self):
        if self.b == 0:
            return "Nie dziel przez 0"
        return self.a / self.b      
    
    
a = 3
b = 4
    

print("Wynik mnozenia to: ", Kalkulator(a,b).mnozenie())  
print("Pierwiastek z a to: ", Kalkulator(a,b).pierwiastek())
print("Pierwiastek z b to: ", Kalkulator(a,b).pierwiastek())
print("Wynik dodawania to: ", Kalkulator(a,b).dodawanie())
print("Wynik odejmowania to: ", Kalkulator(a,b).odejmowanie())
print("Wynik dzielenia to: ", Kalkulator(a,b).dzielenie())
