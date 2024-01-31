import time

class Euristico3:

    def __init__(self, S, D, capacita, costo_setup, domande, costi):
        self.S = S
        self.D = D
        self.capacita = capacita
        self.costo_setup = costo_setup
        self.domande = domande
        self.costi = costi

    def creazione(self):

        capacita_allocata = []
        for i in range(0,self.D):
            capacita_allocata.append(0)

        x = []
        for i in range(0, self.S):
            x.append(0)

        y = []
        for i in range(0, self.S):
            lista = []
            for j in range(0, self.D):
                lista.append(0)
            y.append(lista)

        list_facil = []
        index = 0
        cap = 0

        for j in range(0, self.S):
            if self.capacita[j] > cap:
                cap = self.capacita[j]
                index = j
        list_facil.append(index)   #inserisco il primo facility con capacità più grande
        facilAlloc = 1

        for i in range(0, self.D):
            costo = 10000000
            index = self.S+1
            for j in range(0, facilAlloc):
                if self.costi[list_facil[j]][i] < costo and (capacita_allocata[list_facil[j]]+self.domande[i]) < self.capacita[list_facil[j]]:
                    costo = self.costi[list_facil[j]][i]
                    index = list_facil[j]
            if index == self.S+1:
                cap = 0
                for j in range(0, self.S):
                    if j not in list_facil:
                        if self.capacita[j] > cap:
                            cap = self.capacita[j]
                            index = j
                facilAlloc += 1
                list_facil.append(index)

            capacita_allocata[index] += self.domande[i]
            x[index] = 1
            y[index][i] = 1

        fo = 0
        for i in range(0, self.S):
            fo += x[i] * self.costo_setup[i]

        for i in range(0, self.S):
            for j in range(0, self.D):
                fo += y[i][j] * self.costi[i][j]

        return float(fo)