from abc import ABC, abstractmethod
# Classe de Compte de base qui utilise l'encapsulation pour protéger les attributs
class Compte(ABC):
    def __init__(self, titulaire, solde=0):
        self._titulaire = titulaire  
# Titulaire du compte, protégé par l'encapsulation
        self._solde = solde  
# Solde du compte, protégé par l'encapsulation

# Méthode pour afficher le solde du compte
    def afficher_solde(self):
        return self._solde

  # Méthode pour effectuer un virement vers un autre compte 
    def virementSurCompte(self, montant, autre_compte):
        if self.retirer(montant):
            autre_compte.deposer(montant)
            return True
        return False

# Méthode pour déposer de l'argent sur un compte
    def deposer(self, montant):
        self._solde =self._solde + montant
        return self._solde



 