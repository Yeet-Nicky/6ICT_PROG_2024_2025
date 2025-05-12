# Werk verder met de klasse Hond van oefen mee 4.
class Hond:
    def __init__ (self, naam, massa):
        self.naam = naam 
        self.massa = massa
    
    def weegschaal (self):
        print(f'{self.naam} weegt {self.massa} kg. ')

hond_1 = Hond('henk', 15)
hond_2 = Hond('pietjan', 20)
" Via onderstaande code kan je niveau 2 testen. "
hond_1.weegschaal()
hond_2.weegschaal()
