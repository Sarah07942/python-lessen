import random

# Rol twee 6-kantige dobbelstenen.

aantal_worpen = 0
totaal_van_de_worpen = 0
aantal_herhaling = int(input("Hoeveel keer worp je de dobbelstenen?:"))
#De dobbelstenen worden 10 keer weggegooid
while aantal_worpen < aantal_herhaling :
    eerste_steen = random.randint(1, 6)
    tweede_steen = random.randint(1, 6)
    dobbelsteen_som = eerste_steen + tweede_steen
    print("Je rolde een " + str(dobbelsteen_som) + "!")
    aantal_worpen = aantal_worpen + 1
#het totaal van de worpen wordt berekend
    totaal_van_de_worpen += dobbelsteen_som 
#Het gemiddelde worp berekenen
if aantal_herhaling > 0:
    gemiddelde_worp = totaal_van_de_worpen / aantal_herhaling
    print("Het gemiddelde worp is" + str(gemiddelde_worp) + ".")
else:
    print("Je hebt geen worpen uitgevoerd.")
