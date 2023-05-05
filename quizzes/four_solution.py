def counter(i):
    if(i == 1):
        return 1
    counter(i-1)
    print(i)

counter(10)

# counter(10)
#   counter(9)
#     counter(8)
#       counter(..)
#         counter(2)
#           counter(1)
#           return 1 - Ende der Funktion
#         print(2)
#       print(...)
#     print(8)
#   print(9)
# print(10)
