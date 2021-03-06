#recursion - the nested russian dolls or the middle man of the jerk

def factorial(n):
    if n < 2: #base case that n is smaller than 2
        return 1
    return n * factorial (n-1) #this is the recursive case

#xample
def factorial(n):
    print("Factorial called with " + str(n))
    if n < 2:
        print ("returning 1")
        return 1
    result = n *factorial(n-1)
    print("Returning " +str(result) + " for factorial of " + str(n))
    return result

factorial(4)

#returning positive number sums between n and 1
def sum_positive_numbers(n):
    # The base case is n being smaller than 1
    if n < 1:
        return 0
   
    # The recursive case is adding this number to 
    # the sum of the numbers smaller than this one.
    return n + sum_positive_numbers(n-1)

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15