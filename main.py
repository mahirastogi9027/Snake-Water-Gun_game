'''
1 for Snake
-1 for Water
0 for Gun
'''
import random
# Computer's choice
computer= random.choice([-1,0,1])
# Your choice
youstr=input("Enter your choice: ")
youdict={"S":1,"W":-1,"G":0}
reversedict={1:"Snake", -1:"Water", 0: "Gun"}

#It will contain your choice of number:
you=youdict[youstr]
# To print yours and computer choice in term of words
print(f"You chose {reversedict[you]}\nComputer chose {reversedict[computer]}")

if(computer==you):
    print("Its a draw!")
else:


     if(computer==1 and you==-1):
         
         print("You Lose!")
     elif(computer==-1 and you==1):
         print("You Win!")    
     elif(computer==0 and you==-1):
         print("You Win!")   
     elif(computer==-1 and you==0):
         print("You Lose!")     
     elif(computer==1 and you==0):
         print("You Win!")  
     elif(computer==0 and you==1):
         print("You Lose!")      
     else:
         print("Something went wrong!")    