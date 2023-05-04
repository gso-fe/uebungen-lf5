import math

exponent = 3
checksum = 0

number = int(input("\nGeben Sie eine Zahl ein: "))

print("\n| exponent |     temp | checksum |   number |")
print("---------------------------------------------")

while exponent >= 0:
    temp_value = number / pow(10, exponent)
    checksum = checksum + math.trunc(temp_value)
    number = number - (math.trunc(temp_value)* pow(10, exponent))
    print(f"|{exponent:9d} |{temp_value:9.3f} |{checksum:9d} |{number:9d} |")
    exponent -= 1

print("")
print(f"Die Quersumme ist: {checksum}\n")
