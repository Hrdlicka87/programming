class Programator: #<-definice tridy
    proselPripravou = True #<-atribut
    absolvoval = False
    vek = 33

    def __init__(self, proselPripravou, absolvoval, vek):
        self.proselPripravou = proselPripravou
        self.absolvoval = absolvoval
        self.vek = vek

    def absolvuj(self): #<-metoda
        self.absolvoval = True
 
karel = Programator(True, False, 40) #<-vytvoreni instance
michal = Programator(True, True, 36)
print(karel.vek)

print(karel.proselPripravou)
karel.absolvuj() #<-volani metody pro instanci
print(karel.absolvoval)

class Webar(Programator):
    def __init__(self, proselPripravou, absolvoval, vek, specializace):
        # self.proselPripravou = proselPripravou
        # self.absolvoval = absolvoval
        # self.vek = vek #<-moc kodu, zkratime volanim konstruktoru nadrizene tridy
        super().__init__(proselPripravou, absolvoval, vek)
        self.specializace = specializace

pepa = Webar(True, True, 26, "Javascript")
print(f"Pepova specializace je {pepa.specializace}")
igor = Webar(True, False, 33, "PHP")
print(f"Tady je hodnota atributu 'absolvoval' u Igora jeste puvodni: {igor.absolvoval}")
igor.absolvuj()
print(f"Tady je hodnota atributu 'absolvoval' jiz zmenena: {igor.absolvoval}")