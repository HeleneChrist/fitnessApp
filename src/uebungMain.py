import uebung
import uebungListe

def uebungHinzufuegen(countable,category, type, name, disrciption, isBreak = False):
    uebungListe.ubungen.append(uebung.uebung(countable,category, type, name, disrciption, isBreak))

def uebungEntfernen(name):
    for i in range(len(uebungListe.ubungen)):
        if uebungListe.ubungen[i].getName() == name:
            uebungListe.ubungen.pop(i)
            break
def uebungAnzeigen():
    for i in range(len(uebungListe.ubungen)):
        print(uebungListe.ubungen[i].getUebung())