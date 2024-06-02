from abc import ABC, abstractmethod
# Classe de Compte de base qui utilise l'encapsulation pour protéger les attributs
class Compte(ABC):
    def __init__(self, titulaire, solde=0):
        self.__titulaire = titulaire  
# Titulaire du compte, protégé par l'encapsulation
        self._solde = solde  
# Solde du compte, protégé par l'encapsulation

# Méthode pour afficher le solde du compte
    def afficher_solde(self):
        return self.__solde

  # surcharge 
    def virementSurCompte(self, montant, autre_compte):
        if self.retirer(montant):
            autre__compte.deposer(montant)
            return True
        return False

# Méthode pour déposer de l'argent sur un compte
    def deposer(self, montant):
        self.__solde =self.__solde + montant
        return self.__solde

# Méthode abstraite pour retirer de l'argent, à définir dans les sous-classes
    @abstractmethod
    def retirer(self, montant):
        pass

# Classe CompteEpargne hérite de Compte et implémente la méthode retirer avec une vérification 
class CompteEpargne(Compte):
    def __init__(self, titulaire, solde=0):
        super().__init__(titulaire, solde)  
# Appel du constructeur de la classe parent

# Surcharge de la méthode retirer pour le CompteEpargne avec une vérification de solde minimum
    def retirer(self, montant):
        if montant <= self._solde and self._solde - montant >= 0:  
# Solde minimum de 50 après retrait
            self._solde -= montant
            return "reussi avec succes"
        return "operation a echouer"

# polymorphisme
    def deposerArgent(self,montant):
        print("deposez dans le compte principale")


# encapsulatiion
class Compte(ABC):
    def __init__(self, titulaire, solde=0):
        self.__titulaire = titulaire  
        self.__solde = solde 

    def afficher_solde(self):
        return self.__solde

    def deposer(self, montant):
        self.__solde =self.__solde + montant
        return self.__solde
# Utilisation de l'héritage, de la surcharge, du polymorphisme, de l'abstraction et de l'encapsulation
compte1 = CompteCourant("Albert ", 1000)
compte2 = CompteEpargne("ndaliko", 500)

# albert dépose  sur son compte
compte1.deposer(200)

# ndaliko retire  sur son compte épargne
compte2.retirer(100)

# albert fait un virement à ndaliko
compte1.virementSurCompte(300, compte2)

 polymorphisme
# Méthode pour déposer de l'argent sur un compte
    def deposer(self, montant):
        print("vous ne pouvez pas deposer sur un compte epargne")


# encapsulatiion
class Compte(ABC):
    def __init__(self, titulaire, solde=0):
        self.__titulaire = titulaire  
        self.__solde = solde 

    def afficher_solde(self):
        return self.__solde

    def deposer(self, montant):
        self.__solde =self.__solde + montant
        return self.__solde
# Utilisation de l'héritage, de la surcharge, du polymorphisme, de l'abstraction et de l'encapsulation
compte1 = CompteCourant("Albert ", 1000)
compte2 = CompteEpargne("ndaliko", 500)

# albert dépose  sur son compte
compte1.deposer(200)

# ndaliko retire  sur son compte épargne
compte2.retirer(100)

# albert fait un virement à ndaliko
compte1.virementSurCompte(300,compte2)
# Affichage des soldes
print(compte1.afficher_solde())  
print(compte2.afficher_solde()) 

 