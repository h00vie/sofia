import os
import time

# Tiedoston nimi, johon käskyt tallennetaan
filename = "sofiaSkills1.txt"

while True:
    # Oletetaan, että `get_new_command` on funktio, joka palauttaa uuden käskyn tai None, jos uutta käskyä ei ole
    new_command = get_new_command()  # Tämä on pseudokoodia
    if new_command:
        # Lisää uusi käsky tiedostoon
        with open(filename, "a") as file:
            file.write(new_command + "\n")
        # Työnnä muutokset GitHubiin
        os.system("git add " + filename)
        os.system('git commit -m "Päivitä Sofia-assistentin osaamisia"')
        os.system("git push")
    # Odota 10 minuuttia ennen seuraavaa iteraatiota
    time.sleep(600)
