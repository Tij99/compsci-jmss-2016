stuff = []

repeat = int(input("How many repeats?"))

for i in range(repeat):

    val = input("Please enter a number")

    if val == "q":
        break

    stuff.append(val)

    if len(stuff) >= 100:
        break

print(stuff)

#1) Change the program so that it takes a value and loops that number of times.

#2) Change the program so that the number of loops doesn't go beyond 100.

#3) Make it so that the user can quit the program by entering a specific input.