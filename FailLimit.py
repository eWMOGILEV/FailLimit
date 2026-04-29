#Ich habe nie gesagt, dass ich der beste Programmierer bin
#Es ist einfach nur für Schüler die es brauchen
import copy 
print(r"______    _ _ _     _           _ _   ")
print(r"|  ___|  (_) | |   (_)         (_) |  ")
print(r"| |_ __ _ _| | |    _ _ __ ___  _| |_ ")
print(r"|  _/ _` | | | |   | | '_ ` _ \| | __|")
print(r"| || (_| | | | |___| | | | | | | | |_ ")
print(r"\_| \__,_|_|_\_____/_|_| |_| |_|_|\__|")
def Intruduction():
    print("\nAnweisungen:\n Du tragst zuerst die mündlichen Noten ein,\n"
    "danach werden die Schulaufgabennoten eingetragen,\n"
    "und zuletzt wird es alles zusammengerechnet")
    NotenKL()


def NotenKL():
    Noten = []
    NotenAnzahl = 1
    print("Trage Noten ein (einfach oder doppelt zählen)\n"
    "Falls keine: direkt 0 eingeben")

    while True:
        try:
            Note = int(input(f"Note Nummer {NotenAnzahl}: "))
            if 1 <= Note <= 6:
                Noten.append(Note)
                NotenAnzahl += 1
                print("Noten:", Noten)
            elif Note == 0:
                NotenSchulaufgaben(Noten)
                break
            else:
                print("Noten gehen von 1 bis 6.")
        except ValueError:
            print("Eingabe ist keine Zahl.")

def NotenSchulaufgaben(NotenKL):
    print("Trage jetzt die SchA Noten ein\nFalls keine: direkt 0 eingeben")

    Noten = [] 

    NotenZahl = 1
    while True:
        try:
            Note = int(input(f"Note Nummer {NotenZahl}: "))
            if 1 <= Note <= 6:
                Noten.append(Note)
                NotenZahl += 1
                print("Noten:", Noten)
            elif Note == 0:
                Zusammenrechnen(Noten, NotenKL)
                break
            else:
                print("Noten gehen von 1 bis 6.")
        except ValueError:
            print("Eingabe ist keine Zahl.")

def safe_average(liste):
    if len(liste) == 0:
        return None
    return sum(liste) / len(liste)

def Zusammenrechnen(NotenSchA, NotenKL):
    print("\n"*100)
    SchnittSchA = safe_average(NotenSchA)
    if len(NotenKL) == 0:
        SchnittKL = None
    else:
        SchnittKL = sum(NotenKL) / len(NotenKL)
    SchAEinsOderZwei = int(input("Wie viel zählen Schulaufgaben? (z.B. 2): "))
    if SchnittSchA is None and SchnittKL is None:
        print("Keine Noten vorhanden.")
        return
    elif SchnittSchA is None:
        gesamt = SchnittKL
    elif SchnittKL is None:
        gesamt = SchnittSchA
    else:
        gesamt = (SchnittSchA * SchAEinsOderZwei + SchnittKL) / (SchAEinsOderZwei + 1)
    print("Schnitt =", round(gesamt, 2))
    TestNotenSchA = copy.deepcopy(NotenSchA)
    TestNotenKL = copy.deepcopy(NotenKL)
    NochSchASchreiben = int(input("Wie viele Schulaufgaben musst du noch schreiben? "))
    Mögliche6SchA = 0
    Mögliche6KL = 0
    while NochSchASchreiben > 0:
        TestNotenSchA.append(6)
        TestSchnittSchA = sum(TestNotenSchA) / len(TestNotenSchA)
        TestSchnitt = (TestSchnittSchA * SchAEinsOderZwei + SchnittKL) / (SchAEinsOderZwei + 1)
        if TestSchnitt >= 4.5:
            TestNotenSchA.pop()
            break
        Mögliche6SchA += 1
        NochSchASchreiben -= 1
    if len(TestNotenSchA) > 0:
        TestSchnittSchA = sum(TestNotenSchA) / len(TestNotenSchA)
        GesamtSchA = (TestSchnittSchA * SchAEinsOderZwei + SchnittKL) / (SchAEinsOderZwei + 1)
    else:
        GesamtSchA = SchnittKL
    while True:
        TestNotenKL.append(6)
        TestSchnittKL = sum(TestNotenKL) / len(TestNotenKL)
        TestSchnitt = (SchnittSchA * SchAEinsOderZwei + TestSchnittKL) / (SchAEinsOderZwei + 1)
        if TestSchnitt >= 4.5:
            TestNotenKL.pop()
            break
        Mögliche6KL += 1
    if len(TestNotenKL) > 0:
        TestSchnittKL = sum(TestNotenKL) / len(TestNotenKL)
        GesamtKL = (SchnittSchA * SchAEinsOderZwei + TestSchnittKL) / (SchAEinsOderZwei + 1)
    else:
        GesamtKL = SchnittSchA
    print(
        f"\nDu kannst entweder {Mögliche6SchA} Schulaufgaben 6(er) haben (Schnitt wäre dann: {round(GesamtSchA,2)})\n"
        f"oder {Mögliche6KL} mündliche / KL 6(er) haben (Schnitt wäre dann: {round(GesamtKL,2)})\n"
    )

Intruduction()
