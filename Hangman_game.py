import random
import Stages

print("Welcome to hangman Game")
print("You have 6 chances to guess letters to complete the word below")

words = ["Balloon", "Butter", "Puppy", "Ground", "Trainer", "Flower", "Fruits", "Blessed"]
lives = 6
gen_word = random.choice(words).lower()
show = []
for i in range(len(gen_word)):
    show += "_"
print(show)
game_over = False
while not game_over:
    guessed_letter = input("Guess a letter: ").lower()
    for position in range(len(gen_word)):
        char = gen_word[position]
        if char == guessed_letter:
            show[position] = guessed_letter
    print(show)
    if guessed_letter not in gen_word:
        lives -= 1
        print(Stages.Hangman_stages[lives])
        if Stages.Hangman_stages[lives] == [0]:
            game_over = True
        if lives == 0:
            game_over = True
            if Stages.Hangman_stages == [6]:
                print("OOPS!! YOU LOSE")
    if '_' not in show:
        game_over = True
        print("YEY!! YOU WIN")
