def switch(operace):
    if operace == "+":
        return print("Vysledek: ", a + b)
    elif operace == "-":
        return print("Vysledek: ", a - b)
    elif operace == "/":
        return print("Vysledek: ", a / b)
    elif operace == "*":
        return print("Vysledek: ", a * b)
    elif operace == "pow":
        return print("Vysledek: ", a ** b)
    elif operace == "sqrt":
        return print("Vysledek: ", a ** (1 / b))
    elif operace == "%":
        return print("Zbytek po deleni je: ", a % b)

while True:
    print("Zadej prvni cislo: ")
    a = int(input())
    print("Zadej druhe cislo: ")
    b = int(input())
    print("Vyber oberaci: /,*,-,+,pow,sqrt,%")
    operace = input()

    switch(operace)
    print("Chcete pokracovat napiste: \"ano\" \"ne\"")
    if (input() == "ne"):
        break