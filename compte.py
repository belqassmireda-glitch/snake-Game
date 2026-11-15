class Compte:
    _compte_compteur = 100
    def __init__(self, solde_initial=0):
        Compte._compte_compteur += 1
        self.numero = Compte._compte_compteur
        self.solde = solde_initial
    def deposer(self, montant):
        if montant > 0:
            self.solde += montant
            print("Depot effectue")
        else:
            print("Le montant doit etre positif")
    def afficher_solde(self):
        return f"Compte n {self.numero} | solde:{self.solde}"

class CompteCourant(Compte):
    def __init__(self,solde_initial = 0, limite_decouvert= -500):
        super().__init__(solde_initial)
        self.limite_decouvert = limite_decouvert
    def retirer(self,montant):
        if self.solde - montant <= self.limite_decouvert:
            self.solde -= montant
            print("Retrait effectué!")
        else:
            print("Refisé limite decouverte depassée!")
class CompteEpargne(Compte):
    def __init__(self,solde_initial=0, taux_interet= 0.02):
        super().__init__(solde_initial)
        self.taux_interet = taux_interet
    def appliquer_interet(self):
        self.solde += self.solde * self.taux_interet
        print(f"Enteréts appliqués, Nouveau solde {self.solde}")

class Client:
    def __init__(self, identifiant, mot_de_passe):
        self.comptes = []
        self.identifiant = identifiant
        self.mot_de_passe = mot_de_passe
    def authentifier(self, mdp):
        return self.mot_de_passe == mdp
    def ajouter_compte(self,type_compte, depot=0):
        if type_compte.lower() == "courant":
            nouveau_compte = CompteCourant(depot)
        elif type_compte.lower() == "epargne":
            nouveau_compte = CompteEpargne(depot)
        self.comptes.append(nouveau_compte)
        print(f"Nouveau compte {type_compte} ouvert pour {self.identifiant}")

class Banque:
    def __init__(self):
        self.clients = {}
    def creer_client(self, identifiant, mdp, depot_initial):
        if identifiant not in self.clients:
            nouveau_client = Client(identifiant, mdp)
            nouveau_client.ajouter_compte("courant", depot_initial)
            self.clients[identifiant]= nouveau_client
        else:
            print("Ereur: cette identifiant existe deja")
    def supprimer_client(self, identifiant):
        if identifiant in self.clients:
            del self.clients[identifiant]
            print("Client supprimee!")
    def calculer_interets_globaux(self):
        for client in self.clients.values():
            for compte in client.comptes:
                if isinstance(compte, CompteEpargne):
                    compte.appliquer_interet()
            
        
              
    
        