# Start de oefen mee met onderstaande dictionary.
gasten = { # Sleutel is naam, waarde is job.
    "Jan":     "reporter",
    "Piet":    "acteur",
    "Joris":   "regisseur",
    "Korneel": "scenarist"
}
while True :
    naam = input('wie is het ')
    if naam != 'stop':
        if naam in gasten :
            gasten.pop(naam)
            print(f'welkom {naam}. kom binnen')
        else :
            print(f'{naam} staat niet op de lijst ')
    else : 
        break