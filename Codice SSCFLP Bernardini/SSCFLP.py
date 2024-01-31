import gurobipy as gp
from gurobipy import GRB


class SSCFLP:

    def __init__(self, S, D, capacita, costo_setup, domande, costi):
        self.S = S
        self.D = D
        self.capacita = capacita
        self.costo_setup = costo_setup
        self.domande = domande
        self.costi = costi

    def creazione(self):

        model = gp.Model("SSCFLP")

        # definisco le variabili
        x = []
        for i in range(0, self.S):
            x.append(model.addVar(vtype=GRB.BINARY, name="x[%s]" % i))

        y = []
        for i in range(0, self.S):
            lista = []
            for j in range(0, self.D):
                lista.append(model.addVar(vtype=GRB.BINARY, name="y[%s][%s]" % (i, j)))
            y.append(lista)

        # i vincoli
        # Vincoli sulla capacità
        # Sommatoria su v (yuv)*dv <= ku*xu
        model.addConstrs((sum(y[u][v] * self.domande[v] for v in range(0, self.D)) <= self.capacita[u] * x[u] for u in
                          range(0, self.S)),
                         "capacity")

        # Vincoli sul soddisfacimento della domanda dei clienti
        # Sommatoria su u (yuv) == 1
        model.addConstrs((sum(y[u][v] for u in range(0, self.S)) == 1 for v in range(0, self.D)), "demand")
        # ancora mancano

        # aggiorno il modello
        model.update()

        # definisco la funzione obiettivo
        fo1 = sum(x[i] * self.costo_setup[i] for i in range(0, self.S))
        for i in range(0, self.S):
            fo2 = sum(y[i][j] * self.costi[i][j] for j in range(0, self.D)) #problema nel doppio ciclo
        fo = 0
        fo += fo1
        fo += fo2

        model.setObjective(fo, GRB.MINIMIZE)

        model.update()

        model.optimize()

        if model.status == GRB.OPTIMAL:

            return model.ObjVal




