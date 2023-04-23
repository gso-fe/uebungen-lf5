#
# Features:
#   Sprache: User hier DE, Entwickler EN,
#   Variablen: PEP 8
#   Schleife: WHILE (inhaltliche Bedingung)
#   Eingabe: Sad Path mit Exception-Handling
#

while True:
    user_input = input("\nBerechnung der Quadratwurzel von: ")
    # Handle wrong input e.g string
    try:
        radicand = int(user_input)
        break
    except ValueError:
        print(" -> Falsche Eingabe: Bitte geben Sie eine Ganzzahl ein.")

print(f"Ihre Eingabe war {radicand}.")

area = radicand
length = 1
width = area/length

diff_length_width = abs(length - width)  

while diff_length_width > 0.001:
    length = (length + width) / 2
    width = area / length
    diff_length_width = abs(length - width)  

print(f"\nDie Quadratwurzel von {area} ist: {round((length + width) / 2,3)}\n")
