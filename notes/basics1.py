# Fundamental Data Types
# int
# float
# bool
# str
# list
# tuple
# set
# dict

# Classes -> custom data types

# Specialized data types (from modules)

# None(absence of value)

# print(), type()

# && -> raised to(exponential)
# // -> quotient
# %  -> remainder

# math functions
# round() -> rounds off value
# abs() -> returns only +ve
# complex() -> for complex maths
# bin() -> gives binary numbers
# print(int('0b101',2)) binary to integer conversion

# variable
# snake_case
# case sensitive
# _var -> underscore represents a private variable

# constants
# PI = 3.14 -> constant

# __name -> dunder variables must not be used


# strings
# ' '
# " "
# ''' long_strings ''' -> for defining long multi-line strings

# formatted strings
# name = 'jash'
# age = '20'
# print(f'hi {name}. You are {age} years old')
# .format method

# string indexes -> 01234....
# string[start:stop:stepover] - string slicing

# strings are immutable -> can't reassign a part of string, completely new string must be created

# functions vs methods
# string methods
# string.upper() -> all strings become capitals (same for lower)
# string.capitalize() -> first letter becomes capital
# string.find('hi') -> finds occurence of the string
# string.replace('hi','me') -> replaces text
# string = 'helloooo'
# print(string[::-1]) -reverse string

# booleans
# bool(1) -> true
# bool(0) -> false

# excercise
# from datetime import date
# todays_date = date.today()
# birth_year = int(input('what year were you born ?\n'))
# current_year = todays_date.year
# age = int(current_year) - birth_year
# print(f'Your age is {age}')

# excercise
# username = input('Username: ')
# password = input('Password: ')
# pass_length = len(password)
# hidden_pass = len(password) * '*'
# print(hidden_pass)
# print(f'{username}, your password {hidden_pass}  is {pass_length} letters long')

# excercise
# username = input("Enter Username: ")
# password = input("Enter Password: ")

# print(f"Hi {username}, your password {(len(password)* '*')} is {len(password)} letters long")

# list - 1st data structure
# li = [1,2,3,4,5]
# li2 = ['a', 'b', 'c']
# li3 = [1,2,'a', True]


# List slicing -new list is created when sliced, original list is not changed
# unlike strings, lists are mutable

# amazon_cart = [
#   'notebooks',
#   'sunglasses',
#   'toys',
#   'grapes'
# ]

# amazon_cart[0] = 'laptop'
# print(amazon_cart)

# new_cart = amazon_cart[:] copying a list

# Matrix

# matrix = [
#   [1, 5, 1],
#   [0, 1, 0],
#   [1, 0, 1]
# ]

# print(matrix[0][1])

# in python everything is an object

# list methods

# basket = [1, 2, 3, 4, 5]

# print(len(basket))
# new_list = basket.append(100)
# print(new_list) - none empty list, append changes the list in place, doesn't create a new value
# print(basket)

# basket.insert(4,100)
# print(basket)

# basket.extend([100,200])
# print(basket)

# basket.pop() removes last value using given index, returns the pop value
# basket.pop(0)

# basket.remove(4) removes value 4

# basket.clear() clears the list, gives empty list
# print(basket)

# basket = ['a', 'b', 'c', 'd', 'e']
# print(basket.index('d', 0, 4)) finds the idex of the given value/string

# print('d' in basket) -can be used in strings as well

# print(basket.count('d'))
# basket.sort()
# sorted(basket)
# basket.copy -returns new list does not affect the original list
# basket.reverse()
# basket[::-1] -returns a new reversed list
# basket[:] -returns copy of a list
# print(list(range(0, 100)))

# sentence = ''
# new_sentence = ''.join(['hi', 'my', 'name', 'is', 'JOJO'])
# print(new_sentence)

# list unpacking
# a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# print(a)
# print(b)
# print(c)
# print(*other)
# print(d)

# Dictionary data type, data structure
# unordered key value pair

# dictionary = {
#     'a': 1,
#     'b': 2,
#     'x': 3
# }

# keys in a dictionary has to be immutable
# if same key is reapeated then the latest value is obtained, key overwrite each other

# user = {
#     'basket': [1, 2, 3],
#     'greet': 'hello',
#     'age': 20
# }

# print(user.get('age', 55)) -used to check if the value is present, also has a default value attribute

# print('basket' in user)

# user2 = dict(name = 'JohnJohn') -just another way to create a dictionary

# print('age' in user.keys()) -check if that key is there
# print('hello' in user.values()) -check if that value is there
# print(user.items()) -give all key-value pair in the form of a tuple
# user.clear()
# user2 = user.copy
# user.pop('age') -removes a value using a key
# user.popitem() -removes last value and key
# user.update({'age': 45}) -change an existing value or add a new value with a key
# print(user)

# Tuple - immutable list
# my_tuple = (1, 2, 3, 4, 5)
# when list is not going to be changed then use tuple
# tuple is a valid key for dictionary

# print(my_tuple.count(5))
# print(my_tuple.index(5))
# print(len(my_tuple))


# Sets
# unordered collection of unique objects, no duplicates in a set

# my_set = {1, 2, 3, 4, 5}
# my_set.add(100)
# print(my_set)

# my_list = [1, 2, 3, 4, 5, 5]
# # print(set(my_list)) -duplicates removed by converting list into set
# print(1 in my_set)
# print(len(my_set))
# print(list(my_set))
# my_set.clear
# new_set = my_set.copy
# print(new_set)

# your_set = {4, 5, 6, 7, 8, 9, 10}

# print(my_set.difference(your_set))
# my_set.discard(5)
# print(my_set.difference_update(your_set)) -removes all elements of other set from this set

# .intersection(), & can also be used for intersection
# .isdisjoint() -returns true if there is no common values between them
# .union, | can also be used for union
