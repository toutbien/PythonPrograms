print("One"\)
#loop through numbers to 5
from multiprocessing.sharedctypes import Value
import numbers


def function_a():
    for x in range(5):
        print(x)

function_a()
    
def square(n):
    return n*n

print("Two"\)
#find the sum of squares
def sum_squares(x):
    sum = 0
    for n in range(x):
        sum += n*n
    return sum

print (sum_squares(10))

print("Three"\)
#create a string
friends = ['Sausage', 'Egg', 'Cheese']
#iterate for each of the items in the string
for friend in friends:
#print a greeting to the string members
    print("hi " + friend)

print("Four"\)   
#number list iteration example following the above logic
numbers = [12, 16, 25, 99, 84, 39, 56 ]
#creating 2 variables to use in the for loop for the iteration
sum = 0
length = 0
#iteration portion
for number in numbers:
    #adds the current value to the sum of values and one in length which calculates elements in the list
    sum += number
    length += 1
    
print ("Total sum: " + str(sum) + " - Average: " + str(sum/length))

#----Note-----#
#iteration in automation: the files in a directory, the lines of a file, running processes
#use FOR loops when iterating automation
#use WHILE loops when you want to repeat an action until a condition is satisfied/changed

print("Five"\)
#calculate the product for all numbers 1-12
product = 1
for n in range(1,12):
    product = product *n
    
print (product)

print("Six"\)
#factorials (multplication down a number)
def factorial(n):
    result = 1
    #iterate through 1 to keep the result positive and add one to n to factor
    for i in range(1, n+1):
        #return the result of the range times the variable +1
        result = result * i
    return result

print(factorial(4)) # should return 24
print(factorial(5))

print("Seven"\)
#increase factorization difference. this example converts fareinheit to celsius
def to_celsius(x):
    return (x-32)*5/9
#this goes in steps of 10 - we call 101 so it will caculate to 100 max
for x in range(0,101,10):
    print(x, to_celsius(x))
    
#---Note-----#
# Using range can receive 3 parameters total
#If it receives one parameter,
#it will create a sequence one by one from
#zero until one less than the parameter received.
#If it receives two parameters,
#it will create a sequence one by one from
#the first parameter until
#one less than the second parameter.
#Finally, if it receives three parameters,
#it will create a sequence starting from
#the first number and moving towards the second number.
#But this time, the jumps between the numbers
#will be the size of the third number,
#and again, it will stop before the second number. 
#So (0,101,10) = Start at 0, iterate through 100, and go by factors of 10
#range will stop one before the parameter specified.

print("Final Challenge"\)
#Final Nested For Loops (Dominoes challenge) using an END parameter
for left in range(7):
    for right in range (left, 7):
        print("[" + str(left) + "|" + str(right) + "]", end = " ")
    print()

#output all team matchup options without having team face itself
teams = ['Dragons','Tigers','Timberwolves','Bobcats','Gophers']
for home_team in teams:
    for away_team in teams:
#create a conditional that skips a case where both teams are the same
        if home_team != away_team:
            print(home_team + " vs " + away_team)
        
