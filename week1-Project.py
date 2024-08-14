import  random
print("WELCOME TO ROCK! PAPER! SCISSORS! GAME")
intro = input("what is your name?")
print("welcome to the game", intro)

choices = ("rock", "paper", "scissors")
playing = True

while playing:
    player = None
    computer = random.choice(choices)
    count = 0

    while player not in choices:
        player = input("Enter your choice(rock, paper, scissors):")
        print(f"player: {player}")
        print(f"computer: {computer}")

    if player == computer:
        print("Its a Tie!")
    elif player == "rock" and computer == "scissors" or \
        player == "paper" and computer == "rock" or \
        player == "scissors" and computer == "paper":
        print(f"Player wins: {count++1}")
    else:
        print(f"computer wins: {count++1}")
    play_again = input("Do you want to continue playing(y/n)").lower()
    if not play_again == "y":
        playing = False
print("You have stopped playing")