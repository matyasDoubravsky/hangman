import re
import string
from random import choice

def play_hangman():
    word_pool = ["python", "java", "kotlin", "javascript"]
    picked_word = choice(word_pool)
    hidden_word = ("-" * (len(picked_word)))
    used_letters = []
    index = 0
    lives = 8
    wanna_play = input("Type \"play\" to play the game, \"exit\" to quit: ")
    print()
    print(hidden_word)
    if wanna_play == "play":
        while lives > 0:
            if hidden_word == picked_word:
                print()
                print(hidden_word)
                print("You guessed the word!")
                print("You survived!")
                print()
                play_hangman()
            letter = input("Input a letter: ")
            if len(letter) != 1:
                print("You should input a single letter\n")
                print(hidden_word)
            elif letter not in string.ascii_lowercase:
                print("It is not an ASCII lowercase letter\n")
                print(hidden_word)
            elif letter in used_letters:
                print("You already typed this letter\n")
                print(hidden_word)
            elif letter not in picked_word:
                used_letters.append(letter)
                lives -= 1
                print("No such letter in the word")
                if lives == 0:
                    print("You are hanged!")
                    print()
                    play_hangman()
                print()
                print(hidden_word)
            elif letter in picked_word:
                used_letters.append(letter)
                all_positions = [i.start() for i in re.finditer(letter, picked_word)]  # returns all indexes on which you can find the letter [x, x, x, ...]
                position = all_positions[index]
                while index <= len(hidden_word) - 1:
                    if picked_word[index] == letter:
                        hidden_word = hidden_word[:index] + letter + hidden_word[index + 1:]
                    index += 1
                print()
                print(hidden_word)
            index = 0
    elif wanna_play == "exit":
        exit()
    else:
        play_hangman()

print("H A N G M A N")
play_hangman()
