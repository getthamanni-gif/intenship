import random

# List of 5 predefined words
words = ["python", "computer", "program", "coding", "developer"]

# Select a random word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Number of incorrect guesses allowed
incorrect_guesses = 0
max_guesses = 6

# Display the hidden word
display = ["_"] * len(word)

print("🎮 Welcome to Hangman!")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses.")

while incorrect_guesses < max_guesses and "_" in display:

    print("\nWord:", " ".join(display))
    print("Guessed letters:", guessed_letters)
    print("Incorrect guesses:", incorrect_guesses)

    guess = input("Enter a letter: ").lower()

    # Check if input is a single letter
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    # Check whether the letter is in the word
    if guess in word:
        print("Correct! ✅")

        # Reveal the letter
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess

    else:
        incorrect_guesses += 1
        print("Wrong guess! ❌")

# Game result
if "_" not in display:
    print("\n🎉 Congratulations!")
    print("You guessed the word:", word)
else:
    print("\n💀 Game Over!")
    print("The word was:", word)