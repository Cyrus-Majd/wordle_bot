from gettext import find
from time import sleep # i like sleeping
import operator

## the massive brain algorithm:

# INPUT FOR FIRST ITERATION: nothing do a wild guess
# 1st guess. come up with a random *completely diverse* word. so no repeating letters in the word.
# the word should be skewed to the LEFT of the letter distribution diagram. So as to maximize chance of hitting correct letters.
# OUTPUT OF FIRST GUESS: some letters not in the word, maybe some yellow, maybe some green

# INPUT FOR SECOND ITERATION: the black, yellow, and green values.
# 2nd guess. completely cross out (remove) all black letters from the word frequency distribution diagram.
# take a guess with the constaints that there MUST BE greens in the correct spots and there MUST BE a yellow somewhere
# OUTPUT OF SECOND GUESS: some letters not in the word, maybe some yellow, maybe some green

# repeat this logic for all iterations.

## SELECTION CRITERIA FOR PICKING A RANDOM WORD SKEWED TO THE LEFT: assign a "value" to each letter in the letter distribution diagram.
# we add the values of each letter for each word and assign each word to a value. the highest value words mean that they contain the most left-skewing letters.
# we then just add a constaint that says keep going until you find a completely diverse match.

# list of all words with length 5.
wordsOfCorrectLength = [] # here we go again with the long variable names nonsense

# map corresponding letters to frequency values.
lettersValues = {
    "E":12.02,
    "T":9.10,
    "A":8.12,
    "O":7.68,
    "I":7.31,
    "N":6.95,
    "S":6.28,
    "R":6.02,
    "H":5.92,
    "D":4.32,
    "L":3.98,
    "U":2.88,
    "C":2.71,
    "M":2.61,
    "F":2.30,
    "Y":2.11,
    "W":2.09,
    "G":2.03,
    "P":1.82,
    "B":1.49,
    "V":1.11,
    "K":0.69,
    "X":0.17,
    "Q":0.11,
    "J":0.10,
    "Z":0.07,
    "\n":0.0,
}

# map corresponding each word to its value.
wordValues = {}

# superior version of the map above lol
wordValuesSorted = {}

# filters list by greens constraint
def cutDownList(wordValuesSorted, greens):
    for each in list(wordValuesSorted.keys()):
        for index in list(greens.keys()):
            # print("checking", each[index], "with", greens[index].lower())
            if (each[index] != greens[index].lower()):
                # print("uh oh.", each[index], " is not ", greens[index].lower())
                # print("deleting:", each, "with a value of", wordValuesSorted[each])
                del wordValuesSorted[each]
                break
    return wordValuesSorted

# gives the green letters
def analyzeResult(result):
    capitals = {} # keep track of uppercase (green and yellow and black, basiclly the capital letters) letters and their locations. LOCATION is KEY and LETTER is VALUE
    print("lookin at result")
    counter = 0
    for each in result:
        # print(each)
        if (each.isupper()):
            # print(each, "is uppercase!")
            capitals[counter] = each
        counter = counter + 1
    print(capitals)
    return capitals

# uhm... interacts with human?
def interactWithHuman(wordValuesSorted):
    # FIRST GUESS. BASICLALY HIGHEST VALUE DIVERSE WORD.
    print("Highest Value & Most Unique Word (FIRST GUESS):", highestUniqueWord(wordValuesSorted), "\nValue:", wordValuesSorted[highestUniqueWord(wordValuesSorted)])

    print()

    result = input("enter the result. green letters should be caps. ex: aPPlE means the Ps and the E are in the correct spot and are right.\n")
    resultGreen = result[0:result.find(",")]
    resultYellow = result[result.find(",")+1:result.find(",")+len(resultGreen)+1]
    resultBlack = result[result.find(",")+len(resultYellow)+2:]

    print(resultGreen)
    print(resultYellow)
    print(resultBlack)

    greens = analyzeResult(resultGreen) # gives the greens.
    wordValuesSorted = cutDownList(wordValuesSorted, greens)

    print("list after filter:", wordValuesSorted) # OH MY FUCKING GOD IT ACTUALLY WORKED. I FILTERED BY THE GREEN LETTERS WTF!!!! LETS GOOOOO


# checks if letters ina  word repeat. 
def isUnique(word) -> bool:
    return len(set(word)) == len(word)

# this function should return the same thing every time, i just wanna know the highest value most completely diverse word for my first wordle guess.
def highestUniqueWord(dict) -> str:
    for each in list(dict.keys()):
        if isUnique(each.upper()):
            return each
    return "bruh. no unique values? :megamindPleadingFace:"

def findBestCandidate(wordValuesSorted) -> str:
    return ""

def valuePerWord(word) -> float:
    sum = 0.0
    for each in word:
        sum = sum + float(lettersValues[each.upper()])
    # print("WORD:", word, "SUM:", sum)
    return sum

# function to calculate the values of all words. puts results in wordValues map.
def calculateAllValues():
    for each in wordsOfCorrectLength:
        each = each[:-1]    # get rid of stoopid \n character that messes with mah wordValues dictionary
        wordSum = valuePerWord(each)
        wordValues[each] = wordSum

# get rid of words that are not 5 letters long
def filterByLength():
    wordFile = open("allEnglishWords.txt", 'r')
    lines = wordFile.readlines()
    for line in lines:
        if (len(line) == 6):
            # print(line)
            wordsOfCorrectLength.append(line)


# method to throw all words in a hashset for easy recalling.
def hashWords():
    with open('allEnglishWords.txt') as word_file:
        valid_words = set(word_file.read().split())
    return valid_words

# main method
def main():
    # first, get rid of everything that is not exactly 5 chars long.
    filterByLength()
    calculateAllValues()

    # sleep(1)

    wordValuesSorted = dict(sorted(wordValues.items(), key=operator.itemgetter(1), reverse=True)) # now sorted :)

    # print(list(wordValuesSorted.keys()))

    print()
    # print("is 'apple' unique?", isUnique("apple"), "is 'aPe' unique?", isUnique("aPpe".upper()))

    # print(wordValuesSorted) ## this is all the words sorted by value.

    # throw it in a text file so i can quickly solve the wordle and impress my girlfriend :)
    with open('epic.txt', 'w') as f:
        f.write(str(wordValuesSorted))

    # welp. now i gotta do the hard part. user data input ;-;
    # i dont know what the hell kinda algorithm i wrote before but i dont wanna read it. NEW PLAN. take a guess. if nothing
    # works, tough luck, guess again with the next highest value word that doesnt have those exlcuded chars in the first word.
    # if you hit a match, just like select the next highest word with specific constriants. ok you know what i mean. go do it nerd.
    
    interactWithHuman(wordValuesSorted)

    ## this does some weird stuff with hashing the words but i dont need it anymore but its also genius sooo im keeping it
    # english_words = hashWords()
    # target = input("Enter the word you want to find in the dataset\n")
    # print(target in english_words)

# fake main method because python is smart :)
if __name__ == '__main__':
    main()