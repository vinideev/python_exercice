# Open with R for read my doc story.txt

with open(".python/madlibs/story.txt", "r") as f:
    story = f.read()

words = set()  #Using set to find just the unique words without repeat
start_word = -1

# to open bracket and clor bracket 

symbol_start = "<"
symbol_final = ">"

#To find the beginning of the word we use this first condition

for i,char in enumerate(story):
    if char ==  symbol_start:
        start_word = i

# In here char will receive the final symbol and the index to add the words

    if char == symbol_final and start_word != -1:
        word = story[start_word: i + 1]
        words.add(word)
        start_word = -1


# To choise the news words in our history
         
answers = {}

for word in words:
    answer = input("Enter a word for" + word + ": ")
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word])


print(story)