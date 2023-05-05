value = ""
text="Eule"
for zeichen in text:
    print(id(value))
    value += (chr(ord(zeichen)+ 4))
print(value)
