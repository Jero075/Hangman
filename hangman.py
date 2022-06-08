picture =[
"          \n          \n          \n          \n           \n           ",
"          \n          \n          \n          \n      /    \n     /     ",
"          \n          \n          \n          \n      / \  \n     /   \ ",
"       |  \n       |  \n       |  \n       |  \n      / \  \n     /   \ ",
"-------|  \n       |  \n       |  \n       |  \n      / \  \n     /   \ ",
"-------|  \n      \|  \n       |  \n       |  \n      / \  \n     /   \ ",
"-------|  \n |    \|  \n       |  \n       |  \n      / \  \n     /   \ ",
"-------|  \n |    \|  \n ◯    |  \n       |  \n      / \  \n     /   \ ",
"-------|  \n |    \|  \n ◯    |  \n/      |  \n      / \  \n     /   \ ",
"-------|  \n |    \|  \n ◯    |  \n/ \    |  \n      / \  \n     /   \ ",
"-------|  \n |    \|  \n ◯    |  \n/|\    |  \n      / \  \n     /   \ ",
"-------|  \n |    \|  \n ◯    |  \n/|\    |  \n/     / \  \n     /   \ ",
"-------|  \n |    \|  \n ◯    |  \n/|\    |  \n/ \   / \  \n     /   \ "]

word = input("Word: ").lower()
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

drawn = 0
right_guesses = ""
wrong_guesses = ""
end = False
while not end:
    print_word = ""
    for i in range(len(word)):
        if word[i] not in right_guesses:
            print_word += "-"
        else:
            print_word += word[i]
            
    if "-" not in print_word:
        print("You won!")
        break
    elif "-" in right_guesses:
        print("You won!")
        break
    elif drawn == len(picture)-1:
        print("You lost!")
        print("The word was: " + word)
        break
    
    print(picture[drawn])
    print(f"\n{print_word}")
    print("\nWrong guesses: " + wrong_guesses)
    guess = input("Guess a letter: ").lower()
    
    if guess not in right_guesses and guess not in wrong_guesses:
        if len(guess) == 1:
            if guess in word:
                right_guesses += guess
            else:
                wrong_guesses += guess
                drawn += 1
    print("\n\n\n\n\n")