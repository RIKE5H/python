import random
# simple calculator but with a small tweak the previous calculation can be continued
def add(num1, num2):
    return num1 + num2

def multiply(num1, num2):
    return num1 * num2

def subtract(num1, num2):
    return num1 - num2

def divide(num1, num2):
    return num1 / num2

operations = {
    '+' : add,
    '-' : subtract,
    '/' : divide,
    '*' : multiply
}

num1 = int(input("What's the first number? : "))
num2 = int(input("what's the second number? :"))

[print(x) for x in operations.keys()]

operation_symbol = input("Pick an operation from live above: ")

calculation_function = operations[operation_symbol]
answer = calculation_function(num1,num2)
print(f"The result is\n\n {answer}")
is_continued = True
while is_continued:
    if input(f"Type 'y' for continuing with {answer} and 'n' for exit: ") == 'y':
        num1 = answer
        num2 = int(input("What's the second number? : "))
        [print(x) for x in operations.keys()]
        operation_symbol = input("Pick an operation from live above: ")
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1,num2)
        print(f"The result is\n\n {answer}")
    else:
        is_continued = False


A = 1
J = K = Q = 10
cards = [A, 2,3,4,5,6,7,8,9,10,J, K, Q]
user_cards = []
dealer_cards = []

# idk if the below rules complies with the official rule but just made it so doesnot choose the same card
# to remove it you can just add another len(user_cards) == len(cards): next_card = random.choice(cards)
# who fking take so many card without going over 21
def choose_for_user():
    while True:
        next_card = random.choice(cards)
        if next_card not in user_cards:
            return next_card
        else:
            continue
def choose_for_computer():
    while True:
        next_card = random.choice(cards)  
        if next_card not in dealer_cards:
            return next_card
        else:
            continue
        

def blackjack():

    first_cards = random.choices(cards, weights=None, k=2)
    second_card = random.choices(cards, weights=None,k=2)
    
    user_cards.extend(first_cards)
    dealer_cards.extend(second_card)
    
    print(f"Your cards : {user_cards}\nDealer Cards : {dealer_cards[0]}")
    
    playing =  True
    while playing:
        if input("Type 'y' to get another card or 'n' to pass: ") == 'y':
            user_cards.append(choose_for_user())
            dealer_cards.append(choose_for_computer())
            print(f"Your cards : {user_cards}\nDealer Cards : {dealer_cards[0:len(dealer_cards)-1]}")
        else:
            playing = False

    print("\n")         
    user_total = sum(user_cards)
    dealers_total = sum(dealer_cards)
    print(f"Your total = {user_total} computer totals = {dealers_total}")
    if dealers_total != user_total:
        if user_total > 21 :
            print("You went over 21 you lose the game")
        elif user_total == 21:
            print("Congratulation blackjack, you win")
        else:
            if user_total > 21:
                print("Dealer went over you lose")
            else:
                if dealers_total < 21 and dealers_total < user_total:
                    print("Dealer lost the game, Cogratulation you win")
                elif dealers_total == 21:
                    print("black jack dealer won the game")
                else:
                    print("Dealer won the game")
    else:
        print("its a tie") 

while True:
    if input("do you want to play the black jack game 'y' for yes 'n' for no: ") == 'y':
        blackjack()
    else:
        print("have a good day\n")
        break
    