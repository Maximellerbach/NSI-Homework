cout_total = 134.34
donnee = 150
du = round(donnee-cout_total, 2)

monnaie = [2, 1, 0.50, 0.20, 0.10, 0.05, 0.01]
rendu = []

for piece in monnaie:
    a = round(du, 2)//piece
    du -= (piece*a)
    rendu.append(int(a))

print(rendu)