""" Oefening 2 (   / 3)
Onderstaande structuur geeft per persoon het aantal gemaakte doelpunt over 5 wedstrijden.
Print wie gemiddeld de meeste doelpunten heeft gemaakt, en hoeveel er dit waren.
Print wie gemiddeld de minste doelpunten heeft gemaakt, en hoeveel er dit waren.
De code moet blijven werken, ook als er later meer personen bijkomen.

Voor onderstaande datastructuur is dit het correcte antwoord.
    Meest: Sarah (2.6 doelpunten per match)
    Minst: Kiana (1.2 doelpunten per match)

TIP! Gebruik een for-loop om voor iedere persoon de gemiddelde score te berekenen.     
"""

sport_uitslagen = {
    'Emma': [2, 3, 1, 4, 2],  # Aantal doelpunten per wedstrijd
    'Liam': [1, 2, 1, 3, 0],
    'Noah': [0, 1, 2, 1, 3],
    'Sarah': [3, 3, 4, 2, 1],
    'Kiana': [1, 0, 2, 1, 2],
    'Lucas': [2, 1, 3, 1, 0]
}
som = 0
for i, meeste_doelpunten in sport_uitslagen.items():
    for j, doelpunten in enumerate(meeste_doelpunten):
        som += doelpunten
        # gemiddelde = j / doelpunten
        print(som)