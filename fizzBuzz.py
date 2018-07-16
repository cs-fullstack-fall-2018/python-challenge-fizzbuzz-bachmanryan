import os

os.system("clear")

my_file = open("fives.txt", "w+")
my_otherFile = open("three.txt", "w+")
my_anotherFile = open("both.txt", "w+")
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        my_anotherFile.write(str(num) + "\n")
        print("FIZZBUZZ: ", num)
    elif num % 5 == 0:
        my_file.write(str(num) + "\n")
        print("BUZZ: ", num)
    elif num % 3 == 0:
        my_otherFile.write(str(num) + "\n")
        print("FIZZ: ", num)
    else:
        print(num)
