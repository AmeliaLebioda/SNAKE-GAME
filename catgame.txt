

def give():
  global x
  global y
  global z
  x = float (input ('Were is the A cat?'))
  if 1 < x < 100:
      print (x)
  else:
      print("Wrong points. Try again from 2 to 99 ")
  y = float(input('Were is the B cat?'))
  if 1 < y < 100:
      print (y)
  else:
      print("Wrong points. Try again from 2 to 99 ")
  z = float(input('Were is the mouse?'))
  if 1 < z < 100:
      print (z)
  else:
      print("Wrong points. Try again from 2 to 99 ")

      return x,y,z

give()


if (x==y) or (x==y==z) or (x<z<y and y-z==z-x) or (y<z<x and x-z==y-z):
    print ('The two cats fight and mouse escapes!')
elif (y<z<x and x-z<z-y) or (y<x<z and z-x<z-y) or (z<x<y and x-z<y-z):
    print ('Cat A won')
else:
    print ('Cat B won')






