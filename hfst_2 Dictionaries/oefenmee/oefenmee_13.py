# Start de oefen mee met onderstaande dictionary.
fruitmand = { # Sleutel is fruit, waarde is aantal
    "appels": 2,
    "bananen": 3,
    "kersen": 10,
    "mango's": 1
}
for fruit in fruitmand :
    bijkopen = int(input(f'hoeveel {fruit} bijkopen (huidige aantal {fruitmand[fruit]}: )'))
    fruitmand[fruit] += bijkopen
for fruit in fruitmand :
    print(f'{fruitmand[fruit] } {fruit}')
    print('test')