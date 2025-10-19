def citeste_numar(i):
    while True:
        try:
            numar = float(input(i)) # transformam inputul in nr
            return numar
        except ValueError:
            print("Nr nu este valid")


def citeste_operator():
    while True: # loop pentru expresiile matematice
        op = input("Introduceti expresia (+, -, *, /) sau C pentru stergere: ")
        if op in ['+', '-', '*', '/']:
            return op  # daca expresia este permisa, continuam
        elif op.upper() == 'C':
            return 'C'
        else:
            print("Operator invalid! Folositi doar +, -, *, / sau C.") # eroare daca expresia nu este permisa



# cazurile pentru calcul
def calculeaza(nr1, op, nr2):
    if op == '+':
        return nr1 + nr2
    elif op == '-':
        return nr1 - nr2
    elif op == '*':
        return nr1 * nr2
    elif op == '/':
        if nr2 == 0:
            return "Eroare: impartire la 0!"
        return nr1 / nr2


def calculator():
    while True:
        nr1 = citeste_numar("Introduceți un numar: ")

        op = citeste_operator()
        if op == 'C':
            continue

        nr2 = citeste_numar("Introduceți al doilea numar: ")

        rezultat = calculeaza(nr1, op, nr2)
        print("Rezultat:", rezultat, "\n")

        cont = input("Doriti sa faceti alt calcul? (da/nu): ").strip().lower()
        if cont != 'da':
            print("La revedere!")
            break


# Rula programul
calculator()
