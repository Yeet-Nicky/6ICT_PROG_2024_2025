# Maak voor deze oefen mee gebruik van onderstaande dictionary van dictionaries.
grootste_steden = {
    'Frankrijk': {
        'Parijs': 2140526,
        'Marseille': 869815,
    },
    'Belgi?': {
        'Brussel': 1209000,
        'Antwerpen': 523248,
    },
    'Duitsland': {
        'Berlijn': 3769495,
        'Hamburg': 1841179,
    }
}

print("overzicht van groote steden in europa")
for land,steden in grootste_steden.items():
    print(f'de grootste steden in {land} zijn:')
    for stad, inwoners in steden.items():
        print(f'    -{stad} met {inwoners} inwoners.')