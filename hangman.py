import random

def play_hangman():
    # 5 predefined words ki list (No external API needed)
    word_list = ["python", "codealpha", "developer", "internship", "computer"]
    secret_word = random.choice(word_list)
    guessed_letters = []
    attempts_left = 6

    print("--- Welcome to Hangman Game ---")
    
    while attempts_left > 0:
        # Word display logic (e.g., p _ t h o _ )
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        
        print("\nWord to guess: ", display_word.strip())
        print(f"Attempts left: {attempts_left}")
        print(f"Guessed letters: {', '.join(guessed_letters) if guessed_letters else 'None'}")
        
        # Check if player won
        if "_" not in display_word:
            print(f"\n🎉 Congratulations! You guessed the word correctly: {secret_word}")
            break
            
        # User input taking
        guess = input("Guess a letter: ").lower()
        
        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter a single valid letter.")
            continue
            
        if guess in guessed_letters:
            print("⚠ You already guessed that letter. Try another one.")
            continue
            
        guessed_letters.append(guess)
        
        # Guess checking
        if guess in secret_word:
            print(f"✅ Good job! '{guess}' is in the word.")
        else:
            print(f"❌ Oops! '{guess}' is not in the word.")
            attempts_left -= 1
            
    if attempts_left == 0:
        print(f"\n💀 Game Over! You ran out of attempts. The word was: {secret_word}")

if __name__ == "__main__":
    play_hangman()