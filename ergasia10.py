import random
import itertools
def Three_or_Five_of_a_kind_or_Pair(hand):#ελέγχει εαν όλες οι κάρτες είναι ίδιες ή αν 3 απ αυτές είναι ίδιες και οι άλλες 2 είναι διαφορετικές μεταξυ τους ή εάν έχει μ'ονο δύο ίδιες και 3 διαφορετικές
    kind_list = [karta[0] for karta in hand]
    kind_list = list(set(kind_list))
    n =  len(kind_list)                 
    if (n == 1): 
      print("Έχει Five of a Kind")
    elif (n == 3  ) :
      print("Έχει Three of a Kind")
    elif (n == 4  ) :
      print("Έχει ένα pair")   
    else :
      print("Δεν εχει ουτε Three ουτε Five of a Kind ούτε Pair")
def Straight_flush_or_StraightFlush(hand) :
    plhthos_StraightFlush = 0
    plhthos_Straight = 0
    plhthos_Flush = 0
    for karta in hand:
        if (karta == 5):
            break
        if (((karta + 1)[0] == (karta[0] + 1)) and ((karta + 1)[1] == karta[1])):
            plhthos_StraightFlush += 1
        elif ((karta + 1)[0] == (karta[0] + 1)):
            plhthos_Straight += 1
        elif ((karta + 1)[1] == karta[1]):
            plhthos_Flush += 1
    if (plhthos_StraightFlush == 5):
        print("Έχει Straight Flush")
    elif (plhthos_Straight == 5) :
        print("Έχει Straight")
    elif (plhthos_Flush == 5):
       print("Έχει Flush")
    else:
       print("Δεν έχει ούτε Straight Flush ούτε Straight ούτε Flush") 
kartes = [ i for i in range (1,14) ] 
xrwmata = [ 'Spades','Hearts','Clubs','Diamonds' ]
trapoula = list(itertools.product(kartes , xrwmata))
random.shuffle(trapoula)
pc_hand = []
for i in range (5) :
    pc_hand = pc_hand + [trapoula.pop()]
print (pc_hand)
print(Three_or_Five_of_a_kind_or_Pair(pc_hand))
print(Straight_flush_or_StraightFlush(pc_hand))
