#
# Features:
#   Sprache: User hier DE, Entwickler EN,
#   Kommentare: Dateikopf
#   Variablen: PEP 8, selbstsprechend
#   Eingabe: minimal (Happy Path) ohne Plausibilisierung
#   Ausgabe: formatiert, in Anlehnung an den Schreibtischtest
#
print("Populationsentwickung R2D2:")
print()
print("Geben Sie eine Anzahl")
r2d2_young = int(input(" - junger R2D2 ein: "))
r2d2_adult = int(input(" - erwachsener R2D2 ein: "))
r2d2_old = int(input(" - alter R2D2 ein: "))
print()
num_of_iterations = int(input("Geben Sie eine Anzahl von Iterationsschritten ein: "))
print()

print("|  Iteration |      Junge | Erwachsene |       Alte |")
print("-----------------------------------------------------")

for i in range(num_of_iterations):
    print(f"|{i+1:11d} |{r2d2_young:11d} |{r2d2_adult:11d} |{r2d2_old:11d} |")

    new_r2d2_old = int(r2d2_adult / 3)
    new_r2d2_adult = int(r2d2_young / 2)
    r2d2_young = 4 * r2d2_adult + 2 * r2d2_old

    r2d2_adult = new_r2d2_adult
    r2d2_old = new_r2d2_old
