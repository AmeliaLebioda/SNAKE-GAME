lphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
   global h
   global n
   global w
   global pol
   global poh
   n=0
   height = []
   while n<=25:
       print ('Height of the ', end ="")
       print (alphabet[n] , end  = '')
       h = int(input(' letter '))
       if 1 <= h <= 7:
            height.append(h)
            n=n+1

       else: print ('Wrong height ')
   print (height)

   w = (input('Word contains no more than 10 letters '))
   if 1<=len(w) <=10 :
       m=0
       thelastone = []
       while m<=len(w)-1:

          pol = (alphabet.index(w[m]))
          poh = (height[pol])
          thelastone.append(poh)
          m=m+1

   else: print ('Too many letters')

   print (max(thelastone)*len(w)*1)

   return height

viewer()
