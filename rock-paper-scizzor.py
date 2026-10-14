import random
print("Wwelcom to rock-paper-scissors game")
print("Winning rules")
print("Rock vs Paper -> Paper wins")
print("Rock vs   Scissors --> Rock wins")
print("Paper vs Scissors --> Scissors wins")
choices = ["rock", "paper", "scissors"]
while True:
    print("choose an option from rock, paper, scissors")
    print("1- rock")
    print("2- paper")
    print("3- scissors")
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 3.")
        continue
    while choice < 1 or choice > 3:
        choice = int(input("Invalid input. Please enter a number between 1 and 3: "))
    user_choice = choices[choice - 1]
    print("Your choice is: " + user_choice)
    print("Now its computer turn.......")
    comp_choice = random.randint(1,3)
    computer_choice = choices[comp_choice - 1]
    print("Computer choice is: " + computer_choice)
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (choice == 1 and comp_choice == 2) or (choice == 2 and comp_choice == 3) or (choice == 3 and comp_choice == 1):
        print("Computer wins!")
    else:
        print("You win!")
    while True:
        ans =input("Do you want to play again? (y/n): ").lower()
        if ans in ['y', 'n']:
            break
        if ans == 'n':
            break
        print() 
        print("Thank you for playing the game. Goodbye!")      
