# Makler betritt den Raum
#  solange der Raum noch nicht vermessen wurde wiederhole
#    solange der Raum aus noch nicht vermessenen Rechtecken besteht
#        ermittle Seitenlängen des (ersten) Rechtecks
#        ermittle die Fläche des Rechtecks
#        addiere zur bisherigen Raumfläche hinzu
#  addiere zur bisherigen Wohnungsfläche hinzu

# HAPPY FLOW - without exception handling

apartment_area = 0
rectangle_count = 0
room_count = 0

is_room_remaining = True

print()
print(f" You entered the apartment...")
print(" -------------------------------------------------")

while (is_room_remaining == True):
    room_area = 0
    room_count += 1
    rectangle_count = 0
    is_rectangle_remaining = True
    
    while (is_rectangle_remaining == True):
        rectangle_count += 1
        rectangle_area = 0

        #handle user input for length and width of rectangles
        print(f" Room no.{room_count}, Rectangle no.{rectangle_count}:")
        input_value = input(f" -> Please insert the length of the current rectangle [cm]:")
        rectangle_length = int(input_value)
        input_value = input(f" -> Please insert the width of the current rectangle [cm]:")
        rectangle_width = int(input_value)

        #calculation (sum up the room area)
        rectangle_area = (rectangle_length / 100) * (rectangle_width / 100)
        room_area = room_area+rectangle_area

        #control the flow for the current room (boolean is_rectangle_remaining)
        input_value = input(f" Is there another rectangle to capture for this room [Y/N]?")
        if (input_value.upper() == "N"):
            is_rectangle_remaining = False
        else:
            is_rectangle_remaining = True
        print()

    #calculation (sum up the apartment area)
    apartment_area = apartment_area + room_area

    #control the flow for the apartment (boolean is_room_remaining)
    input_value = input(f" Is there another room to capture for this apartment [Y/N]?")
    if (input_value.upper() == "N"):
        is_room_remaining = False
    else:
        is_room_remaining = True
    print()

print(" -------------------------------------------------")
print(f" The area of the apartment is:{apartment_area} m²")
input("---------")

