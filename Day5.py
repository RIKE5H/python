import random


# average height exercise

student_heights = input("Enter a list of student heights: ").split()
sum = 0
for n in range(0,len(student_heights)):
    sum += int(student_heights[n])
total = len(student_heights)
average = sum/total
print(f"The average height of student is {average} cm")


scores = input("Enter a list of students score: ").split()
max = 0
for x in scores:
    if int(x) > max:
        max = int(x)
print(f"The highest score is {max}")


# printing the sum of even numbers from 0 to 101 
even_sum = 0
for i in range(2, 101,2):
    even_sum += i
print(f"The sum of even numbers from 1 to 100 is {even_sum}")

# the fizz buzz challenge

for i in range(1, 101):
    if (i % 3 == 0 and i % 5 == 0):
        print("FizzBuzz")
    elif(i % 3 == 0):
        print("Fizz")
    elif(i % 5 == 0):
        print("Buzz")
    else:
        print(i)
        


# password generator

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
random.shuffle(letters)

numbers = ["1","2","3","4","5", "6", "7","8","9"]
symbols = ["!", "@", "#", "$", "^", "&", "*", "~"]

letter_count = int(input("How many letters do you want: "))
numbers_count = int(input("How many numbers do you want: "))
symbols_count = int(input("How many symbols do you want: "))
result =  True

while result: 
    
# not suited method but ok haha
# password_list = []

# choice_list = [letters, numbers, symbols]
# number_list = [letter_count, numbers_count, symbols_count]

# for n in range(0, 3):
#     password_list += random.choices(choice_list[n],weights=None,k=number_list[n])
                 
                 # OR
                 
    password_list = random.choices(letters, weights=None, k=letter_count)+random.choices(numbers, weights=None, k=numbers_count)+random.choices(symbols,weights=None, k=symbols_count)
    random.shuffle(password_list)
    generated_password = "".join(password_list)
    print(f"\nHere is your password: {generated_password}\n\n")
    
    user_choice = input("Do you want to generate again: Y/N ||: ").lower()
    if (user_choice != "y"):
        result = False
    