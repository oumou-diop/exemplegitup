nbr=int(input("entrer un nombre"))

for i in range(0,nbr+1,2):
     if i%2==0:
        print(i,"est paire")
        som=0
        i=1
        while (i<=nbr):
            if(i%2 !=0):
                som+=i
                i+=1
                print("la somme des nombres impairs est ",som)
                for i in range(nbr+1):
                    if (i%2==0):
                        print(i)
       
    
       
