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
        words = line.split(" ")
            #now we need to add each word to the dictionary as it's own key 
        for word in words:
        #dictionary.get(word, 0) += 1
            counts[word] = counts.get(word,0) + 1
    # letter_count[letter] = letter_counts.get(letter,0) +1
    # return dictionary
    
    # counts.items()
    for item in counts.items():
        print(item)
    return item
