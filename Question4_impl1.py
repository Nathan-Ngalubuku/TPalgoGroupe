""" TRAVAIL FAIT PAR LES MEMBRES DU GROUPE 17 A SAVOIR : NGALUBUKU, RUKENGEZA, SHUKANYA"""

""" QUESTION NUMERO 4 """

class Geometrie(): # Creation de la classe qui exploite les classes des diffentes formes geo pour fournir le perimetre et la surface de celles-ci
    try:
        def __init__(self):
            self.gGeo_rep = []
        def add(self, fig):
            self.gGeo_rep.append(fig)
        def descript(self):
            for g in self.gGeo_rep:
                print("Soit {}\nLe Perimetre est : {}\nLa Surface est : {}".format(g.name, g.perimeter(), g.surface()))
    except:
        print(" ERREUR SUR LE PARAMETRE INSERER . ")