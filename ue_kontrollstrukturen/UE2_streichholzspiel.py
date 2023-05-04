#
# Features:
#   Sprache: User hier DE, Entwickler EN,
#   Variablen: PEP 8
#   Schleife: WHILE (inhaltliche Bedingung)
#   Eingabe: minimal (Happy Path) ohne Plausibilisierung
#   Ausgabe: Unterscheidung Singular-Plural
#

num_matches = 31
print("STREICHHOLZSPIEL")
print(f"# {num_matches} Streichhölzer sind im Spiel.")

print("\nDer Computer nimmt 2 Streichhölzer.")
num_matches = num_matches - 2

while num_matches > 1:
    print(f"# {num_matches} Streichhölzer verbleiben.")

    #get user-input
    human_choice = int(input("\nWieviele Streichhölzer [1-6] nehmen Sie? "))
    num_matches = num_matches - human_choice

    print(f"# {num_matches} Streichhölzer verbleiben.")

    #calculate computer choice 
    comp_choice = 7 - human_choice

    #display computer choice
    if comp_choice == 1:
        print(f"\nDer Computer nimmt {comp_choice} Streichholz.")
    else:
        print(f"\nDer Computer nimmt {comp_choice} Streichhölzer.")

    #calculate remaining matches
    num_matches = num_matches - comp_choice

print("# EIN LETZTES Streichholz verbleibt.\n")
print("SIE HABEN LEIDER VERLOREN...\n")
