import random

# just simple games as a python beginner

# lets build a head and tail game with some small tweak


# vitrual head and tails game
random_number = random.randint(0, 1)

print("Head") if random_number == 1 else print("Tails")


# who pays the bill game

# cannot use choice module haha
name_list = input("Enter the names || ex: rikesh,radhika,radhyeshyam: ")

names = name_list.split(",")

# lets pick a people using the random module but not choice

random_id = random.randint(0, len(names)-1)

print(f"{names[random_id]} will buy us the meal today")


# the treasure marking game 

row1 = ["🧱", "🧱", "🧱"]
row2 = ["🧱", "🧱", "🧱"]
row3 = ["🧱", "🧱", "🧱"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
# we will ask two value separated by space from the user like 2 3 and put the treasure there and print the spot as X
position = input("where do you want to put the treasure? : ")
pos = position.split(" ")

# convert to int and do -1 as array start from 0

map[int(pos[1])-1][int(pos[0])-1] = "X"

print("marked treasure: ")

# list are not immutable ie they are mutable
print(f"{row1}\n{row2}\n{row3}")


# rock paper scissors game

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]

# lets use the choice module this time it will be easier

computer_choice = random.choice(options)
human_choice = input("Enter 1 for 'rock' 2 for 'paper'  and  3 for 'scissor' : ")

# picking from the list to print (never forget that fucking -1)
h_choice = options[int(human_choice)-1]

print(f"Computer choice: \n{computer_choice}\n Your choice: \n{h_choice}")



if (computer_choice == rock and human_choice == "3") or (computer_choice == paper and human_choice== "1") or (computer_choice == scissors and human_choice == "2"):
    print("Sorry the computer won")
elif (computer_choice == h_choice):  # hchoice and computer choice both are from same list
    print("Its a tie")
else:
    print("Yahoo you won!")
