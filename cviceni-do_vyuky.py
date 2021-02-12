#Vypište do konzole následující vzor. Zkuste to udělat tak, aby program měl jenom dva řádky.  
# for i in range(1,6):
#     print((str(i) + " ") *(i))

#Trochu hardcore obměna, opět dvěma řádky: 
# for i in range(1,6):
#     print((str(6-i) + " ") *(6-i))

#Vygenerujte 20 čísel do pole, vytáhněte z něj min, max, spočítejte průměr.  
#Na závěr vraťte z pole poslední prvek. (udělejte to tak, abyste v případě, že najednou stoupne počet požadovaných čísel, museli změnit program jen v 1 místě)  
# import random 
# pole = []
# s=""
# for i in range(0, 20):
#     cislo = random.randint(1, 100)
#     pole.append(cislo)
#     s+= str(cislo) + " "
# print(pole)
# print(max(pole))
# print(min(pole))
# print(sum(pole)/len(pole))
# print(pole[-1])

#Vyžádejte si od uživatele číslo a vypočtěte součet všech čísel od 1 do toho čísla 
#Test case: 10 musí vrátit 55 
# cislo = int(input("Zadejte cislo: "))
# soucet = 0
# for i in range(1, cislo+1):
#     soucet+=i
# print(soucet)

#Vyžádejte si od uživatele číslo a vypište jeho počet číslic.  
#(jde to dvěma řádky) 
# cislo = input("Zadej cislo: ")
# print(len(cislo))

#Vytvořte dva seznamy zákazníků, připojte je za sebe a pak je zobrazte seřazené podle abecedy (není nutno každého na zvláštní řádek).
# zakosi1 = ["Jan", "Amos", "Karel"]
# zakosi2 = ["Kamila", "Marie", "Eva"]
# zakosi1.extend(zakosi2)
# zakosi1.sort()
# print(zakosi1)

#Vygenerujte náhodně 2x20 čísel od 1 do 6 (hody 2 kostkami) a sečtěte oka z každého hodu.  
#(který součet je nejčastější hodnotou?) 
# import random
# kostky1 = []
# kostky2 = []
# for i in range(0,20):
#     kostky1.append(random.randint(1,6))
#     kostky2.append(random.randint(1,6))
# print(kostky1)
# print(kostky2)
# soucty = []
# for j in range(0,len(kostky1)):
#     soucty.append(kostky1[j] + kostky2[j])
# print(soucty)

#Dejte programu seznam (je celkem jedno čeho) a vypište, pokud je první a poslední prvek listu stejný (dá se dvěma způsoby) 
# seznam = [1, 2, 4, 5, 7, 4, 0]
# if(seznam[0]==seznam[-1]):
#     print("Prvni a posledni prvek jsou stejne")
# else:
#     print("Prvni a posledni prvek nejsou stejne")

#Dejte programu list čísel, projeďte ho a vytiskněte jen ta, co jsou dělitelná 5. 
# cisla = [2, 8, 5, 6, 10, 26, 25, 12]
# for cislo in cisla:
#     if(cislo%5==0):
#         print(cislo)

#Funkce
#Vytvořte funkci, která si vezme jako parametr string a vrátí počet samohlásek v něm.  
#prvni definuju funkci a pak ji teprve volam!
# def spocitejSamohlasky(ret):
#     pocetSamohlasek = 0
#     samohlasky = ["a", "e", "i", "o", "u", "y"]
#     for i in range(0, len(ret)):
#         for j in range(0, len(samohlasky)):
#             if ret[i]==samohlasky[j]:
#                 pocetSamohlasek+=1
#     return pocetSamohlasek
# ret = input("Zadej retezec: ")
# pocetS = spocitejSamohlasky(ret)
# print(f"Pocet samohlasek je {pocetS}.")

# Vytvořte funkci, která vezme jméno a příjmení osoby a vrátí ho v inverzi (prvně příjmení)
# def prohod(jm):
#     casti = jm.split(" ")
#     inv = casti[1]+" " +casti[0]
#     return inv
# jmeno = input("Zadej nejake jmeno a prijmeni: ")
# print(prohod(jmeno))

#Vytvořte funkci, které předáte datum jako řetězec a která vyhodnotí, jestli jsou Vánoce nebo ne. (šlo mi jenom s řetězcem) 
# def zjistiVanoce(d):
#     denmesicrok = d.split(".")
#     if ((denmesicrok[0]=='24') and (denmesicrok[1]=='12')):
#         print("Jsou Vanoce!")
#     else:
#         print("Jeste nejsou Vanoce")
# dnes = input("Zadej dnesni datum: ")
# zjistiVanoce(dnes)

#Parta kamarádů se rozhodla založit tajnou společnost. Vytvořte funkci, která vezme jako parametr list jmen a vrátí název tajné společnosti složený z prvních písmen jejich členů, seřazených podle abecedy.  
# def vratSpolecnost(clenove):
#     clenove.sort()
#     spolecnost = ""
#     for clovek in clenove:
#         spolecnost+=clovek[0]
#     return spolecnost
# lidi = ["Michal", "Adam", "Zdenek", "Karel"]
# print(vratSpolecnost(lidi))

#Napište program, který spočítá ve stringu počet písmen a číslic (zvlášť).
# def spocitej(retezec):
#     pismenka = 0
#     cisla = 0
#     for i in range(0, len(retezec)):
#         if(retezec[i].isalpha()):
#             pismenka+=1
#         else:
#             cisla+=1
#     print(f"retezec obsahuje {pismenka} pismen a {cisla} cislic")
# vstup = input("Zadej retezec pismen a cislic: ")
# spocitej(vstup)


# class Consumer():
#     def __init__(self, wealth):
#         self.wealth = wealth
    
#     def earn(self, howMuch):
#         self.wealth+=howMuch
    
#     def spend(self,howMuch):
#         self.wealth-=howMuch
    
# zak = Consumer(300)
# zak.earn(100)
# print(zak.wealth)
# zak.spend(200)
# print(zak.wealth)



# class Zamestnanec():
#     def __init__(self, jmeno, prijmeni):
#         self.jmeno = jmeno
#         self.prijmeni = prijmeni
#         self.cele = f"{self.jmeno.capitalize()} {self.prijmeni.capitalize()}"
#         self.email = f"{self.jmeno.lower()}.{self.prijmeni.lower()}@firma.cz"
    
#     def __str__(self):
#         return f"Zamestnanec jmenem {self.cele} ma e-mail {self.email}."
    

# karel = Zamestnanec("Karel", "Novak")
# franta = Zamestnanec("Franta", "Voprsalek")
# print(karel)
# print(franta)

# class Computer:
#     def __init__(self, barva, vyrobce):
#         self.barva = barva
#         self.vyrobce = vyrobce
#         self.os = ""

#     def install_os(self, novy_os):
#         self.os = novy_os

#     def which_os(self):
#         return self.os

# c = Computer("black", "lenovo")
# print(c.which_os())

# class Notebook(Computer):
#     def __init__(self, barva, vyrobce, vaha):
#         super().__init__(barva, vyrobce)  
#         self.vaha = vaha   

# c1 = Notebook("silver", "Lenovo", 3)
# c2 = Notebook("white", "Dell", 4)
# print(c1.barva) # silver
# print(c2.barva) # white
# print(c1.vyrobce) # Apple
# print (c2.vyrobce) # Apple

# c1.install_os("OS X")
# print(c1.os) # OS X
# print(c2.os) # ""