# copy the code from sum1.py into this file, THEN:
# change your program so it keeps reading numbers until it gets a -1, then prints the sum of all numbers read

i = 0
Sum = 0


while i == 0:
    response = input("Enter number")
    Sum += int(response)
    if response == "-1":
        print(Sum)
        exit()
