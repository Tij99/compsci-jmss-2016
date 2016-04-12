# write a program that reads in 10 numbers, then prints the sum of those
i = 1
numbers = []  # List

while i <= 10:
    response = input("Enter number " and i)  # I am trying to print: Enter the (value of i), but and is not the correct code.
    numbers.append(int(response))
    i = i + 1

while i > 10:
    Sum = int(numbers[0] + numbers[1] + numbers[2] + numbers[3] + numbers[4] + numbers[5] + numbers[6] + numbers[7] + numbers[8] + numbers[9])
    print("The sum of the 10 numbers entered is " and Sum)
    exit()