

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
}

# map corresponding each word to its value.
wordValues = {}

def valuePerWord(word):
    sum = 0.0
    print("type of sum", type(sum), "================")
    for each in word:
        print(each, "type of letters:", type(lettersValues.get(each.upper())) )
        sum = sum + lettersValues.get(each.upper())
        print(sum)
    return sum

# function to calculate the values of all words. puts results in wordValues map.
def calculateAllValues():
    for each in wordsOfCorrectLength:
        print("calling")
        type(valuePerWord(each))
        # wordSum = valuePerWord(each)
        print("setting")
        # wordValues[each] = wordSum

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

    # print(valuePerWord("AaA"))
    # each = "Aa"
    # print(lettersValues.get(each.upper()))
    

    # english_words = hashWords()
    # target = input("Enter the word you want to find in the dataset\n")
    # print(target in english_words)

# fake main method because python is smart :)
if __name__ == '__main__':
    main()