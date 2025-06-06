# Maak de klasse Hond aan zoals omschreven in oefen mee 9.
class Hond:
    locaties = ["living", "tuin", "buren", "keuken"]
    
    def __init__(self, naam, locatie):
        self.naam = naam
        self.locatie = locatie

    def ziet_hond(self, geziende_hond):
        print(f'{self.naam} ziet {geziende_hond} in de {self.locatie}')

" Via onderstaande code kan je niveau 1 testen. "

hond_1 = Hond("Lulu", "keuken")
hond_2 = Hond("Floris", "keuken")
hond_3 = Hond("Ranger", "tuin")

hond_1.ziet_hond(hond_2)
hond_1.ziet_hond(hond_3)


" Via onderstaande code kan je niveau 2 & 3 testen. Opgelet! Resultaat is random. "
" Best print je in __init__ ook de locatie waar iedere hond start, zo kan je de werking makkelijker nagaan. "

# hond_1 = Hond("Lulu")
# hond_2 = Hond("Floris")
# hond_3 = Hond("Ranger")

# hond_1.ziet_hond(hond_2)                  
# hond_1.ziet_hond(hond_3)   
          
# print(hond_1.locatie)   
