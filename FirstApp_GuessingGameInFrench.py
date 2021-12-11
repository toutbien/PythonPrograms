#!/usr/bin/env python
# coding: utf-8

import random

number = random.randint(1, 17)
player_name = input('Bonjour, Comment tu tappelles? ')

number_of_guesses = 0

print('Daccord '+ player_name+ ', Je vais deviner un numbre entre 1 et 17: ')

guess = input('Quelle est votre guess?: ')

while number_of_guesses <6:
    guess = int(input())
    number_of_guesses += 1
    if guess <number:
        print('Votre guess est trop petit')
    if guess >number:
        print('Votre guess est plus grande')
    if guess ==number:
        break
if guess ==number:
        print('Vous avez devine le numbre en '+ str(number_of_guesses+1)+ ' tentatives!')
else:
        print('Vous navez pas devine le numbre. Le numbre etait ' + str(number))

        
print('Bon anniversaire, '+player_name+ ' !')



