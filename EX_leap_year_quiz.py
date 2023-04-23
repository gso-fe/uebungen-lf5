#
# LEAP YEAR QUIZ
# Happy Path ;)
#

import random

# initialisation of variables
hits = 0
is_tip_correct = True

print("----------")
print("SCHALTJAHR- Ratespiel:\n")

while(is_tip_correct == True):
    # generate a random value - GREGOR
    random_year = random.randint(1900, 2050)

    # get users tip - GUDRUN
    tip = input(f"{random_year} - ein Schaltjahr? [j/n] ")

    # determine leap year or not- GREGOR
    if random_year % 4 == 0:
        if random_year % 100 == 0:
            if random_year % 400 != 0:
                is_leap_year = False
            else: is_leap_year = True
        else: is_leap_year = True
    else: is_leap_year = False

    # compare tip with result (is_leap_year) - GREGOR
    if (tip == "j" and is_leap_year == True) \
            or (tip == "n" and is_leap_year == False):
        print("Treffer - du darfst weiterraten.\n")
        hits += 1
    else:
        print("Leider falsch. Spiel vorbei.\n")
        is_tip_correct = False

# show statistics - GREGOR
print(f"Erreichte Punkte: {hits}")
print("Auf Wiedersehen...")
print("---------")