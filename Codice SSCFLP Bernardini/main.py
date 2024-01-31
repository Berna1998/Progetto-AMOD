import os
import time
from Euristico import Euristico
from SSCFLP import SSCFLP
from Euristico2 import Euristico2
from Euristico3 import Euristico3


def writeFile(lis):

    file = open("dati.csv","w")
    num_file = int(len(lis)/9)
    x = 0
    file.write("File;F.O. SSCFLP;Tempo SSCFLP;F.O. Euristica 1;Tempo Euristica 1;F.O. Euristica 2;Tempo Euristica 2;F.O. Euristica 3;Tempo Euristica 3\n")
    for i in range(num_file):
        file.write(str(lis[x]))
        file.write(";")
        file.write(str(lis[x+1]))
        file.write(";")
        file.write(str(lis[x+2]))
        file.write(";")
        file.write(str(lis[x+3]))
        file.write(";")
        file.write(str(lis[x+4]))
        file.write(";")
        file.write(str(lis[x+5]))
        file.write(";")
        file.write(str(lis[x+6]))
        file.write(";")
        file.write(str(lis[x+7]))
        file.write(";")
        file.write(str(lis[x+8]))
        file.write("\n")
        file.flush()
        x = x + 9
    file.close()
def createIstances():
    dir = os.listdir('./Yang_Istances')
    lis = []

    for path in dir:

        num_path = path
        path = os.listdir('./Yang_Istances/'+path)
        for ist in path:
            S = 0  # inizializzo il numero di possibili fornitori
            D = 0  # inizializzo il numero di clienti
            capacita = []
            costo_setup = []
            domande = []
            costi = []
            lis.append(ist)
            file = open("./Yang_Istances/" + num_path + "/" + ist, "r")
            riga = file.readline()
            S, D = riga.split()  # con split io leggo di una riga i due numeri saltando gli spazi

            for i in range(0, int(S)):  # in S righe ho di ogni deposito costo di setup e capacita'
                riga = file.readline()
                cap, set = riga.split()
                capacita.append(int(cap))
                costo_setup.append(int(set))

            riga = file.readline()  # in una riga ho tutte le domande dei clienti
            for i in range(0, int(D)):
                domande.append(int(riga.split()[i]))

            for i in range(0, int(S)):  # in S righe ho per ogni deposito D costi di ogni cliente con quel deposito
                riga = file.readline()
                list = []
                for j in range(0, int(D)):
                    list.append(int(riga.split()[j]))
                costi.append(list)

            start = time.time() #prendo il tempo in cui inizio ad eseguire il modelo con Gurobi
            istance = SSCFLP(int(S),int(D),capacita,costo_setup,domande,costi) #creo l'istanza del modello
            fo = istance.creazione()
            end = time.time() #prendo il tempo in cui termino di eseguire il modello con Gurobi
            current = end - start
            lis.append(fo)
            lis.append(round(current,2))

            start = time.time()#prendo il tempo in cui inizio ad eseguire la prima euristica
            euri = Euristico(int(S),int(D),capacita,costo_setup,domande,costi)
            fo = euri.creazione()
            end = time.time() #prendo il tempo in cui termino l'esecuzione della prima euristica
            current = end - start
            lis.append(fo)
            lis.append(round(current, 2))

            start = time.time()#prendo il tempo in cui inizio ad eseguire la seconda euristica
            euri2 = Euristico2(int(S),int(D),capacita,costo_setup,domande,costi)
            fo = euri2.creazione()
            end = time.time() #prendo il tempo in cui termino l'esecuzione della seconda euristica
            current = end - start
            lis.append(fo)
            lis.append(round(current, 2))

            start = time.time()#prendo il tempo in cui inizio ad eseguire la terza euristica
            euri3 = Euristico3(int(S),int(D),capacita,costo_setup,domande,costi)
            fo = euri3.creazione()
            end = time.time() #prendo il tempo in cui termino l'esecuzione della terza euristica
            current = end - start
            lis.append(fo)
            lis.append(round(current, 2))

    writeFile(lis)


if __name__ == '__main__':

    createIstances()