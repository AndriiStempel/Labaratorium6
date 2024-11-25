#Zdanie 1
import geometria as g
promien = 16
obwod = g.obwod_kola(promien)
pole = g.pole_kola(promien)
print("Obwód koła o promieniu 16: ",obwod)
print("Pole koła o promieniu 16: ",pole,"\n")

#Zdanie 2 
import temperatura as t
celsius_to_fahrenheit = t.c_to_f(21)
fahrenheit_to_celsius = t.f_to_c(89)
celsius_to_kelvin = t.c_to_k(35)

print(f"21 stopni Celsjusza to {celsius_to_fahrenheit:}: stopni Fahrenheita.")
print(f"89 stopni Fahrenheita to {fahrenheit_to_celsius:}: stopni Celsjusza.")
print(f"35 stopni Celsjusza to {celsius_to_kelvin}: Kelwinów.","\n")

#Zdanie 3
import fmat
from fmat import kwadrat, szescian, dodaj

print(f"Kwadrat twojej liczby będzie wynosić: {kwadrat(10)}")
print(f"Sześcian twojej liczby będzie wynosił: {szescian(3)}")
print(f"dodanie twoich liczb będzie:{dodaj(10,5)}\n")

#Zdanie 4
import random

szczesliwa_liczba = random.randint(1, 100)
print(f"Twoja szczęśliwa liczba to: {szczesliwa_liczba}\n")

roczniki = [1990, 1995, 1996, 2000, 2002, 2006, 2007, 2010]
szczesliwy_rocznik = random.choice(roczniki)
print(f"szczesliwy_rocznik: {szczesliwy_rocznik}\n")

#Zdanie 5
liczby = list(range(1, 50))
wylosowane_kule = random.sample(liczby, 6)

print("Wylosowane liczby Dużego Lotka to:", sorted(wylosowane_kule),"\n")

#Zdanie 6
import time
czas = int(input("Podaj czas w sc: "))
for secund in range(czas,0,-1):
    print(f"Pozostało {secund} secund:")    
    time.sleep(1)
print("Końiec obliczania\n")

#Zdanie 7
from datetime import datetime
data_laboratoriow = datetime(2024, 11, 19)

data_kolokwium = datetime(2024, 12, 17)

obecna_data = datetime.now()

dni_od_laboratoriow = (obecna_data - data_laboratoriow).days

dni_do_kolokwium = (data_kolokwium - obecna_data).days


miesiace = {
    1: "stycznia", 2: "lutego", 3: "marca", 4: "kwietnia", 5: "maja", 6: "czerwca",
    7: "lipca", 8: "sierpnia", 9: "września", 10: "października", 11: "listopada", 12: "grudnia"
}

print(f"Dziś jest {obecna_data.day} {miesiace[obecna_data.month]} {obecna_data.year}.")
print(f"Od ostatnich laboratoriów minęło {dni_od_laboratoriow} dni.")
print(f"Do kolokwium zostało {dni_do_kolokwium} dni.\n")


#Zadanie 8
import keyword
lista = ["for", "print", "break", "done", "bad"]
for słowo in lista:
    if keyword.iskeyword(słowo):        
        print(f"{słowo} jest slowom kluczowym")
    else:        
        print(f"{słowo} jest slowom kluczowym\n\n")

#Zadanie 9
print(dir(time))

#Zadanie 10
import random
from math import prod, pow

dolny_zakres = int(input("Podaj dolny zakres przedziału: "))
gorny_zakres = int(input("Podaj górny zakres przedziału: "))

krotka = tuple(random.randint(dolny_zakres, gorny_zakres) for _ in range(10))

srednia_geometryczna = pow(prod(krotka), 1/len(krotka))

print(f"Wylosowana krotka: {krotka}")
print(f"Średnia geometryczna krotki: {srednia_geometryczna:}")


