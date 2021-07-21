import random
import gamewords
def choose_level():
    print("Choose a number corresponding to the level you want to play")
    print("Easy(1)\n"
          "Medium(2)\n"
          "Hard(3)")
    level = int(input("Choose level :"))
    return level

def get_word(words):
    word = random.choice(words)
    return word

def get_letter_count(letter, letters_list):
    letter_indices = []
    for each_index in range(len(letters_list)):
        if letters_list[each_index] == letter:
            letter_indices.append(each_index)
        else:
            pass

    return letter_indices

def word_operation(level):
    words = gamewords.game_words
    if level == 1:
        word = get_word(words)
        letters = list(word)

        letters_copy = letters.copy()
        removed_letters = []
        alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

        for loop in range(2):
            removed_letter = random.choice(letters_copy)
            if removed_letter in alphabet:
                removable_indices = get_letter_count(removed_letter, letters_copy)
                for each_index in removable_indices:
                    letters_copy[each_index] = "_"
                removed_letters.append(removed_letter)
            else:
                while removed_letter not in alphabet:
                    removed_letter = random.choice(letters_copy)
                removable_indices = get_letter_count(removed_letter, letters_copy)
                for each_index in removable_indices:
                    letters_copy[each_index] = "_"
                removed_letters.append(removed_letter)

    elif level == 2:
        word = get_word(words)
        letters = []
        for letter in word:
            letters.append(letter)

        letters_copy = letters.copy()
        removed_letters = []
        alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

        for loop in range(len(letters_copy) - 1):
            removed_letter = random.choice(letters_copy)
            if removed_letter in alphabet:
                removable_indices = get_letter_count(removed_letter, letters_copy)
                for each_index in removable_indices:
                    letters_copy[each_index] = "_"
                removed_letters.append(removed_letter)
            else:
                pass
    else:
        word = get_word(words)
        letters = []
        for letter in word:
            letters.append(letter)

        letters_copy = letters.copy()
        removed_letters_set = set(letters_copy.copy())

        for each_index in range(len(letters_copy)):
            letters_copy[each_index] = "_"

        removed_letters = list(removed_letters_set)

    return [word, letters, letters_copy, removed_letters]

def draw_hangman(chances):
    hangman = [
        ["_", "_", "_", "_", "_", "_"],
        [" ", "|", " ", " ", " ", " ", "|"],
        [" ", "O", " ", " ", " ", " ", "|"],
        ["/", "|", "\\", " ", " ", " ", "|"],
        [" ", "|", " ", " ", " ", " ", "|"],
        ["/", " ", "\\", " ", " ", " ", "|"],
        [" ", " ", " ", " ", " ", " ", "|"],
        ["_", "_", "_", "_", "_", "_", "|"]
    ]
    if chances == 3:
        for part in hangman[0]:
            print(part, end = " ")
        print()
        for times in range(6):
            for space in hangman[6]:
                print(space, end = " ")
            print()
        for part in hangman[7]:
            print(part, end = " ")
        print()
    elif chances == 2:
        for index in range(2):
            for parts in hangman[index]:
                print(parts, end = " ")
            print()
        for times in range(4):
            for space in hangman[6]:
                print(space, end = " ")
            print()
        for each in hangman[7]:
            print(each, end = " ")
        print()
    elif chances == 1:
        for index in range(4):
            for parts in hangman[index]:
                print(parts, end = " ")
            print()
        for times in range(3):
            for space in hangman[6]:
                print(space, end = " ")
            print()
        for each in hangman[7]:
            print(each, end = " ")
        print()
    else:
        for each in hangman:
            for part in each:
                print(part, end = " ")
            print()

def get_guess_options(missing_letters):
    x = missing_letters
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    other_letters = []
    for times in range(10):
        random_letter = random.choice(alphabet)
        if random_letter not in missing_letters:
            other_letters.append(random_letter)
        else:
            pass
    final = x + other_letters
    return set(final)

def guess_letters(word_list, correct_combination):
    incomplete_word = str()
    for character in word_list[2]:
        incomplete_word = incomplete_word + character + " "
    chances = 3
    print(f"You have {str(chances)} remaining chances")
    draw_hangman(chances)
    print(f"Guess the missing letters in the word below \n"
          f"{incomplete_word}")
    guess_options = get_guess_options(word_list[3])

    while "_" in word_list[2] and chances > 0:
        print(f"Guess a letter from the following set {guess_options}")
        my_guess = input("Guess a letter in the set of letters above\n"
                         "If you input more than one letter only the first letter will be picked\n"
                         "My guess : ").lower()
        first_letter = my_guess[0]
        my_guess = first_letter
        if my_guess in correct_combination:
            guess_indices = []
            for index in range(len(word_list[1])):
                if word_list[1][index] == my_guess:
                    guess_indices.append(index)
                else:
                    pass

            for index in guess_indices:
                word_list[2][index] = my_guess

            incomplete_word = str()
            for character in word_list[2]:
                incomplete_word = incomplete_word + character + " "
            print(f"'{my_guess}' is CORRECT")
            print(incomplete_word)
            correct_combination.remove(my_guess)
            guess_options.remove(my_guess)
        else:
            chances = chances - 1
            print(f"'{my_guess}' is INCORRECT")
            print(f"You have {str(chances)} remaining chances")
            draw_hangman(chances)
            if my_guess in guess_options:
                guess_options.remove(my_guess)
            else:
                pass

    final_word = str()
    for character in incomplete_word:
        if character != " ":
            final_word = final_word + character
        else:
            pass

    if final_word == word_list[0]:
        print(f"YOU WIN\n"
              f"'{word_list[0]}' was the correct word")
    else:
        print(f"GAME OVER. YOU LOST\n"
              f"'{word_list[0]}' was the correct word")

def play_hangman():
    print("Hangman")
    level = choose_level()
    word_list = word_operation(level)
    guess_letters(word_list, word_list[3])

play_hangman()



