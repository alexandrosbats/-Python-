def string_se_arithmo():
  keimeno = input("Δώστε string: ")
  string = str(keimeno)
  noumeroASCII = ''.join(str(ord(c)) for c in string)
  noumeroASCII2=int(noumeroASCII) 
  plhthos = 0 
  for i in range(1,noumeroASCII2 + 1):
      if (noumeroASCII2 % i == 0):
          plhthos = plhthos + 1
  if(plhthos == 2):
      print("Είναι πρώτος")
  else:
      print("Δεν είναι πρώτος")
  print(noumeroASCII2)
  

      

string_se_arithmo()
 
