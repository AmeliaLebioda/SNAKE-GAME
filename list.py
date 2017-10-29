def number():
    global n
    global d
    n = int (input ('Give n'))
    if 1 <= n <= 100000:
        new = []
        z = 1
        while int(z) < n+1:
            new.append(z)
            z = int(z) + 1
        print (new)
    else:
        print('Wrong numbers')

    d = int (input ('Give d'))
    if 1 <= d <= n:
        y=1
        a=1
        while y<=d:
           new.remove(a)
           new.append(y)
           a=a+1
           y=y+1
           print (new)
    else:
        print('Wrong numbers')

    return n,d

number()