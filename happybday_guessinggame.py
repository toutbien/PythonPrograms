#!/usr/bin/env python
# coding: utf-8

import random
import time

number = random.randint(1, 39)
player_name = input('Hi, What is your name? ')

number_of_guesses = 0

print('Alright '+ player_name+ ', You will pick any number between 1 and 39. You ready?')
time.sleep(3)
print ('By the way, you look fantastic today.')
time.sleep(3)
guess = input('Type your guess now and hit enter. I will tell you if you are correct: ')

while number_of_guesses <7:
    guess = int(input())
    number_of_guesses += 1
    if guess <number:
        print('Your number is too low')
    if guess >number:
        print('Your number is too high')
    if guess ==number:
        break
if guess ==number:
        print('You did great! You guessed it in '+ str(number_of_guesses+1)+ ' tries!')
else:
        print('Aw, shucks. You did not guess correctly. The number is ' + str(number))

        
print('Happy Birthday, '+player_name+ ', and Lisa too!')
