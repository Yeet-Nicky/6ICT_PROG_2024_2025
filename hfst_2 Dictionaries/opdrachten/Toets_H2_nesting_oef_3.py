""" Oefening 2 (  / 3)
Maak onderstaande Vriendenlijst-app verder af.
Het menu is reeds gemaakt. Jij zal de eerste 2 opties in dit menu verder uitwerken.
 1) Toon details van een vriend
 2) Voeg een vriend toe
"""

vriendenlijst = {  # De startlijst van vrienden.
    'Emma': {'leeftijd': 25, 'woonplaats': 'Antwerpen'},
    'Liam': {'leeftijd': 30, 'woonplaats': 'Brussel'},
    'Noah': {'leeftijd': 22, 'woonplaats': 'Gent'},
}
test = {}

while True:  # Start de app.
    # Overzicht keuzemenu
    print("\nMenu:")
    print("  1) Bekijk details van een vriend.")
    print("  2) Voeg een vriend toe.")
    print("  3) Stop de app.")

    # Kies een van de 3 opties.
    optie = input("\nSelecteer wat je wilt doen: ")

    if optie == "1": 
        """ 1) Bekijk details van een vriend. (  / 1.5)
        Vraag de gebruiker naar de naam van een vriend.

        Als de naam voorkomt in de vriendenlijst, print dan alle informatie als volgt:
            >>> *naam* is *leeftijd* jaar oud en woont in *woonplaats*.
        
        Als de naam niet voorkomt, print dan:
            >>> Kan vriend *naam* niet vinden.

        """
        naam_vragen = input('geef de naam van je vriend: ')
        if naam_vragen in vriendenlijst:
            print(f'{naam_vragen} is {vriendenlijst[naam_vragen]['leeftijd']} jaar oud en woont in {vriendenlijst[naam_vragen]['woonplaats']}')

    elif optie == "2": 
        """ 2) Voeg een vriend toe. (  / 1.5)
        Vraag de gebruiker naar een *naam*, *leeftijd* en *woonplaats*.
        Voeg deze vriend toe aan de dictionary vriendenlijst.
        Het is toegestaan om een bestaande vriend te overschrijven.

        Tip! Maak eerst de sub-dictionary met leeftijd/woonplaats.
             Deze kan je vervolgens toevoegen aan de vriendenlijst met de opgegeven naam.
        Tip! Print na het sluiten van de app de dictionary. 
             Zo weet je of de nieuwe vriend correct is toegevoegd.

        """
        naam_nieuwe_vriend = input('wat is de naam van je nieuwe vriend: ')
        leeftijd_nieuwe_vriend = int(input('wat is de leeftijd van je nieuwe vriend: '))
        woonplaats_nieuwe_vriend = input('wat is de woonplaats van je nieuwe vriend: ')
        vriendenlijst['hi'] = 'leeftijd'
        vriendenlijst[naam_nieuwe_vriend]['leeftijd'] = leeftijd_nieuwe_vriend
        vriendenlijst[naam_nieuwe_vriend]['woonplaats'] = woonplaats_nieuwe_vriend
        print(vriendenlijst)


    elif optie == "3":  # Stop de app.
        print("\nBedankt voor het gebruiken van deze app.")
        break

    else:  # Verkeerde input gegeven.
        print("\nDit is geen optie. Gelieve opnieuw te proberen.")
