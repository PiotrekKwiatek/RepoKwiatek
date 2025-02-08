import konwenter

predkosc = float(input("Podaj wartosc predkosci: "))
jednostka = input("Podaj jednostke predkosci (km/h, mph): ")

if jednostka == "km/h":
    predkosc_mph = konwenter.kmh_to_mph(predkosc)
    print(f"Predkosc w mph wynosi {predkosc_mph}")
    
elif jednostka == "mph":
    predkosc_kmh = konwenter.mph_to_kmh(predkosc)
    print(f"Predkosc w km/h wynosi {predkosc_kmh}")

else:
    print("Nieznana jednostka predkosci")

