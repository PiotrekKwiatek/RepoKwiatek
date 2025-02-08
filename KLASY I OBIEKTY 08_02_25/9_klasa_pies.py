class Pies:
    def __init__(self, nazwa, wiek):
        self.nazwa = nazwa
        self.wiek = wiek

    def szczekaj(self):
        print(f"{self.nazwa} szczeka")

    def przelicz_wiek(self):
        return self.wiek * 7


pies_1 = Pies("Burek", 3)

pies_1.szczekaj() 
print(pies_1.wiek)
print(pies_1.przelicz_wiek())
print(pies_1.szczekaj())
   