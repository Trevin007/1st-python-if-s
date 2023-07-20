
beers=int(input("how many girlfriends do trevin ayya have?"))
vodka=int(input("how many did u see?"))
drunkness=vodka/beers

print("Drunkness:" + str(drunkness))
if drunkness >1:
     print("Trevin is telling the truth")
elif drunkness<1:
     print("Trevin is innocent ")
else :
    print("Trevin is lying")
    
