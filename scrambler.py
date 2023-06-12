import random
import pickle
from os import path

def save (object, file):
    """Serialize a dictionary to a file."""
    with open(file, "wb") as f:
        pickle.dump(object, f)

def load(file):
    """Load a dictionary from a serialized file.
     Or return None if the file doesn't exist."""
    if path.exists(file):
        with open(file, "rb") as f:
            return pickle.load(f)
    return None

# Get the previously saved dictionary of users if it exists
# Else start with an empty dictionary
USERS_FILE = "users.pkl"
users = load(USERS_FILE)
if users is None:
  users = {}

while True:
    user = input("Enter a username, or q to quit, u to see all users: ").capitalize()
    if user == "Q":
        break
    elif user == "U":
        for user, user_info in users.items():
          print (user, ": ", user_info, sep="")
    elif user in users:
        print("Welcome back", user)
    else:
        print("Welcome", user)
        users[user] = ""
  


## -- List -- ##
score = 0
words = ["blood", "sport", "light", "maintain", "hair", "work", "ants", "python", "yummy", "dream", "wrong", "distract", "bad", "rude", "cheese", "annoyed", "curious", "kind", "honor", "phone", "family", "bike", "feet", "swimmer", "football", "dumpy", "yellow", "rubber", "navigation", "king", "song", "red", "battery", "home", "create", "hunger", "spot", "before", "athletic", "usually", "chicken", "vacation", "rock", "teacher", "wiggle", "happy", "math", "night", "plane", "proud"]

#### ---- JUMBLE ---- ####
play = True
while play: 
## -- Word choice -- ##
    word = random.choice(words)

    ## -- Word jumble -- ##

    # Create a list of the word's characters, shuffle them,
    # and build a new string

    letters = list(word)
    random.shuffle(letters)
    word_jumbled = "".join(letters)

    #### ---- GUESS ---- ####

    ## -- Input -- ##

    print("Unscramble this word: " + word_jumbled)
    guess = input("Your guess: ")

    ## -- Comparison -- ##
    if guess == word:
        print("You got it!")
        score += 1
        print(score)
    
    else:
        if guess != word:
            print ("Sorry correct answer was \"" + word + "\".")
            print("Final score:", score)
            save(users, USERS_FILE)   # Save the updated dictionary on exit
            play = False
            

