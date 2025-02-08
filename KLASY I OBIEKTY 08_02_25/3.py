import random #importujemy modul do losowania liczb

#wylosujemy liczbe z przedziału 1 do 10

losowa = random.randint(1, 10)
print("Wynik losowania z liczb z zakresu 1 do 10 to: ", losowa)


#wylosujemy 5 licz z zakresu od 1 do 10 i zapiszmy je do listy

lista_losowych = random.sample(range(1, 11), 5)

print("Lista liczb wylosowanych za zakresu 1 do 10 to ", lista_losowych)