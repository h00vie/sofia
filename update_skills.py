import requests

# Oletetaan, että repositoriosi on julkinen. Jos se ei ole, sinun täytyy lisätä headers-parametriin API-avain.
url = "https://raw.githubusercontent.com/käyttäjänimi/repositorio/master/sofiaSkills1.txt"
response = requests.get(url)

if response.status_code == 200:
    skills_content = response.text
    print(skills_content)
else:
    print("Ei voitu hakea tiedostoa.")
