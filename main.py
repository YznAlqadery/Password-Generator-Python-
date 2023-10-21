import random

print("Welcome to Python Password Generator!")

password_length = int(input("How long do you want the password to be? "))

symbols_amount = int(input("How many symbols do you want to include? "))

numbers_amount = int(input("How many numbers do you want to include? "))

alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
             ,'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

symbols = ['#','@','&','-','_','*','+','$','%']

numbers = ['0','1','2','3','4','5','6','7','8','9']

password = []

def get_random_number(value):
    return random.randint(0,len(value) - 1)

total_length = password_length - symbols_amount - numbers_amount

for i in range(0,total_length):
    random_no = get_random_number(alphabets)
    password.append(alphabets[random_no])


for i in range(0,symbols_amount):
    random_no = get_random_number(symbols)
    password.append(symbols[random_no])

for i in range(0,numbers_amount):
    random_no = get_random_number(numbers)
    password.append(numbers[random_no])

final_password = ""
#Shuffling the password list
random.shuffle(password)

for i in password:
    final_password += i


print(f'Your final password is {final_password}')
