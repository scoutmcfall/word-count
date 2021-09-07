"""Count words in file."""


def word_count(file):
    # open file 
    text_file = open(file)
    # make a dictionary to store the word counts
    counts = {}
    # make a list of each line and split words up by space.
    # for loop to go through each line, word by word
    for line in text_file:
        # for word in file 
        #make a list of words
        # rstrip() to remove trailing white space
        line = line.rstrip()
        words = line.split()
        #now we need to add each word to the dictionary as it's own key 
        for word in words:
            counts[word] = counts.get(word,0) + 1
    # letter_count[letter] = letter_counts.get(letter,0) +1
    # return dictionary
   
    # return item
    for key, value in counts.items():
        print(key, value)
    return None