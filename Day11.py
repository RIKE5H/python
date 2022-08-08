import random
# guessing game


# computer_number = random.randint(1, 101)


# def game(lives):
#     print("\n----Welcome to number guessing game-----\nI'm thinking between number between 1 to 100")
#     while lives > 0:
#         print("\n")
#         user_input = int(input(f"You have {lives} lives remaining\nMake a guess:"))
#         if user_input < computer_number:
#             lives -= 1
#             print("Sorry low")
#         elif user_input > computer_number:
#             lives -=1
#             print("Sorry high")
#         else:
#             print("you guessed the number correct")
#             break
#     if lives == 0:       
#         print(f"\nYou ran out of lives. The number was {computer_number}") 

# if input("Choose a dificulty type : Type 'easy' or 'hard': ").lower() == 'easy':
#     lives = 10
#     game(lives)
# else:
#     lives = 5
#     game(lives)
    
# higher or lower game
# if you want to know how the games works search for higher or lower game in searchbar

# make a dictionary and if you want a longer list fill the data yourself sike
store_room = {
    "neymar": 1000,
    "kim_Kardashian": 200000,
    "messi": 300000000,
    "ronaldo": 1000000000,
    "nike": 3000000,
    "adidas": 10000000,
    "puma": 400000,
    "tesla": 2000000
}

keylist = []
[keylist.append(x) for x in store_room.keys()]
result = True
prev = score = 0
next = 1
print("------Welcome to higher or lower Game------\nType 'y' for yes and 'n' for no")
while result:
    
    character_one = keylist[prev]
    character_two = keylist[next]
    
    if input(f"{character_one} has more followers than {character_two} : ").lower() == 'y':
        
        c1_fcount = store_room[character_one]
        c2_fcount = store_room[character_two]
        
        if c1_fcount < c2_fcount:
            print(f"sorry your you lost\n{character_two} followers: {c2_fcount} || {character_one} followers: {c1_fcount}")
            result = False
    score += 1
    prev = next
    next += 1
