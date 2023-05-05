def counter(i):
    if(i == 1):
        return 1
    counter(i-1)
    print(i)

counter(10)
