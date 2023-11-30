class Clatie:
    def __init__(self,lungie,grosime,umplutura):
        self.lungime = lungie
        self.grosime = grosime
        self.umplutura = umplutura

    def __str__(self):
        return f'Clatita facuta de mama are lungimea de {self.lungime} si e umpluta cu {self.umplutura}'

    def __eq__(self, other):
        return self.lungime == other.lungime and self.umplutura == other.umplutura
    def umplu(self):
        if self.umplutura == "ciocolata":
            print(self.umplutura)

a = Clatie(30,2,"ciocolata")
a.umplu(f'gem')
print(a)
class Ciocolata(Clatie):
    def __init__(self,grame_cacao):
        self.grame_cacao = grame_cacao
    def cioco(self):
        if self.grame_cacao > 5:
            print(f'Calitate')
        if self.grame_cacao < 5:
            print(f'Calitate inferioara')

    def __str__(self):
        return f'Clatita contine {self.grame_cacao} de cacao'
c = Ciocolata(8)
print(c)
c.cioco(8)

class Gem(Clatie):
    def __init__(self,fructe):
        self.fructe = fructe
    def __str__(self):
        return f' Clatite cu {self.fructe}'
    def tip_fructe(self):
        if self.fructe == f'capsuni':
            print(f'Avem 3 clatite cu capsuni')
        else:
            print(f'Avem clatite cu fructe de padure')
g = Gem("capsuni")
g.tip_fructe("capsuni")

class Vanilie(Clatie):
    def __int__(self, grad_de_dulce):
        self.grad_de_dulce = [0,0,0,0]

    def foartedulce(self,up):
        for x in range (0,4):
            self.grad_de_dulce[x] += up
            print(self.grad_de_dulce[x])
            print(f'  ')

r = Vanilie(4,5,"vanilie")
print(r)
r.grad_de_dulce(6)


