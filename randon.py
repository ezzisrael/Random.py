# # #madlibs
# # youtuber = '@jameskoko'
# # print('subscribe to ' +  youtuber)
# # print('subscribe to {}'.format(youtuber))
# # print(f'subscribe to {youtuber}')


# adj = input('Adjective: ')
# verb1 = input('Verb: ')
# verb2 = input('Verb: ')
# famous_person = input('Famous person: ')

# madlib = f'computer programming is so {adj}! It makes me so exicted all the time becasue \
# i love to {verb1}. Stay hydrsted and {verb2} like you are {famous_person}!'
# print(madlib)

#Guessing NUmber
import random

 def guess (x):
     random_number = random.randint(1,x)
     guess = 0
     while guess != random_number:
         guess = int(input(f'Guess a number between 1 and {x}: '))
         if guess < random_number:
             print('Sorry guess again. Too low.')
         elif guess > random_number:
             print('Sorry guess again. Too high.')

     print('Yay, Congrants!. You have guessed the number.')



 num = int (input (“Enter any number to test whether it is odd or even: “)

 if (num % 2) == 0:
     print (“The number is even”)
 else:
     print (“The provided number is odd”)






def guess (x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Enter number guessed between 1 and {x}: '))

        if (x % 2) == 0 and guess < random_number:
            print('Sorry try again: Guess is an even number but too low')
        elif (x % 2) == 0 and guess > random_number:
            print('Sorry guess again. number guessed is even and too high')
        elif (x % 3) == 0 and guess > random_number:
            print('Sorry guess again. number guessed is odd and too high')
        elif (x % 3) == 0 and guess < random_number:
            print('Sorry try again: Guess is an odd number and too low')

    print(f'Weldone you have guessed right {random_number} correctly')

guess()

