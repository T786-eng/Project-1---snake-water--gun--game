import random

# map short input -> index (used for compact logic)
CHOICE_INDEX = {'s': 0, 'w': 1, 'g': 2}
CHOICE_NAMES = ['snake', 'water', 'gun']

# computer picks 0..2
comp = random.randrange(3)

# read and validate user input
user_raw = input("Enter choice (s for snake, w for water, g for gun): ").strip().lower()
while user_raw not in CHOICE_INDEX:
    user_raw = input("Invalid. Enter s, w or g: ").strip().lower()

user = CHOICE_INDEX[user_raw]

print(f"You chose {CHOICE_NAMES[user]}\nComputer chose {CHOICE_NAMES[comp]}")

# decide outcome:
# If equal -> draw.
# Using cycle order [snake(0), water(1), gun(2)], user wins when (user - comp) % 3 == 2
if user == comp:
    print("It's a draw.")
elif (user - comp) % 3 == 2:
    print("You win!")
else:
    print("You lose!")
