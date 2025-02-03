""" Oefening 3 (   / 8)
Deze oefening bestaat uit 3 niveaus, die je afzonderlijk kan maken. 
Elk niveau gebruikt de geneste lijst producten, waarin info over een reeks producten staat.

Tip! Als je met een bepaald niveau bezig bent, zet de code van de andere niveaus in commentaar. 
     Dit voorkomt fouten en zorgt dat je alleen aan de code werkt die relevant is.

"""
producten = [
    {"naam": "Laptop", "prijs": 999.99, "voorraad": 5},
    {"naam": "Muis", "prijs": 25.50, "voorraad": 20},
]

""" Niveau 1 (   / 2)
Stel een overzicht op van alle producten.
Print voor ieder product de totale stockwaarde. Dit door voorraad maal prijs te doen.
Print tenslotte ook de totale waarde van alle producten samen.

De code moet blijven werken ook als de inhoud van producten wijzigt.
Test dit zelf uit door manueel producten toe te voegen of te wijzigen.

VOORBEELD
---------
Overzicht van producten...
    - Laptop heeft een totale waarde van €4999.95
    - Muis heeft een totale waarde van €510.0
De totale prijs van alle producten bedraagt €5509.95.

"""


""" Niveau 2 (   / 2)
Vraag de gebruiker naar een voorraad.
Print vervolgens alle producten waarvan er minder in voorraad is dan het opgegeven aantal.

De code moet blijven werken ook als de inhoud van producten wijzigt.
Test dit zelf uit door manueel vragen toe te voegen of te veranderen.

VOORBEELD
---------
Zoek producten met minder voorraad dan: 15
    - Laptop heeft nog maar 5 stuks op voorraad.
"""


""" Niveau 3 (   / 4)
Vraag de gebruiker naar een productnaam.

Bestaat dit product nog niet in de geneste lijst?
    Vraag de gebruiker dan naar de prijs en de initiele voorraad.
    Voeg vervolgens een nieuw element met deze info toe aan de geneste lijst.
    De opbouw van dit nieuwe element moet hetzelfde zijn als de reeds bestaande producten.
Bestaat dit product reeds in de geneste lijst?
    Print dan dat het product reeds bestaat.

Print tenslotte de geneste lijst om eventuele wijzigingen erin te tonen.

Tip! Ga er eerst vanuit dat het ingegeven product NIET bestaat in de lijst.
     Controleren of het product bestaat is moeilijk.

    VOORBEELD (nieuw element)
---------
Geef een product in: Headset
(Headset is nieuw) Prijs: 49.95
(Headset is nieuw) Voorraad: 9
[ ..., {'naam': 'Headset', 'prijs': 49.95, 'voorraad': 9}]

VOORBEELD (bestaand element)
---------
Geef een product in: Muis
Muis bestaat reeds.
[{'naam': 'Laptop', 'prijs': 999.99, 'voorraad': 5}, {'naam': 'Muis', 'prijs': 25.5, 'voorraad': 20}, {'naam': 'Monitor', 'prijs': 150.0, 'voorraad': 10}]

"""
