from random import randint

wordlist = []
"""wordlist = ["Adult", "Age", "Amount", "Area",
            "Back", "Bed", "Blood", "Body", "Book", "Box", "Boy", "Bulb", "Bunch", "Business",
            "Camera", "Chicken", "Child", "Chocolate", "City", "Clothes", "Colony", "Colors", "Company", "Computer", "Continent", "Council", "Country", "Course", "Cycle",
            "Dates", "Day", "Death", "Desk", "Door",
            "Egg",
            "Face", "Fact", "Factory", "Family", "Farm", "Farmer", "Father","Fish", "Floor", "Flowers", "Food", "Fridge", "Future",
            "Game", "Garden", "Gas", "Glass", "Group",
            "Health", "Hill", "Hospital",
            "Idea", "Image", "Industry", "Island",
            "Jewelry", "Job",
            "Kitchen",
            "Land", "Law", "Leaves", "Leg", "Letter", "Life",
            "Magazine", "Market", "Metal", "Mirror", "Mobile", "Money", "Morning", "Mother", "Mountain", "Movie",
            "Name", "Nest", "News",
            "Ocean", "Oil",
            "Painter", "Park", "Party", "Pen", "Pencil", "Person", "Picture", "Pillow", "Place", "Plant", "Pond",
            "Rain", "Rate", "Result", "Ring", "Road", "Rock", "Rocket", "Room", "Rope", "Rule",
            "Sale", "School", "Shape", "Shapes", "Ship", "Shop", "Sister", "Site", "Skin", "Snacks", "Son", "Song", "Sort", "Sound", "Soup", "Sports", "State", "Stone", "Street", "System",
            "Taxi", "Tea", "Teacher", "Team", "Toy", "Tractor", "Trade", "Train",
            "Video", "View",
            "Water", "Waterfall", "Week", "Women", "Wood", "Word",
            "Year", "Yesterday"]"""

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

if wordlist == []:
    word = input("Word: ").lower()
else:
    word = wordlist[randint(0, len(wordlist)-1)].lower()
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
