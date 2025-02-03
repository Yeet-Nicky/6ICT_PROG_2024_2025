""" Oefening 3 (   / 8)
Deze oefening bestaat uit 3 niveaus, die je afzonderlijk kan maken. 
Elk niveau gebruikt de geneste dictionary spelrecensies, waarin een aantal recensies van spellen staan.

Tip! Als je met een bepaald niveau bezig bent, zet de code van de andere niveaus in commentaar. 
     Dit voorkomt fouten en zorgt dat je alleen aan de code werkt die relevant is.

"""
spelrecensies = {
    "Zeeslag": [8, 7, 9, 6, 3],
    "Catan": [9, 8, 8, 7],
}

""" Niveau 1 (    / 2)
Stel een overzicht op van ieder spel in spelrecensies.
Print voor ieder spel hoeveel recensies deze heeft en wat de laagste score is.

De code moet blijven werken ook als de inhoud van spelrecensies wijzigt.
Test dit zelf uit door manueel vragen toe te voegen of te veranderen.

VOORBEELD
---------
Overzicht van spellen...
    - Zeeslag heeft 5 recensies, met een 3 als laagste score.
    - Catan heeft 4 recensies, met een 7 als laagste score.
"""
# aantal_recensies = 0
# for recencies , score in spelrecensies.items():
#     print(f' - {recencies} heeft {len(score)} recensies, met een {min(score)} als laagste score')


""" Niveau 2 (    / 2)
Vraag een spel aan een gebruiker.
Bestaat dit spel in spelrecensies? 
    print dan: *spel* heeft een gemiddelde score van *gemiddeld*/10!
Bestaat dit spel niet?
    Print dan: *spel* niet gevonden in de database!

De code moet blijven werken ook als de inhoud van spelrecensies wijzigt.
Test dit zelf uit door manueel vragen toe te voegen of te veranderen.

VOORBEELD
---------
Welk spel wil je opzoeken? Catan
Catan heeft een gemiddelde score van 8.0/10!

VOORBEELD
---------
Welk spel wil je opzoeken: Pim-Pam-Pet
Pim-Pam-Pet niet gevonden in de database.
"""
# som_score = 0
# for spel , score in spelrecensies.items():
#     spel_controle = input('Welk spel wil je opzoeken? ')
#     print(score)
    # if spel_controle in spelrecensies:
    #     som_score = som_score + score
    #     gem_score = som_score/len(score)
    #     print(f'{spel_controle} heeft een gemiddelde score van {gem_score}/10')

""" Niveau 3 (   / 4)
Vraag de gebruiker naar een spel dat NIET in de database staat. 
Herhaal hierna het volgende...
    Vraag de gebruiker naar een recensie van dit spel.

Stop met herhalen wanneer de gebruiker STOP ingeeft. Voeg vervolgens dit spel, 
samen met alle recensies, toe aan de dictionary spelrecensies. De opbouw van 
dit nieuwe spel moet hetzelfde zijn als de spellen die al in de dictionary staan.
(de recensies moeten dus samen in een lijst staan)

Print tenslottee een overzicht met de nieuwe inhoud van de dictionary.
De spellen moeten alfabetisch overlopen worden in dit overzicht (zie voorbeeld).

VOORBEELD
---------
Welk nieuw spel toevoegen? Pim-Pam-Pet
    - Voeg een recensie toe: 4
    - Voeg een recensie toe: 5
    - Voeg een recensie toe: 2
    - Voeg een recensie toe: STOP

Nieuw spel toegevoegd. De dictionary ziet er nu als volgt uit...
    - recensies van Catan: [9, 8, 8, 7]
    - recensies van Pim-Pam-Pet: [4, 5, 2]
    - recensies van Zeeslag: [8, 7, 9, 6, 3]
"""
for spel, recensies in spelrecensies.items():
    nieuw_spel = input('Welk nieuw spel toevoegen? ')
    recensie = int(input('- Voeg een recensie toe: '))
    if recensie == 'STOP':
        break
    else:
        spel[nieuw_spel] = 1
        print(spelrecensies)