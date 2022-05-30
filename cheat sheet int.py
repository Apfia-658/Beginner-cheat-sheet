#dictionaries
ages = {
    "Dave": 24,
    "Mary": 42, 
    "John": 58
} #each element is a key:value pair
print(ages["Dave"])
print(ages["Mary"]) #only immutable objects can be used as keys to dictionaries(no lists)

nums = {
    1: "one",
    2: "two",
    3: "three",
}
print(1 in nums) #use in and not in to determine whether a key is in a dictionary
print("three" in nums)
print(4 not in nums)

#get() #same thing as indexing, but if key is not found, returns specified value
pairs = {1: "apple",
  "orange": [2, 3, 4], 
  True: False, 
  12: "True",
}

print(pairs.get("orange"))
print(pairs.get(7, 42))
print(pairs.get(12345, "not found"))

#tuples #like lists, but immutable, made using parentheses
words = ("spam", "eggs", "sausages")
print(words[0])

my_tuple = "one", "two", "three" #parentheses not required
print(my_tuple[0])

#unpacking tuples
numbers = (1, 2, 3)
a, b, c = numbers #assigns each item to a variable
print(a)
print(b)
print(c)

x,y = (1,2) #can be used to switch variables
x,y = y,x
print(y)

a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c) #asterisk- takes all values that are left over
print(d)

#sets #like lists, but unordered (can't be indexed), made using {}
num_set = {1, 2, 3, 4, 5} #storage method= faster to check if an item is part of a set than a list
print(3 in num_set)

nums = {1, 2, 1, 3, 1, 4, 5, 6}
print(nums) #sets cannot contain duplicate elements, auto-removed
nums.add(-7) #add function adds item
nums.remove(3) #remove function removes item
print(nums)

first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}
print(first | second) #union operator combines two sets to form a new one containing items in either
print(first & second) #intersection operator gets items only in both
print(first - second) #difference operator gets items in the first set but not in the second
print(second - first)
print(first ^ second) #symmetric difference operator gets items in either set, but not both

#list comprehension #way to create lists whose contents obey a rule
cubes = [i**3 for i in range(5)]
print(cubes)

evens=[i**2 for i in range(10) if i**2 % 2 == 0] #can contain if statement to enforce a condition
print(evens) 

#DATA STRUCTURES
print('dictionary')
'''
When to use a dictionary:
- When you need a logical association between a key:value pair.
- When you need fast lookup for your data, based on a custom key.
- When your data is being constantly modified. Remember, dictionaries are mutable.
'''

print('list')
'''
- Use lists if you have a collection of data that does not need random access. 
  Try to choose lists when you need a simple, iterable collection that is modified frequently.
'''

print('set')
'- Use a set if you need uniqueness for the elements.'

print('tuple')
'- Use tuples when your data cannot/should not change.'

#higher order functions
def apply_twice(func, arg): #take other functions as arguments or return them as results
    return func(func(arg))

def add_five(x):
    return x + 5

print(apply_twice(add_five, 10))

def test(func, arg):
  return func(func(arg))

def mult(x):
  return x * x

print(test(mult, 2))

