val = float(input("digite o valor que deseja ver a tabuada"))
tab = int(input("digite quantas vezes quer calcular"))

for n in range(tab):
  print(f"{val} + {n} = {val + n}")

  print(f"{val} - {n} = {val - n}")

  print(f"{val} * {n} = {val * n}")
  if n > 0:
    print(f"{val} / {n} = {val / n}")
  print()