import joueur
class Bateau:
    def __init__(self, nom):
        self.nom = nom

    def __str__(self):
        return "{}".format(self.nom)

class BlackPearl(Bateau):
    def __init__(self, nom, longeur = 5):
        Bateau.__init__(self, nom)
        self.longeur = longeur

    @property
    def length(self):
        return self.longeur
    def __str__(self):
        return "Capitain {}, le navire {} à une longeur de {}".format(joueur.nom_joueur,self.nom, self.longeur)

class QueenAnneRevenge(Bateau):
    def __init__(self, nom, longeur = 4):
        Bateau.__init__(self, nom)
        self.longeur = longeur

    @property
    def length(self):
        return self.longeur
    def __str__(self):
        return "Capitain {}, le navire {} à une longeur de {}".format(joueur.nom_joueur,self.nom, self.longeur)

class SilentMary(Bateau):
    def __init__(self, nom, longeur = 3):
        Bateau.__init__(self, nom)
        self.longeur = longeur

    @property
    def length(self):
        return self.longeur
    def __str__(self):
        return "Capitain {}, le navire {} à une longeur de {}".format(joueur.nom_joueur,self.nom, self.longeur)

class HmsIntercepteur(Bateau):
    def __init__(self, nom, longeur = 3):
        Bateau.__init__(self, nom)
        self.longeur = longeur

    @property
    def length(self):
        return self.longeur
    def __str__(self):
        return "Capitain {}, le navire {} à une longeur de {}".format(joueur.nom_joueur,self.nom, self.longeur)

class TheDyingGull(Bateau):
    def __init__(self, nom, longeur = 2):
        Bateau.__init__(self, nom)
        self.longeur = longeur
    @property
    def length(self):
        return self.longeur

    def __str__(self):
        return "Capitain {}, le navire {} à une longeur de {}".format(joueur.nom_joueur, self.nom, self.longeur)


black_pearl = BlackPearl("Black Pearl")
queen_anne_evenge = QueenAnneRevenge("Queen Anne's Revenge")
silent_mary = SilentMary("Silent Mary")
hms_intercepteur = HmsIntercepteur("HMS Intercepteur")
the_dying_gull = TheDyingGull("The Dying Gull")

