import random
rock='''                _    
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\
                     '''
paper='''                             
 _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|              '''
scissor='''  ____
  / __ \
 ( (__) |___ ___
  \________,'   """""----....____
   _______<  () dd       ____----'
  / __   __`.___-----""""
 ( (__) |
  \____/
'''
names=["rock","paper","scissor"]
i=random.choice(names)

choice=input("Enter your choice \"Rock\" or \"Paper\" or \"Scissor\" ")
if choice.lower()=='rock':
    print("Yours choice\n",rock)
elif choice.lower()=="paper":
    print("Yours choice is\n\n",scissor)
else:
    print("Yours choice is\n\n",paper)
if i.lower()=='rock':
    print("Computers choice\n\n",rock)
elif i.lower()=="paper":
    print("Computers choice is\n",scissor)
else:
    print("Computers choice is\n",paper)

if choice.lower()=="rock" and i=='paper':
    
    print("You loose")
elif choice.lower()=="paper" and i=="scissor":
    print("You loose")
elif choice.lower()=="scissor" and i=="rock":
    print("You loose") 
elif choice.lower()=='rock' and i.lower()=="scissor":
    print("You loose")
elif choice.lower()=='paper' and i.lower()=="rock":
    print("You loose")
elif choice.lower()=='scissor' and i.lower()=="paper":
    print("You loose")


elif choice.lower() == i.lower():
    print("No result")

else:

    print("You Win")
    