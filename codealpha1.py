import random

def choose_word():
    words = ["python", "hangman", "programming", "computer", "code", "developer", "challenge"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    print("Welcome to Hangman!")
    secret_word = choose_word()
    guessed_letters = []
    incorrect_attempts = 0
    max_attempts = 6

    while True:
        current_display = display_word(secret_word, guessed_letters)
        print("Current word:", current_display)
        guess = input("Guess a letter: ").lower()

        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("You already guessed that letter. Try again.")
            elif guess in secret_word:
                guessed_letters.append(guess)
                print("Good guess!")
            else:
                incorrect_attempts += 1
                print(f"Incorrect guess! {max_attempts - incorrect_attempts} attempts left.")

            if set(guessed_letters) == set(secret_word):
                print("Congratulations! You guessed the word:", secret_word)
                break

            if incorrect_attempts == max_attempts:
                print("Sorry, you ran out of attempts. The word was:", secret_word)
                break
        else:
            print("Invalid input. Please enter a single letter.")

if __name__ == "__main__":
    hangman()
