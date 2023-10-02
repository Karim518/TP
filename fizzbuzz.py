class fizzbuzz:
    def affiche(self, nombre):
        resultat=""

        for i in range(1, nombte + 1):
            if i%15==0:
                resultat += "FrisBee"
            elif i%5==0:
                resultat += "Buzz"
            else:
                resultat += i

        return resultat