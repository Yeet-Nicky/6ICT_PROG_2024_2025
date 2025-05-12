# Werk verder met de klasse Hond van oefen mee 6.
class Hond:
    def __init__ (self, naam, massa):
        self.naam = naam 
        self.massa = massa
    
    def weegschaal (self):
        print(f'{self.naam} weegt {self.massa} kg. ')

    def wijzig_naam (self, nieuwe_naam):
        print(f'{self.naam} heet nu {nieuwe_naam}')
        self.naam = nieuwe_naam

    def eten(self,hoeveelheid):
        self.massa = self.massa + hoeveelheid
        print(f'{self.naam} weegt nu {self.massa}')
hond_1 = Hond('henk', 15)
hond_2 = Hond('pietjan', 20)

" Via onderstaande code kan je niveau 1 testen. "
hond_3 = Hond("Lucky", 5)
hond_3.wijzig_naam("Bolly")

" Via onderstaande code kan je niveau 2 testen. "
hond_3.eten(0.5)
hond_3.eten(0.5)
hond_3.eten(0.5)

" Stel de test voor niveau 3 zelf op. "