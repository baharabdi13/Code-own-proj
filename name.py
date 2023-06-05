import random

## -- List -- ##
score = 0
words = ["flood", "record", "sparks", "contain", "haircut", "busy", "spiders", "coding", "tasteful", "dreamy", "agree", "meddle", "harsh", "impolite", "chess", "grumpy", "wonder", "respect", "honorable", "camera", "friend", "skates", "tooth", "dancer", "whistle", "bump", "yellow", "elastic", "direction", "queen", "rhythm", "pink", "charge", "house", "produce", "hungry", "spotted", "previous", "physical", "typical", "beef", "travel", "rocky", "teacher", "wobble", "jumpy", "history", "night", "airport", "proud"]

#### ---- JUMBLE ---- ####

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
    score += 1
    print("You got it!")
    print (score)
else:
    print("Sorry, the correct answer was \"" + word + "\".")
    score -= 1
