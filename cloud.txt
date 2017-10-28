def game():

 def game():

    global n
    global k
    global x
    global c
    global p
    global j
    global E
    n = int (input ('the number of clouds'))
    if 2 <= n <= 25:
        x = 0
        numberofclouds = []
        while int(x) < n :
            numberofclouds.append(x)
            x = int(x) + 1
        print(numberofclouds)

    else:
        print('Wrong numbers')

    m=0
    p = 0
    while int (m) < n:
        numberofclouds.remove(p)
        c = int(input('What kind of cloud: 0-ordinary, 1-thundercloud'))
        if c == 0:
           numberofclouds.insert(p,0)
        elif c == 1:
           numberofclouds.insert(p,1)
        else:
            print('Wrong numbers')
        p = p + 1
        m = int(m) + 1
    print (numberofclouds)
    k = int(input('the jump distance'))
    if (1<=k<=n) and (n % k == 0 ):
        print ('Aerith starts out')
    else: print ('Wrong numbers. Try again')


    E=100
    while k<=n-1:
        if numberofclouds[k] == 0:
            E=E-1
        else:
            E=E-1-2;
        k=k+k


    print (E)

    return n,c

game()
