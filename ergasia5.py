anoigw = open('keimeno5.txt','r+')
for line in anoigw:
  for lejh in line.split():
     if (len(lejh) > 3 ):
        w = lejh
        l = w[0] + "ay"
        lejh = w[1:]
        lejh = lejh + l
        print(lejh)
       
         

