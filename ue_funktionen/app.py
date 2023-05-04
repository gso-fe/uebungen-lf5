from tools import add
from tools import calculate
from tools import is_palindrom
from tools import shift
from tools import menue

print(add(1,2,3,4,5,6,7,8,9))

print(calculate("a",1,2,3,4,5))
print(calculate("m",1,2,3,4,5))

print(is_palindrom("reliefpfeiler"))
print(is_palindrom("ottoh"))

clear_text = "Geheim"
secure_text = None

for char in clear_text:
  print(shift(char,1), end="")

menue()