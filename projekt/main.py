import pickle, sys, os
from lexikonautomat import LexiconAutomaton

def create_alphabet(filename):
    path = os.path.abspath(filename)
    lexicon = []
    try:
        with open(path, "r") as text:
            words = [word.lower() for word in text.read().splitlines()]
            for line in words:
                lexicon.append(line)
        return sorted(lexicon)
    except FileNotFoundError:
        print("Datei nicht gefunden! Bitte gültige Datei eingeben!\nDas Programm wird beendet...")
        sys.exit(1)


def menu():
    construction = True
    while construction:
        print("***Start des Programms***\n(load) Automaten aus einer gespeicherten Datei laden\n(wordlist) Automaten aus " \
              "Wortliste konstruieren")
        question = input("Eingabe: >>> ")
        if question == "load":
            try:
                with open("Lexikonautomat.dat", "rb") as loaded:
                    automaton = pickle.load(loaded)
                construction = False
            except FileNotFoundError:
                print("Es existiert keine Datei mit einem gespeicherten Automaten. Bitte laden Sie den Automaten aus " \
                      "einer Wortliste.")
                
        elif question == "wordlist":
            input_word_list = input("Bitte geben Sie die Wortliste ein, mit der der Lexikonautomat initialisiert werden " \
                                    "soll:\n>>> ")
            wordlist = create_alphabet(input_word_list)
            automaton = LexiconAutomaton(wordlist)
            construction = False
        else:
            print("Die Eingabe ist ungültig! Bitte geben Sie eine gültige Eingabe ein.")

    run = True
    while run:
        print("*****Willkommen im Hauptmenü!*****\nWas möchten Sie tun?\n(1) Wort abfragen\n(2) Automaten zeichnen\n" \
              "(3) Sprache ausgeben\n(4) Automat speichern\n(q/quit) Programm beenden")
        option = input("Bitte eine der Optionen auswählen:\n>>> ")
        if option == "1":
            prog = True
            while prog:
                input_word = input("Dies ist die Worteingabe. Beende das Programm durch die Eingabe des leeren Worts " \
                                   "('').\nBitte geben Sie ein Wort ein:\n >>> ")
                if input_word == '':
                    prog = False
                    print("Das Programm wird beendet...")
                elif input_word in automaton.get_language(): 
                    print("Das Wort", input_word, "befindet sich im Lexikonautomaten.")
                else:
                    print("Das Wort", input_word, "befindet sich NICHT im Lexikonautomaten.")
        elif option == "2":
            print(automaton.draw_automaton())
        elif option == "3":
            print(automaton.get_language())
            automaton.language.clear()
        elif option == "4":
            with open("Lexikonautomat.dat", "wb") as saved:
                pickle.dump(automaton, saved, pickle.HIGHEST_PROTOCOL)
        elif option == "q" or option == "quit":
            run = False
            print("Das Hauptmenü wird beendet...")
        else:
            print("Keine gültige Option! Bitte gültige Option eingeben!")

if __name__ == "__main__":
    menu()