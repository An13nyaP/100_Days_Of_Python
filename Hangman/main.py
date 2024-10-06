import random
from hangman_words import word_list
from hangman_art import stages, logo

print(logo)

end_of_game = False
lives = 6
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game and lives != 0:
    guess = input("Guess a letter: ").lower()

    
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        if (lives == 0):
            end_of_game = True
            print("You lose. The man is hung:(")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win! You saved the man:)")

    print(stages[lives])
