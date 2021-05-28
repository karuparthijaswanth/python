import random
n=str(input("enter your choice :"))
l=["STONE", "PAPER", "SCISSOR"]
m=random.choice(l)
print(m)
if (n=="STONE" and m=="PAPER"):       
    print("COMPUTER WINS")
elif(n=="STONE" and m=="SCISSOR"):
    print("YOU WINS")
elif(n=="STONE"and m=="STONE"):
    print("MATCH DRAW!!!!")
elif(n=="PAPER" and m=="SCISSOR"):
    print("COMPUTER WINS")
elif(n=="PAPER"and m=="STONE"):
    print("YOU WINS")
elif(n=="PAPER" and m=="PAPER"):
    print("MATCH DRAW!!!")
elif(n=="SCISSOR"and m=="STONE"):
    print("COMPUTER WINS")
elif(n=="SCISSOR" and m=="PAPER"):
    print("YOU WINS")
elif(n=="SCISSOR" and m=="SCISSOR"):
    print("MATCH DRAW!!!")
else:
    print("GAME OVER")
        
        
       
            
        
            
       




