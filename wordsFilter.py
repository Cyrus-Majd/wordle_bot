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