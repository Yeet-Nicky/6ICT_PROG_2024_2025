# Start de oefen mee met onderstaande dictionary.
fruitmand = { # Sleutel is fruit, waarde is aantal
    "appel": 5,
    "banaan": 3,
    "kers": 50
}

# fruit = "banaan"
# print( fruitmand[fruit] )

# nieuw_fruit  = "mango"
# nieuw_aantal = 1
# fruitmand[nieuw_fruit] = nieuw_aantal
# print(fruitmand)

# fruit = "banaan"
# nieuw_aantal = 8
# fruitmand[fruit] = nieuw_aantal
# print(fruitmand)

# fruit = "kers"
# nieuw_aantal = 43
# fruitmand[fruit] = fruitmand[fruit] - 43
# print(fruitmand)

terugleggen_fruit = "kers"
fruitmand.pop(terugleggen_fruit)
print(fruitmand)