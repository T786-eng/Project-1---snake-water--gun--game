import random
'''
1 = snake 

-1 = water

0 = gun

'''

computer = random.choice ([1 , 0 , -1])
yourstr = input ("Enter the choice: ")
yourDic = {'s' : 1 , 'w' : -1 , 'g' : 0}
reverseDic = {1 : "snake" , -1 : 'water' , 0 : 'gun'}

you = yourDic[yourstr]
#by now we have 2 numbers (variables) , you and computer

print(f"you chose {reverseDic[you]} \ncomputer chose {reverseDic[computer]}")

if computer == you:
    print ("It is a draw")

else :
    '''
    if (computer == -1 and you == 1):  = -2
        print("You win!")
    
    elif (computer == 1 and you == 0): = 1
        print("You lose!")

    elif (computer == 1 and you == -1): = 2
        print("You lose!")

    elif (computer == 1 and you == 0): = 1 
        print("You win!")
    
    elif (computer == 0 and you == -1): = 1
        print ("You win!")
    
    elif (computer == -1 and you == 0): = -1
        print ("You lose!")
    
    elif (computer == 0 and you == 1): = -1
        print ("You lose!")
    
    The below logic is written on the basis of value of computer - you
    
    '''
    
    # this is a shorter way of writing the above code
    
    # (computer - you) == 1  => computer = 1 , you = 0
    
    # (computer - you) == -2 => computer = -1 , you = 1
    
    # in both cases computer wins
    
    # in all other cases you win
    
    # this is a shorter way of writing the above code
    
    # you can also use (computer - you) % 3 == 1 to check if computer wins
    
    # you can also use (computer - you) % 3 == 1 to check if computer wins
    
    # this is because (1 - 0) % 3 == 1 and (-1 - 1) % 3 == 1
    
    
    if ((computer - you) == 1 or (computer - you) == -2 ):
        print("you lose!")
    else :
        print ("You win!")

