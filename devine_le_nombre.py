import random

nombre_secret = random.randint(1, 100)

essais = 0

while True:

    proposition = int(input("Choisis un nombre entre 1 et 100 : "))
    essais += 1

    if proposition > nombre_secret:
        print("Plus bas")

    elif proposition < nombre_secret:
        print("Plus haut")

    else:
        print("Bravo !")
        print("Tu as trouvé en", essais, "essais.")
        break