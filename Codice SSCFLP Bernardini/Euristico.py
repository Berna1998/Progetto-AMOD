import time

class Euristico:

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

        for i in range(0, self.D):
            costo = 10000000
            index = 0
            for j in range(0, self.S):
                if self.costi[j][i] < costo and (capacita_allocata[j]+self.domande[i]) < self.capacita[j]:
                    costo = self.costi[j][i]
                    index = j
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