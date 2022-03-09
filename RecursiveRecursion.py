#a recurssion can be called 1000x

#A recursive function must include a recursive case and base case.
#The recursive case calls the function again, with a different value. 
#The base case returns a value without calling the same function

#Typical recursion structure
from unittest import result


def recursive_function(parameters):
    if base_case_condition(parameters):
        return base_case_value
    recursive_function(modified_parameters)
    
#function of recurssion practice
def is_power_of(number, base):
  # Base case: when number is smaller than base.
  if number < base:
    # If number is equal to 1, it's a power (base**0).
    return number == 1

  # Recursive case: keep dividing number by base.
  return is_power_of(number/base, base)

print(is_power_of(8,2)) # Should be True
print(is_power_of(64,4)) # Should be True
print(is_power_of(70,10)) # Should be False

#another positive number run
def sum_positive_numbers(n):
  if n < 0:
    return -1
  elif n < 1:
    return 0
  else:
    return n + sum_positive_numbers(n-1)

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15