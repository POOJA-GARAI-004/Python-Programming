import random

# Predefined list of words
words = ['apple', 'banana', 'grape', 'mango', 'peach']

# Choose a random word
word_to_guess = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

# Create a display of underscores for each letter
display_word = ['_'] * len(word_to_guess)

print("Welcome to Hangman!")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses allowed.")

# Game loop
while wrong_guesses < max_wrong_guesses and '_' in display_word:
    print("\nCurrent word:", ' '.join(display_word))
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word_to_guess:
        print("Good guess!")
        for idx, letter in enumerate(word_to_guess):
            if letter == guess:
                display_word[idx] = guess
    else:
        wrong_guesses += 1
        print(f"Wrong guess! You have {max_wrong_guesses - wrong_guesses} tries left.")

# Game result
if '_' not in display_word:
    print("\nCongratulations! You guessed the word:", word_to_guess)
else:
    print("\nGame Over! The word was:", word_to_guess)
