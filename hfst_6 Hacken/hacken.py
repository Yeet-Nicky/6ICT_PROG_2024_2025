import requests

# TODO 1: vervang URL door te doorzoeken webpagina.
URL = "http://172.16.112.19:8000/" 
html_code = requests.get(URL).text

# Overloop iedere regel HTML-code apart.
for regel in html_code.split("\n"):
    if "href" in regel :
        print("##############")
        print(regel)
        print("##############")

