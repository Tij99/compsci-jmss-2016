

'''
1. String concatenation:
        	x="cat"
        	y="dog"

        	What does x+y equal?


Write a for loop that takes a list of words
words=["cat","dog","fish","sugar glider","frog","rabbit"]
makes it into one string and prints out that string.
'''

words = ["cat","dog","fish","sugar glider","frog","rabbit"]

finalword = ""
look_for = "cat"
replace_with = "dog"

for word in words:
    if word == look_for:
        word = replace_with
    finalword += word

print(finalword)

# 2. Now INSIDE the for loop, search for a particular word and change it in the
# final string. Eg search for "cat" and change it to "dog" before you create the string.

# 3a. Now write a for loop that prints out the position in the list of a particular
# word, input by the user (ie if the user enters “cat” it should print 0, if they enter
#  “fish”, it prints 2. If the word is not in the list it should print "not found")


# 3b. Change your for loop to use the index instead of the items.
