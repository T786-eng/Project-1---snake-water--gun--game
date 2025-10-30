import random
'''
1 = snake 

-1 = water

0 = gun

'''
computer = random.choice ([1 , 0 , -1])
yourstr = input ("Enter your choice :")
yourdic = {'s': 1 , 'w' : -1 , 'g' : 0 }
reversedic = {1 : 'snake' , -1 : 'water' , 0 : 'gun'}

you = yourdic[yourstr]

# by now we have 2 numbers(variable), you and computer

print(f"you chose {reversedic[you]} \ncomputer chose {reversedic[computer]}")


if (computer == you):
    print("its a draw")
else:
    if (computer == -1 and you == 1):
        print("You win!")
    elif (computer == 1 and you == 0):
        print("You lose!")

    elif (computer == 1 and you == -1):
        print("You lose!")

    elif (computer == 1 and you == 0):
        print("You win!")
    
    elif (computer == 0 and you == -1):
        print ("You win!")
    
    elif (computer == -1 and you == 0):
        print ("You lose!")
    
    elif (computer == 0 and you == 1):
        print ("You lose!")

    else :
        print ("something went wrong")


