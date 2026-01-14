import random

CHOICES = {'s': 'snake', 'w': 'water', 'g': 'gun'}
# who beats whom
WINS = {'snake': 'water', 'water': 'gun', 'gun': 'snake'}


def get_user_choice():
    while True:
        choice = input("Enter your choice (s for snake, w for water, g for gun): ").strip().lower()
        if choice in CHOICES:
            return CHOICES[choice]
        print("Invalid choice. Please enter 's', 'w' or 'g'.")


def main():
    computer = random.choice(list(CHOICES.values()))
    you = get_user_choice()

    print(f"You chose {you}\nComputer chose {computer}")

    if you == computer:
        print("It's a draw.")
    elif WINS[you] == computer:
        print("You win!")
    else:
        print("You lose!")


if __name__ == "__main__":
    main()

