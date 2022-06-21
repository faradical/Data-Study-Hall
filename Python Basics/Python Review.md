
# PYTHON REVIEW
### Table of Contents
1. [DataTypes](#1)
    * [Strings](#1.1)
    * [Integers](#1.2)
    * [Floats](#1.3)
    * [Python Arithmetic Operations:](#1.4)
    * [Booleans](#1.5)
    * [Lists](#1.6)
    * [Sets](#1.7)
    * [Tuples](#1.8)
    * [Dictionaries](#1.9)
2. [Type Casting](#2)
3. [String Formatting](#3)
4. [If/Elif/Else](#4)
5. [For Loops](#5)
6. [While Loops](#6)
7. [Using Functions](#7)
8. [Creating New Functions](#8)
9. [Reading Files](#9)
10. [Importing Modules](#10)

<a id="1"></a>
## DataTypes
There are a number of built-in classes, or datatypes, to python that you will want to familiarize yourself with.

<a id="1.1"></a>
###  - Strings
Strings in programming are literally a string of characters. They allow us to introduce words and sentences into our program.


INPUT: 
```python
# In Python, strings can be defined using double quotes...
var1 = "Hello"
# Or single quotes. You just need to be consistent.
var2 = 'World'
```


INPUT: 
```python
# We can print strings using the print() function.
print(var1)
print(var2)
```
OUTPUT: 

    Hello
    World
    


INPUT: 
```python
# We con also concatenate strings together using the + operator.
var3 = var1 + " " + var2
print(var3)
```
OUTPUT: 

    Hello World
    

<a id="1.2"></a>
### - Integers
Ints, or integers, are all real whole numbers.


INPUT: 
```python
#Create an integer
num1 = 7
print(num1)
```
OUTPUT: 

    7
    


INPUT: 
```python
# BONUS: You can use the type() function to check the datatype of a variable
print(type(num1))
```
OUTPUT: 

    <class 'int'>
    

<a id="1.3"></a>
### - Floats
Floats are another numerical datatype used to hold decimals.


INPUT: 
```python
# Floats are defined the same way as regular integers, except that they feature decimals
num2 = 15.5
print(num2)
print(type(num2))
```
OUTPUT: 

    15.5
    <class 'float'>
    


INPUT: 
```python
# It is possible to perform arithmetic operations on both number types.
num3 = num1 + num2
print(num3)

# If you combine a float class with an int class, the result will be the class with the higher precision: float.
print(type(num3))
```
OUTPUT: 

    22.5
    <class 'float'>
    

<a id="1.4"></a>
### Python Arithmetic Operations:
![Python Arithmetic](https://d1e4pidl3fu268.cloudfront.net/f20083ef-a2fb-4673-ac88-13d58ba68133/Arithmeticoperators.png)

<a id="1.5"></a>
### - Booleans
Booleans are a variable class that have a binary of True or False values


INPUT: 
```python
status1 = True
status2 = False
print(status1)
```
OUTPUT: 

    True
    

<a id="1.6"></a>
### - Lists
Lists are the work-horse for iterable data in python. They are an object that, as the name suggests, contain multiple other objects in list.


INPUT: 
```python
# We can define a list using the square brackets with each item in the list being seperated by a comma.
my_list = ["a", "b", 3.14, 5, True]
# You will notice that the items in a list do not have to all have the same class.
print(my_list)
```
OUTPUT: 

    ['a', 'b', 3.14, 5, True]
    


INPUT: 
```python
# We can access items in a list using indexing.
# Simply write the name of the list, then specify the index position in square brackets.
# Do not forget that the index starts at 0!
# i.e., the first item in the list is position 0, and the fourth item in the list is position 3.
print(my_list[3])
```
OUTPUT: 

    5
    


INPUT: 
```python
# It is possible to perform more complex tasks with indexing as well!
print(my_list[:3]) # Print the range from the beginning of the list to index position 2 (The last value, 3, is non-inclusive!)
print(my_list[3:]) # Print the range from index position 3 to the end of the list
print(my_list[-1]) # Print the last item in the list
new_list = my_list[:3] +  my_list[4:] # Create a new list without index position 3
print(new_list)
```
OUTPUT: 

    ['a', 'b', 3.14]
    [5, True]
    True
    ['a', 'b', 3.14, True]
    


INPUT: 
```python
# It is possible to add items to a list using the append() method:
my_list.append("hello")
print(my_list)
```
OUTPUT: 

    ['a', 'b', 3.14, 5, True, 'hello']
    


INPUT: 
```python
# It is possible to 
my_list.remove(5)
print(my_list)
```
OUTPUT: 

    ['a', 'b', 3.14, True, 'hello']
    

An important note on variables in a list:


INPUT: 
```python
# Note that we can make a list out of variables we have defined.
my_new_list = [var1, num1, num2]
print(my_new_list)
```
OUTPUT: 

    ['Hello', 7, 15.5]
    


INPUT: 
```python
# However, if we update one of those variables, that does not effect the value in the list
var1 = "Now time for something completely different!"
print(my_new_list)
```
OUTPUT: 

    ['Hello', 7, 15.5]
    


INPUT: 
```python
# This is because the list only gains it's intial value from the variable. In order to update the list item, we need to use indexing!
my_new_list[0] = "Now time for something completely different!"
print(my_new_list)
```
OUTPUT: 

    ['Now time for something completely different!', 7, 15.5]
    

<a id="1.7"></a>
### - Sets
Sets in Python are modeled after mathematical sets and often used in similiar operations. Unlike lists, sets are unordered and have no index to access specific items. Items in a set must also all be unique, making them a quick way to get rid of duplicate data. While items in a set can be added or removed, they are immutable, meaning they cannot be changed.


INPUT: 
```python
# Sets can be created similiarly to a list, but using curly brackets instead of square brackets.
my_set = {"a","b","c",1,2,3}
print(my_set)
```
OUTPUT: 

    {1, 'b', 2, 3, 'a', 'c'}
    


INPUT: 
```python
# Add a value to the set using add().
my_set.add("new value")
print(my_set)
```
OUTPUT: 

    {1, 'b', 2, 3, 'a', 'c', 'new value'}
    


INPUT: 
```python
# Remove a value from the set using discard().
my_set.discard("new value")
print(my_set)
```
OUTPUT: 

    {1, 'b', 2, 3, 'a', 'c'}
    

<a id="1.8"></a>
### - Tuples
Tuples are another collection data structure that uses indexing to access the data within, but unlike lists, tuples are completely imutable and connot be changed at all.


INPUT: 
```python
# Tuples can be created using the parentheses.
my_tuple = ("a", "b", 3.14, 5, True)
print(my_tuple)
print(my_tuple[2])
```
OUTPUT: 

    ('a', 'b', 3.14, 5, True)
    3.14
    

<a id="1.9"></a>
### - Dictionaries
Next to lists, dictionaries are one of the most powerful collection structures in Python! As opposed to to an index, however, dictionary data is accessed using key:value pairs. Dictionaries are easily changeable and do not allow duplicate keys.


INPUT: 
```python
# Create a dictionary using the curly brackets in combination with key:value pairs seperated by commas.
my_big_dict = {"key 1": 3, "key 2": "value 2", "Pi": 3.1415}
print(my_big_dict)
```
OUTPUT: 

    {'key 1': 3, 'key 2': 'value 2', 'Pi': 3.1415}
    


INPUT: 
```python
# Access data in a dictionary by putting the key you want in square brackets
print(my_big_dict["key 2"])
```
OUTPUT: 

    value 2
    


INPUT: 
```python
# Adding a key:value pair to a dictionary as specifing the new key in square brackets and setting it equal to the intended value.
my_big_dict['golden ration'] = 1.618
print(my_big_dict)
```
OUTPUT: 

    {'key 1': 3, 'key 2': 'value 2', 'Pi': 3.1415, 'golden ration': 1.618}
    


INPUT: 
```python
# You can edit the value of one of the value pairs in much the same way
my_big_dict['key 2'] = 7
print(my_big_dict)
```
OUTPUT: 

    {'key 1': 3, 'key 2': 7, 'Pi': 3.1415, 'golden ration': 1.618}
    


INPUT: 
```python
# You can also remove keys by using the pop() method...
my_big_dict.pop("key 1")
print(my_big_dict)
```
OUTPUT: 

    {'key 2': 7, 'Pi': 3.1415, 'golden ration': 1.618}
    


INPUT: 
```python
# Or delete key using the del operation and specifing the key
del my_big_dict["key 2"]
print(my_big_dict)
```
OUTPUT: 

    {'Pi': 3.1415, 'golden ration': 1.618}
    

<a id="2"></a>
## Type Casting
Have a variable that is currently one type of data class, but want it to be another? No problem, casting is here to help!


INPUT: 
```python
# You can usually cast a data class to any other similiar class by calling the "class constructor".
# Here, we will use the float class constructor to cast an integer as a float:
my_int = 6
print(f"My integer is: {my_int}")
print(f"It's class is:")
print(type(my_int))

print() # Additional print function to make our output prettier

my_float = float(my_int) # Here is where we use the class constructor to cast my_int as a float!
print(f"My float is: {my_float}")
print(f"It's class is:")
print(type(my_float))
```
OUTPUT: 

    My integer is: 6
    It's class is:
    <class 'int'>
    
    My float is: 6.0
    It's class is:
    <class 'float'>
    

Casting can be used to solve a number of problems you might encounter!


INPUT: 
```python
# Have a string you need to convert to a number?
num_string = "13"
num = int(num_string)
print(num)
print(type(num))
```
OUTPUT: 

    13
    <class 'int'>
    


INPUT: 
```python
# How about converting a number back to a string to be concatentated?
print("Friday the " + str(num))
```
OUTPUT: 

    Friday the 13
    


INPUT: 
```python
# Run into tuple you need to be able to manipulate? Lists can do the job!
print(my_tuple) # This tuple cannot be changed.
list_from_tuple = list(my_tuple) # But this list can!
list_from_tuple[1] = "red"
print(list_from_tuple)
```
OUTPUT: 

    ('a', 'b', 3.14, 5, True)
    ['a', 'red', 3.14, 5, True]
    


INPUT: 
```python
# How about if you need the set of unique items in a list?
big_list = ["a","a","a","b","b","b","b","b","b","c","c","c","c","d","d"]
# Well that sounds like a job for a set!
unique = list(set(big_list))
print(unique)
```
OUTPUT: 

    ['c', 'b', 'd', 'a']
    

<a id="3"></a>
## String Formatting
Casting is one effective way to concatenate non-string data to a string, but there are to other hghly effective ways that come with additional formatting benefits.


INPUT: 
```python
# The format method, which replaces the {} in a string with the variable specified.
print("The number Pi is roughly {}".format(my_big_dict["Pi"]))
# This method allows us to use special formatting, such as below used to round the digits of Pi.
print("The number Pi is roughly {:.2f}".format(my_big_dict["Pi"])) # Note the format specifier in the {}
```
OUTPUT: 

    The number Pi is roughly 3.1415
    The number Pi is roughly 3.14
    


INPUT: 
```python
# The f-string is also a grat way to quickly format strings. Note the "f" at the beginning of the string!
print(f"The number Pi is roughly {my_big_dict['Pi']}") # Notice that the quotes around 'Pi' are now single quotes since the f-string was started with double quotes!
# We can use the same format specifier with in the f-string.
print(f"The number Pi is roughly {my_big_dict['Pi']:.2f}")
```
OUTPUT: 

    The number Pi is roughly 3.1415
    The number Pi is roughly 3.14
    

<a id="4"></a>
## If/Elif/Else
If/Then statements allow us to create different paths in our program depending on the conditions it encounters.


INPUT: 
```python
# If/then statements in Python are bult off conditionals, statements that have two pieces of data and a comparison operater between them describing relationship to look for.
a = 2 # A variable assignment.
a == 2 # A conditional. Note that the comparison operator is a double equals sign to distinguish it from the assignment operator
```




    True




INPUT: 
```python
# If the conditional returns True, the if statement will execute:
if a == 2:
    print("Variable 'a' is indeed 2.")
```
OUTPUT: 

    Variable 'a' is indeed 2.
    


INPUT: 
```python
response = input("Please select y or n: ")

if response == "y":
    print("You chose y! Great choice!")
elif response == "n":
    print("You choose n. Bad move.")
else:
    print("You were supposed to choose y or n!")
```


INPUT: 
```python
# You can make additional conditions in a single line by using the "and" as well as "or" operators to seperate the conditionals.
if a==2 and response=="y": # Both conditions must be true
    print("A is 2 AND you chose Y.")
    
if a==2 or response=="y": # Only one condition needs to be true
    print("Either A is 2 OR you chose Y.")
```

Comparison Operators List\
![Comparison Operators](https://iconicdevelopers.com/wp-content/uploads/2019/01/Overview-of-Comparison-Operators-in-Python-1024x603.png)

<a id="5"></a>
## For Loops
For Loops allow us to perform a set number of iterations of a block of code. They are one of the first keys you learn to automating repetitive tasks!


INPUT: 
```python
# Iterate over a sequence of numbers using the range function
for n in range(5):
    print(n)
```


INPUT: 
```python
# Iterate over items in a list
for i in my_list:
    print(i)
```


INPUT: 
```python
# Iterate over the keys in dictionary
for i in my_big_dict:
    print(i)
```


INPUT: 
```python
# You can also feed those keys back into the diction to iterate over the values!
for i in my_big_dict:
    print(my_big_dict[i])
```

<a id="6"></a>
## While Loops
Unlike For Loops, which perform a set numer of iterations, while loops are intended to loop until a certain condition is met.


INPUT: 
```python
response = input("Please select y or n: ") # initializing the response variable for the while loop to use.

while response != "n":
    response = input("Please select y or n: ")

    if response == "y":
        print("You chose y! Great choice!")
    elif response == "n":
        print("You choose n. Bad move.")
    else:
        print("You were supposed to choose y or n!")
```

<a id="7"></a>
## Using Functions
Functions are versatile blocks of pre-written code that take arguments as input, perform some program, then return some data to the user.

Functions we have already used in this review so far include:
* [print()](https://docs.python.org/3/library/functions.html#print)
* [type()](https://docs.python.org/3/library/functions.html#type)
* [input()](https://docs.python.org/3/library/functions.html#input)
* [len()](https://docs.python.org/3/library/functions.html#len)
* [range()](https://docs.python.org/3/library/functions.html#func-range)

Other functions you will want to familiarize yourself with include:
* [isinstance()](https://docs.python.org/3/library/functions.html#isinstance)
* [sum()](https://docs.python.org/3/library/functions.html#sum)
* [zip()](https://docs.python.org/3/library/functions.html#zip)
* [enumerate()](https://docs.python.org/3/library/functions.html#enumerate)
* [round()](https://docs.python.org/3/library/functions.html#round)
* [open()](https://docs.python.org/3/library/functions.html#open)


INPUT: 
```python
import pandas as pd
df = pd.DataFrame({"a": [1,2,3],
                  "b": ['John',"Saiana","Bob"]})
type(df)
```




    pandas.core.frame.DataFrame




INPUT: 
```python
type(df["b"])
```




    pandas.core.series.Series



<a id="8"></a>
## Creating New Functions
We are not limited to only those functions that are native in Python, but can write our own!


INPUT: 
```python
# Functions are defined using the "def" prefix followed by any arguments in parentheses
def my_func(argument1, argument2):
    return argument1 + argument2

print(my_func(5, 7))
print(my_func("cat", "dog")) # When writing functions, it is important to keep in mind how it will handle datatypes.
```


INPUT: 
```python
import math
def get_hypotenuse(a, b):
    c = math.sqrt(a**2 + b**2)
    return c

(print(get_hypotenuse(5, 7)))
```


INPUT: 
```python
# You can even call functions inside of functions to create more powerful code.
def perimeter(a, b):
    c = get_hypotenuse(a, b)
    result = my_func(a, b) + c
    return result

print(perimeter(5, 7))
```


INPUT: 
```python
def my_routine():
    return 2 + 2
    
var = my_routine() * 8
```




    32



<a id="9"></a>
## Reading Files


INPUT: 
```python
path = "Resources/my_file.txt"
file = open(path, "r") # Here we are opening the file in red mode, as denoted by the "r".
print(file.read())
```


INPUT: 
```python
# We can open files as a variable and write to them.
file = open(path, "a+") # Here we are opening the file in append mode, as denoted by the "a+".
file.write("\nA new line")
file.close()
```


INPUT: 
```python
#Or open files using the "with/as" statement.
#A bonus of this method is it does not require a file.close(), but everything we do with the file must be under the "with/as".
with open(path, "a+") as file:
    file.write("\nAnother new line")

file = open(path, "r")
print(file.read())
```

<a id="10"></a>
## Importing Modules
Modules are collections of pre-written Python code, including variables, classes, and functions which are not included in regular Python. However, we can import these modules for use in our own code.


INPUT: 
```python
import random as rn
print(rn.choice(my_list))
```


INPUT: 
```python
import pandas as pd
pd.DataFrame({"Column A":[1,2,3],"Column B":[4,5,6],"Column C":[2,5,3]})
```

## Thanks for Reading!
    -Seth Pruitt
