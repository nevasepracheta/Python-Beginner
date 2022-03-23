secret_word = "Monkey"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("Enter your guess: ")
        guess_count += 1
        if guess_count == 1:
            print("Clue : It's an animal!")
        if guess_count == 2:
            print("Final Clue: It's your very old ancestor!")
    else:
        out_of_guesses = True
if out_of_guesses:
    print("Out of guesses! You Lose!")
else:
    print("Hurray! You win!")
