#A while loop executes the body of the loop while the condition remains True

#A for loop iterates over a sequence of elements,
#executing the body of the loop for each element in the sequence
#For loops are mostly used when there's a pre-defined sequence or range of numbers to iterate.


def factorial(n):
    result = 1
    for x in range(1,n-1):
        result = result * x
    return result

for n in range(1,11):
    print(n, factorial(n+1))

#option 2 for same result   
def factorial(num):
  if num == 0:
    return num
  else:
    return num * factorial(num-1)

for n in range(1,11):
    print (n,factorial(n))

#cubes
for n in range(1,11):
    print(n**3)

#print multiples of 7 to 100    
for n in range(0,101,7):
    print(n)
    
    
def retry(operation, attempts):
  for n in range(attempts):
    if operation():
      print("Attempt " + str(n) + " succeeded")
        break
    else:
      print("Attempt " + str(n) + " failed")

retry(create_user, 3)
retry(stop_service, 5)

#user retry and break functions
def retry(operation, attempts):
  for n in range(attempts):
    if operation():
      print("Attempt " + str(n) + " succeeded")
      break
    else:
      print("Attempt " + str(n) + " failed")

retry(create_user, 3)
retry(stop_service, 5)


def factorial(n):
    result = 1
    if n == 0:
      return 1
    for x in range(1,n+1):
        result = result * x
    return result

for n in range(1,11):
    print(n, factorial(n+1))