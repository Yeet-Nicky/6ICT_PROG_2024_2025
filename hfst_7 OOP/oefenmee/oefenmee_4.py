# Werk verder met de klasse Hond van oefen mee 2.
class Hond:
    naam = 'henk'
    massa = 20

    def blaf(self):
        print(f'{self.naam} zegt blaf')

    def weegschaal(zichzelf) :
        print(f'{zichzelf.naam} weegt {zichzelf.massa}')

    def benoem(self, verander_naam):
        self.naam = verander_naam

    def wegen(self,verander_massa):
        self.massa =verander_massa

hond = Hond()
huisdier = Hond()

print(hond.blaf)
" Via onderstaande code kan je niveau 1 testen. "
hond = Hond()
hond.benoem("Fleur")
print( hond.naam )
hond.blaf()

" Via onderstaande code kan je niveau 2 testen. "
dier = Hond()
dier.benoem("Fifi")
dier.wegen(3)
print( dier.massa )
dier.weegschaal()