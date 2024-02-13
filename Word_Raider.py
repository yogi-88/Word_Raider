import random
game_title = "Data Quest"

word_bank = []
reading_file = open("words.txt", "r")
for reading_lines in reading_file:
    
    word_bank.append(reading_lines.rstrip())

guess_word = random.choice(word_bank)

misplaced_list = []
wrong_guess_list = []
max_chances = 8
current_turn = 0

print(f"Welcome to the game - {game_title}")
print(f"There are in total {len(guess_word)} letters in the word to guess.")
print(f"You are left with {max_chances - current_turn} turns to guess the word.")

while current_turn < max_chances:
    the_guess = input("What is your guess: ").lower()
    if len(the_guess) != len(guess_word) or not the_guess.isalpha():
        print("Length of entered guess should be length of word to guess. and input values should contain only alpha letters")
        continue
        
    index = 0
    for c in the_guess:
        if c == guess_word[index]:
            print(c, end=" ")
            if c in misplaced_list:
                misplaced_list.remove(c)
        elif c in guess_word:
            if c not in misplaced_list:
                misplaced_list.append(c)
            print("_", end=" ")
                
            
        else:
            if c not in wrong_guess_list:
                wrong_guess_list.append(c)
            print("_", end=" ")
        index += 1
    
    print("\n")
    print(f"Misplaced guesses : {misplaced_list}")
    print(f"Incorrect  guesses list: {wrong_guess_list}")
    
    current_turn += 1
    
    if the_guess == guess_word:
        print("Congrates, you won the game")
        break
    if current_turn == max_chances:
        print(f"Bad luck, You lost the game, correct word is {guess_word}")
        break
    print(f"Number of turns left to guess word is : {max_chances - current_turn}")
