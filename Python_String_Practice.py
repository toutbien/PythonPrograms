#Python Practice
#Modify the double_word function so that it returns the same word repeated twice, 
#followed by the length of the new doubled word.
#For example, double_word("hello") should return hellohello10.

def double_word(word):
    n = word + word
    return n + str(len(n))


print(double_word("hello")) # Should return hellohello10
print(double_word("abc"))   # Should return abcabc6
print(double_word(""))      # Should return 0

#practice with indexes
text = "Random text we put in for an example"
print (text[3],text[4],text[9])
#negative indexes
print (text[-2])
print (text[-3])

#Modify the first_and_last function so that it returns True if the first letter 
#of the string is the same as the last letter of the string, False if they’re 
#different. Remember that you can access characters using message[0] or message[-1].
def first_and_last(message):
    if message == "" or message[0] == message[-1]:
        return True
    else:
        return False

print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))

#slicing and dicing practice
name_object = "Fruityplum"
name_object[2:4] #returns "ui"
name_object[:5] #returns "Fruit"
name_object[3:] #returns "ityplum"
name_object[6:] + name_object[3:5] #returns "plumit"

#using a method to get an index (index returns first position which matches)
my_pets = "Dogs & Cats and Bunny or Chickens"
#my_pets.index("or")
#my_pets.index("&") #returns 5

#using index method, find the position of "x" in "supercalifragilisticexpialidocious"
word = "supercalifragilisticexpialidocious"
n= word.index("x")
print(n)

#check boolean in index
pets = "A large amount of animals including donkeys, pigs, and horses"
"dogs" in pets #returns False
"pigs" in pets #returns True

#function to update a new domain
def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:  #checks to make sure old email and old domain are being replaced
        index = email.index("@" + old_domain) 
        new_email = email[:index] + "@" + new_domain #string that has old email up to @ sign
        return new_email 
    return email

#handling things like user input is made easier by using upper() and lower()
#did the user answer yes or no
answer = 'YES'
if answer.lower() == "yes":
    print("User said yeaaaah")
    
answer ='no'
if answer.upper() == 'NO':
    print ("User said nah")

answer = ' sometimes i walk outside '
#answer.strip() #just prints the text for answer
#answer.lstrip() #removes the left hand space
#answer.rstrip() #removes the extra right hand space
#answer.count("e") #counts the occurence of letter e in answer (3)
#answer.endswith("side") #determines if the string ends with "side", False
answer.endswith("side ") #same here but is space sensitive, now True
