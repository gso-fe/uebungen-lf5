def add(*values):
  """Calculates the sum of an abitrary parameter-list"""
  sum = 0
  for element in values:
    sum += element
  return sum

def calculate(op_type, *values):
  """Calculates 
  - the sum (op_type == "a") or 
  - the product (op_type == "m") 
  of an abitrary parameter-list
  """
  if op_type.lower() == "a":
    sum = 0
    for element in values:
      sum += element
    return sum
  elif op_type.lower() == "m":
    product = 1
    for element in values:
      product = product * element
    return product
  else:
    return None

def shift(char, x):
    """Returns a character shifted by x positions."""
    pos_of_char = ord(char)
    shifted_pos = pos_of_char + x
    return chr(shifted_pos)

def is_palindrom(input):
    """Returns True if input is a palindrom."""
    word = input.lower().split()
    reverse_word = input[::-1].lower().split()
    if word != reverse_word:
        return False
    return True

def menue():
  print("\n")
  print("####################################################################")
  print("##              Willkommen zum Ticketautomaten                    ##")
  print("##----------------------------------------------------------------##")
  print("##                                   CC BY 4.0                    ##")
  print("####################################################################")
