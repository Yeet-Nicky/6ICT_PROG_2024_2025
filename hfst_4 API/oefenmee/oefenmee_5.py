import requests

# url = "https://v2.jokeapi.dev/joke/Programming?safe-mode"
# response_json = requests.get(url).json() # Haal JSON uit response.

# # Bepaal of de grap uit 1 of 2 delen bestaat.
# if ("joke" in response_json):
#     print(response_json["joke"])     # De grap
# else:
#     print(response_json["setup"])    # De setup
#     print(response_json["delivery"]) # De punchline

# url = "https://v2.jokeapi.dev/joke/Christmas?safe-mode"
# response_json = requests.get(url).json() # Haal JSON uit response.

# # Bepaal of de grap uit 1 of 2 delen bestaat.
# if ("joke" in response_json):
#     print(response_json["joke"])     # De grap
# else:
#     print(response_json["setup"])    # De setup
#     print(response_json["delivery"]) # De punchline

aantalgrappen = 0
url = "https://v2.jokeapi.dev/joke/Christmas?amount=3?safe-mode"
response_json = requests.get(url).json() # Haal JSON uit response.
for grap in response_json["jokes"]:
    aantalgrappen += 1
    print(f'grap{aantalgrappen}')
    # Bepaal of de grap uit 1 of 2 delen bestaat.
    if ("joke" in grap):
        print(grap["joke"])     # De grap
    else:
        print(grap["setup"])    # De setup
        print(grap["delivery"]) # De punchline
