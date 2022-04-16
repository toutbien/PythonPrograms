#print the numbers 1 through 15
number = 1
while number != 16:
	print(number, end=" ")
	number += 1

#print out each letter of a word on a separate line
def show_letters(word):
	for letter in word:
		print(letter)

show_letters("Wowza")

#Ensure function digits(n) returns how many digits the number has.
def digits(n):
	count = 0
	if n == 0:
	  n = n +1 
	while (n != 0):
		count += 1
		n //= 10
	return count

#multiplication tables
def multiplication_table(start, stop):
	for x in range(1, start + 5):
		for y in range(1, start + 5):
			print(str(x*y), end=" ")
		print()

#up and down counters
def counter(start, stop):
	x = start
	if x>stop:
		return_string = "Counting down: "
		while x >= stop:
			return_string += str(x)
			if x>stop:
				return_string += ","
			x = x-1
	else:
		return_string = "Counting up: "
		while x <= stop:
			return_string += str(x)
			if x<stop:
				return_string += ","
			x = x+1
	return return_string


#even numbers from a string using a range
def even_numbers(maximum):
	return_string = ""
	for x in range(2, maximum +1, 2):
		return_string += str(x) + " "
	return return_string.strip()

#lets find out
for x in range(1, 10, 3):
    print(x)