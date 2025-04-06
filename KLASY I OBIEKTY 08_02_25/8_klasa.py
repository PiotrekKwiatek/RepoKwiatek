class Samochod:
    #deifincja klasy
    def __init__(self, marka, model):
        #self reprezentuje nowo tworzona instacje/obiekt
        self.marka = marka #ustawiamy atrybut 'marka' obiektu
        self.model = model #ustawiamy atrybut 'model' obiektu
        self.predkosc = 0 #predkosc poczatkowa samochodu to 0 km/h
        self.wlaczony_silnik = False #silnik poczatkowo wylaczony
        self.kolor = "Czarny"

    def uruchom_silnik(self):
        print("Silnik zostal uruchomiony")
        self.wlaczony_silnik = True
    
    def przyspiesz(self, wartosc):
        self.predkosc += wartosc
    
moj_samochod = Samochod("Ford", "Fiesta")

moj_samochod.uruchom_silnik()
moj_samochod.przyspiesz(50)

print(moj_samochod.predkosc)
print(moj_samochod.wlaczony_silnik)

moj_samochod_2 = Samochod("Opel", "Astra")  
moj_samochod_2.uruchom_silnik()

print (moj_samochod_2.wlaczony_silnik)