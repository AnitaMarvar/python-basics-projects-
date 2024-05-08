import random
random_number = random.randint(0,99)
user_number = int(input("Enter the number: "))
if random_number == user_number:
    print("You've guessed the number!")
else:
    print("Wrongly Guessed")
    print("\n The number is ",random_number)
