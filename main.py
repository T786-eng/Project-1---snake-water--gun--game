import random

# Mapping of valid inputs to game values
#  1 = snake, -1 = water, 0 = gun
choices = {
    's': 1, 'snake': 1, '1': 1,
    'w': -1, 'water': -1, '-1': -1,
    'g': 0, 'gun': 0, '0': 0,
}
reversedic = {1: 'snake', -1: 'water', 0: 'gun'}

computer = random.choice([1, 0, -1])

# Prompt until a valid choice is entered
while True:
    user_raw = input("Enter your choice (s/w/g, snake/water/gun, or 1/0/-1): ").strip().lower()
    if user_raw in choices:
        you = choices[user_raw]
        break
    print("Invalid choice. Please enter 's', 'w', or 'g' (or full words 'snake','water','gun' or numbers 1,0,-1).")

# by now we have two numbers (you and computer)
print(f"You chose {reversedic[you]} \nComputer chose {reversedic[computer]}")


if computer == you:
    print("It's a draw")
else:
    # Define which choice beats which: key beats value
    wins = {1: -1, -1: 0, 0: 1}  # snake beats water, water beats gun, gun beats snake
    if wins[you] == computer:
        print("You win!")
    else:
        print("You lose!")


