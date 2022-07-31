import os
# i created the program so that it will only decode and encode within the alphabet i.e upper alphabets
msg = input("Enter the message you want to encode: ").upper()
sft = int(input("Enter the number of shifts: "))

def encoder(message, shift):

    encoded_message = ''
    for i in message:
        if ord(i)+shift > ord('Z'):
            encoded_message += chr(ord('A')-1+(ord(i)+shift-ord('Z')))
        else:
            encoded_message += chr(ord(i)+shift)
    return encoded_message
print(encoder(msg, sft))


def decoder(message, unshift):
    decoded_message = ''
    for i in message.upper():
        if ord(i)-unshift < ord('A'):
            decoded_message += chr(ord('Z')-1-(ord(i)-unshift-ord('A')))
        else:
            decoded_message += chr(ord(i)-unshift)
    return decoded_message
m = input("Enter the message to be decoded: ")
s = int(input("Enter number of shits: "))

print(decoder(m, s))




biders = {}

result = True
while result:
    name = input("enter your name: ")
    price = input("Enter your biding price: ")
    biders[name] = price
    ans = input("Do you want to add any other biders| yes/no : ")
    os.system('cls')
    if ans == "no":
        result = False
[print(f"{key} : {value}") for key,value in biders.items()]