# Start de oefen mee met onderstaande dictionary.
steden_temp = { # Sleutel is stad, waarde is temp 
    "Hasselt": 25,
    "Oostende": 21,
    "Antwerpen": 24,
    "Brussel": 23,
    "Luik": 23,
    "Namen": 24
}

stad = input('geef een stad ')
temperatuur = steden_temp.get(stad, '???')
print(f'het is hier {temperatuur}')