# Write a program to read in words from the keyboard one at a time until the word "quit" is typed.
# Store them in a list then print them alphabetically

'''i = 0
p = 0
o = 0

response = ""
words = []
letters = []
word_number = int
letters_number = int

while response.lower() != "quit":
    response = input("Enter word")
    words.append(response)

word_number = len(words) - 1

words.remove(words[word_number])

while p <= word_number:
    string = words[p]
    letters_number = len(string)
    while o < letters_number:
        letters.append(string[o])
    i = i + 1

print(letters)
exit()'''

# ^ I thougt we had to make a program that splits and prints individual letters

response = ""

while response.lower() != "quit":
    response 