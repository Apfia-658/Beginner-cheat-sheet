#basic concepts
print(2 + 2) #simple operations
print(5 + 4 - 3)

print( 8 / 2 ) #floats
print( 6 * 7.0 )
print( 4 + 1.65 )

print( 2**5 ) #exponents

print( 20 // 6 ) #floor division

print(20 % 6) #remainders
print(1.25 % 0.5) 

print(abs(-42)) #absolute value

#strings
print("Python is fun!")
print('Always look on the bright side of life')

print('One \nTwo \nThree') #newlines
print('1. \n 2. \n 3.')

print("Spam" + 'eggs') #concatenation
print("2" + "2")

print("spam" * 3) #string operations
print(4 * '2')

#variables
    # variables are CASE SENSITIVE (capitalization)
BigMan = "Schlatt" #assigning variables
age="42"

x = 7 #reassigning variables
print(x)
print(x + 3)
x = 123.456
print(x)
x = "This is a string"
print(x + "!")

#user input
    #-too lazy to keep inputting numbers
#x = input() 
#print(x)
#name = input("Enter your name: ")
#print("Hello, " + name) 

#age = int(input())  #str-->int
#print(age)  
#age = 42            #int-->str      
#print("His age is " + str(age)) 

#name = input()     #multiple inputs
#age = input()
#print(name + " is " + age)  

#in-place operators
x = 2
print(x)
x += 3
print(x)

x = "spam" #strings
print(x)
x += "eggs"
print(x)

#control flow
#booleans
my_boolean = True
print(my_boolean)

print(2 == 3)
print("hello" == "bye")

x = 7 #comparisons
print(x > 5)
print(x < 2)
print(x >= 7)
print(x <= 7)

#boolean operators
print(1 == 1 and 2 == 2) #and
print(1 == 1 and 2 == 3)
print(1 != 1 and 2 == 2)
print(2 < 1 and 3 >  6)

print(1 == 1 or 2 == 2) #or
print(1 == 1 or 2 == 3)
print(1 != 1 or 2 == 2)
print(2 < 1 or 3 >  6)

print(not 1 == 1) #or(inverts argument)
print(not 1 > 7)

#if statements-INDENTATION
x = 42
if x > 5:
    print("x is greater than 5") 

num = 12
if num > 5:
    print("Bigger than 5")
    if num <=47:
        print("Between 5 and 47")

#else statements
x = 4
if x == 5:
    print("Yes")
else:
    print("No")

num = 3
if num == 1:
    print("One")
else: 
    if num == 2:
        print("Two")
    else: 
        if num == 3: 
            print("Three")
        else: 
            print("Something else")

#elif statements (shortcut for if/else)
num = 3
if num == 1:
    print("One")
elif num == 2:
    print("Two")
elif num == 3: 
    print("Three")
else: 
    print("Something else")

#while loops
i = 1
while i <=5:
    print(i)
    i = i + 1
print("Finished!")

x = 1
while x < 10:
    if x%2 == 0:
        print(str(x) + " is even")
    else:
        print(str(x) + " is odd")

    x += 1 

#lists
words = ["Hello", "world", "!"] 
print(words[0]) #index starts at 0
print(words[1])
print(words[2])

#matrices
m= [
    [1,2,3],
    [4,5,6]
]
print (m[1][2]) #index starts at 0

str = "Hello world!"
print(str[6])  #space is also considered a symbol

nums = [1, 2, 3] #lists can be added and multiplied like strings
print(nums + [4, 5, 6])
print(nums * 3)

#list operations
print("spam" in words) #in operator checks if item is in list
print("egg" in words)
print("tomato" in words)

nums = [1, 2, 3] #not operator, checks if item is NOT in list
print(not 4 in nums)
print(4 not in nums)
print(not 3 in nums)
print(3 not in nums)

#for loops
words = ["hello", "world", "spam", "eggs"]
for word in words:
    print(word + "!")

str = "testing for loops"
count = 0

for x in str:
   if(x == 't'):
    count += 1

print(count)

#range
numbers = list(range(10))
print(numbers)

numbers = list(range(3, 8)) #NOTE 8 is not included
print(numbers)

numbers = list(range(5, 20, 2)) #Step- 3rd number is the interval
print(numbers)

for i in range(3): #can be used with for loops
    print("hello!")

#list slices
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[2:6]) #returns new list with old values between indices
print(squares[3:8])
print(squares[0:1])

print(squares[:7]) #taken as start of list
print(squares[7:]) #taken as end of list

print(squares[::2]) #includes alternate values of slice
print(squares[2:8:3])

print(squares[1:-1]) #counts from the end of the list
print(squares[::-1]) #reverses list

#len
nums = [1, 3, 5, 2, 4]
print(len(nums)) #len gets number of items in a list

blood_god = "technoblade" 
print(len(blood_god)) #len gets number of characters in a string

#list functions
#append() #adds items to existing list
nums = [1, 2, 3]
nums.append(4)
print(nums)

#split() #splits a string into a list
numbers = '1 2 3'
numbers.split()
print(numbers.split())

poggers = 'pog-pog-pog'
poggers.split('-')
print(poggers.split('-'))

#insert() #inserts a new item at any position in the list:
words = ["Python", "fun"]
index = 1
words.insert(index, "is")
print(words) 

#index() #finds the first occurrence of a list item and returns its index
letters = ['p', 'q', 'r', 's', 'p', 'u']
print(letters.index('r'))
print(letters.index('p'))
print(letters.index('s')) 

#max(list) # Returns the maximum value
letters = ['a', 'b', 'z', 'e', 'x', 'd']
print(max(letters))

numbers = [1, 4, 6, 82, 93, 7]
print(max(numbers))

#min(list) #Returns the minimum value
letters = ['a', 'b', 'z', 'e', 'x', 'd']
print(min(letters))

numbers = [1, 4, 6, 82, 93, 7]
print(min(numbers))

#list.count(item) #Returns a count of how many times an item occurs in a list
numbers = [1, 4, 6, 82, 93, 7, 6]
print(numbers.count(6))

letters = ['a', 'e', 'z', 'e', 'e', 'd']
print(letters.count('e'))

#list.remove(item) #Removes an item from a list.
numbers = [1, 4, 6, 82, 93, 7]
numbers.remove(6)
print(numbers)

letters = ['a', 'e', 'z', 'w', 'y', 'd']
letters.remove('e')
print(letters)

#list.reverse() #Reverses items in a list.
numbers = [1, 4, 6, 82, 93, 7]
numbers.reverse()
print(numbers)

letters = ['a', 'e', 'z', 'w', 'y', 'd']
letters.reverse()
print(letters)

#format() #string formatting, argument is placed based on {} 
nums = [4, 5, 6]
msg = "Numbers: {0} {1} {2}". format(nums[0], nums[1], nums[2])
print(msg)

a = "{x}, {y}".format(x=5, y=12) #can name placeholders instead of index nums
print(a)

#join() #joins a list of strings with another string as a separator
print(", ".join(["spam", "eggs", "ham"]))

#replace() #replaces one substring in a string with another
print("Hello ME".replace("ME", "world"))

#startswith() #determines if there is a substring at the start of a string
print("This is a sentence.".startswith("This"))

#endswith() #determines if there is a substring at the end of a string
print("This is a sentence.".endswith("sentence."))

#lower() #changes the string to lowercase
print("POGCHAMP".lower())

#upper() #changes the string to uppercase
print("This is a sentence.".upper())

#split) #turns a string with a certain separator into a list
print("spam, eggs, ham".split(", "))

#def statement #defines own function
def my_func():
    print("spam")
    print("spam")
    print("spam")

my_func()

def hello():
   print("Hello world!")
 
hello()
hello()
hello()

#arguments 
def print_with_exclamation(word):
   print(word + "!")
    
print_with_exclamation("spam")
print_with_exclamation("eggs")
print_with_exclamation("python")

def print_sum_twice(x, y):
   print(x + y)
   print(x + y)

print_sum_twice(5, 8)

#returning functions
def max(x, y):
    if x >=y:
        return x
    else:
        return y
        
print(max(4, 7))
z = max(8, 5)
print(z)

def add_numbers(x, y):
    total = x + y
    return total
    print("This won't be printed") #code placed after the return statement won’t be executed

print(add_numbers(4, 5))

#comments
#comments are made using an octothorpe(#)
#python doesn't have general multi-line comments
#If we do not assign strings to any variable, they can act as comments
'this is a comment'
"also a comment"
'''
multi-
line
comment
'''

#docstrings
def shout(word):
    """
    Print a word with an
    exclamation mark following it.
    """
    print(word + "!")

shout("spam")

def punt(name):
    """
    prints punt "person" with
    a person after
    """
    print("punt " + name)

punt("jack")
