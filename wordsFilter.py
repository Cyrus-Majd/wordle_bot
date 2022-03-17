

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

wordsOfCorrectLength = [] # here we go again with the long variable names nonsense

# get rid of words that are not 5 letters long
def filterByLength():
    wordFile = open("allEnglishWords.txt", 'r')
    lines = wordFile.readlines()
    for line in lines:
        if (len(line) == 6):
            print(line)
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

    

    english_words = hashWords()
    target = input("Enter the word you want to find in the dataset\n")
    print(target in english_words)

# fake main method because python is smart :)
if __name__ == '__main__':
    main()