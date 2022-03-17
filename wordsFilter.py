

# method to throw all words in a hashset for easy recalling.
def hashWords():
    with open('allEnglishWords.txt') as word_file:
        valid_words = set(word_file.read().split())
    return valid_words

# main method
def main():
    english_words = hashWords()
    # demo print
    target = input("Enter the word you want to find in the dataset\n")
    print(target in english_words)

# fake main method because python is smart :)
if __name__ == '__main__':
    main()