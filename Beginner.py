############# DAY 1

# print('Welcome to the band name generator')
# city = input('Which city? ')
# pet = input('Name of your pet? ')
# print('A name might be: ' + city + ' ' + pet)

############# DAY 2

# number = input('Enter a two digit number! ')
# print(int(number[0]) + int(number[1]))

# height = float(input('Enter your height: '))
# mass = float(input('Enter your mass: '))
# print(int(mass/height ** 2))

# print(round(8 / 3 , 2))
# print(8 // 3) # gives an integer instead of float
# num = 5
# print(f"This is a {num}")

# age = int(input('How old are you? '))
# old = 90
# print(f'You have {old - age} years, {(old-age)*12} month, {(old - age)*52} weeks or {(old - age)*52*7} days left')

# print('Welcome to the tip calculator!')
# bill = float(input('What was the total bill? '))
# percentage = float(input('What tip would you like to give in percent? '))/100
# people = int(input('How many people to split the bill? '))
# pay = (bill + bill*percentage) / people
# final = "{:.2f}".format(round(pay,2))
# print(f'Each person should pay: ${final}')

############### DAY 3

# height = float(input('Enter your height: '))
# mass = float(input('Enter your mass: '))
# bmi = round(mass/height ** 2)

# if bmi < 18.5:
#     message = 'underweight'
# elif bmi < 25: # not needed (bmi >= 18.5 and)
#     message = 'normal weight'
# else:
#     message = 'overweight'

# print(f'Your are {message}, as your bmi is {bmi}')


# year = int(input('Which year do you want to check? '))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(f'{year} is a leap year.')
#         else:
#             print(f'{year} is not a leap year.')
#     else:
#         print(f'{year} is a leap year.')    
# else:
#     print(f'{year} is not a leap year.')

# name1 = input('Enter the first complete name: ').lower()
# name2 = input('Enter the second complete name: ').lower()
# combined = name1 + name2

# firstLetters = 'true'
# secondLetters = 'love'
# firstDigit = 0
# secondDigit = 0
# for letter in firstLetters:
#     firstDigit += combined.count(letter)
# for letter in secondLetters:
#     secondDigit += combined.count(letter)
# result = str(firstDigit)+str(secondDigit)
# print(f'Your score is {result}.')

################## DAY 4
# import random
# randomInteger = random.randint(1,10)
# randomFloat = random.random();
# randomBool = random.getrandbits(1)
# if randomBool == 0:
#     print('Head')
# else:
#     print('Tail')

# pythonList = ['h', 'i', 'o']
# pythonList.append('hu')
# pythonList.extend(['h','e','y'])
# print(pythonList)

# import random
# namesString = input("Input everybody's name, seperated with a comma: ")
# names = namesString.split(', ')
# winnerIndex = random.randint(0,len(names)-1)
# print(f"{names[winnerIndex]} will pay up for everyone")
# # other possibility:choice

# myChoice = int(input("Rock (1) - Paper (2) - Scissors (3): "))
# computerChoice = random.randint(1,3)
# print(computerChoice);

# if myChoice == computerChoice:
#     print('Equal')
# elif myChoice == 3 and computerChoice == 1:
#     print('You lose')
# elif myChoice > computerChoice:
#     print('You win')
# elif myChoice == 1 and computerChoice == 3:
#     print('You win')
# elif myChoice < computerChoice:
#     print('You lose')

################ DAY 5
# fruits = ['apple', 'banana', 'orange']
# numbers = [2,4,6,3,2,8,2,7,9,4]
# for fruit in fruits:
#     print(fruit)

# for index in range(0, len(fruits)):
#     print(index)

# maxNumber =  0
# for number in numbers:
#     if number > maxNumber:
#         maxNumber = number
# print(maxNumber)        

# summe = 0
# for number in range(1,101): # last number is not included
#     # optional third argument for step size
#     summe += number
# print(summe)

# total = 0
# for number in range(2,101,2):
#     total += number
# print(total)

# for number in range(1,101):
#     if number % 15 == 0:
#         print('FizzBuzz')
#     elif number % 5 == 0:
#         print('Buzz')
#     elif number % 3 == 0:
#         print('Fizz')
#     else:
#         print(number)

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# letterList = [0]*nr_letters
# symbolList = [0]*nr_symbols
# numberList = [0]*nr_numbers

# for i in range(0,nr_letters):
#     letterList[i] = letters[random.randint(0,len(letters)-1)]

# for i in range(0,nr_symbols):
#     symbolList[i] = symbols[random.randint(0,len(symbols)-1)]

# for i in range(0,nr_numbers):
#     numberList[i] = numbers[random.randint(0,len(numbers)-1)]

# password = ''.join(letterList) + ''.join(symbolList) + ''.join(numberList)
# print(password)

#########
password = ''
for char in range(0,nr_letters):
    password += random.choice(letters)
for char in range(0,nr_symbols):
    password += random.choice(symbols)
for char in range(0,nr_numbers):
    password += random.choice(numbers)
print(password)

passwordList = list(password)
random.shuffle(passwordList)

password = ''
for char in passwordList:
    password += char

print(f"Your password is: {password}")