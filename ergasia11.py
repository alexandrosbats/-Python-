anoixe = open("lista_tetradwn.txt","r")#Δεν καταλαβα πως ακριβως επρεπε να ειναι οι τετραδες στο αρχειο οποτε εβαλα ολα τα νουμερα κολλητα σε καθε τετραδα
grammes = []
for line in anoixe:
    grammes.append(line.rstrip())
diathesimes_tetrades = 0
i1 = int(input("Δώστε τον πρώτο αριθμό: "))
i2 = int(input("Δώστε τον δεύτερο αριθμό: "))
i3 = int(input("Δώστε τον τρίτο αριθμό: "))
i4 = int(input("Δώστε τον τέταρτο αριθμό: "))
i5 = int(input("Δώστε τον πέμπτο αριθμό: "))
i6 = int(input("Δώστε τον έκτο αριθμό: "))
list = [i1,i2,i3,i4,i5,i6]
for i in range(0,6):
   for j in range(0,6):
      for g in range(0,6):
         for n in range (0,6):
           prwto_pshfio = list[i]*1000
           deutero_pshfio = list[j]*100
           trito_pshfio = list[g]*10
           tetrapshfio = prwto_pshfio + deutero_pshfio + trito_pshfio + list[n]
           plhthos = 0
           for k in range (0,len(grammes)):
                if(str(tetrapshfio) != grammes[k]):
                   plhthos = plhthos + 1
                if(plhthos == len(grammes)):
                   diathesimes_tetrades = diathesimes_tetrades + 1
if (diathesimes_tetrades > 0):
    print("Υπάρχουν διαθέσιμες τετράδες από τους 6 αυτους αριθμούς")
else :
    print("Δεν υπάρχουν διαθέσιμες τετράδες από τους 6 αυτούς αριθμούς")
                
           
             

