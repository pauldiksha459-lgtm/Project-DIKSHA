#DAY1 (DONE ON PYTHON 3.13 APP)
# Python 3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> print("hello")
# hello
# >>> print("hello world")
# hello world
# >>> if 5>2:
# ...     print("five is greter than two")
# ...
# five is greter than two
# >>> x=5
# >>> y"hello"
#   File "<python-input-4>", line 1
#     y"hello"
#      ^^^^^^^
# SyntaxError: invalid syntax
# >>> x=5
# >>> y=3
# >>> print(x+y)
# 8
# >>>
# >>> x=5
# >>> y=3
# >>> print(x-y)
# 2
# >>> x=5
# >>> y=3
# >>> print(x*y)
# 15
# >>> x=5
# >>> y=3
# >>> print(x/y)
# 1.6666666666666667
# >>> print("this is python")
# this is python
# >>> print('hello')
# hello
# >>> x=7
# >>> y="diksha"
# >>> print(x),print(y)
# 7
# diksha
# (None, None)
# >>> x=7
# >>> y="diksha"
# >>> print(type(x))
# <class 'int'>
# >>> print(type(Y))
# Traceback (most recent call last):
#   File "<python-input-26>", line 1, in <module>
#     print(type(Y))
#                ^
# NameError: name 'Y' is not defined. Did you mean: 'y'?
# >>> print(type(y))
# <class 'str'>
# >>> x=4,5
# >>> print(type(x))
# <class 'tuple'>
# >>> x=5
# >>> y=4
# >>> print(bool(x+y))
# True
# >>> print(bool(x))
# True
# >>> x=""
# >>> print(bool(x))
# False
# >>> x="diksha"
# >>> print(bool(x))
# True
# >>>
# >>>
# >>> my_var=40
# >>> print(my_var)
# 40
# >>> x,y,z="30","40","50"
# >>> print(x)
# 30
# >>> print(y)
# 40
# >>> print(z)
# 50
# >>> x="30","40","50"
# >>> print(x)
# ('30', '40', '50')
# >>> x=y=z="apple"
# >>> print(x)
# apple
# >>>
# >>>
# >>> fruits=["apple","bannana","cherry"]
# >>> x,y,z=fruits
# >>> print(x)
# apple
# >>> print(y)
# bannana
# >>> print(z)
# cherry
# >>>
# >>> fruits=["apple","banana","cherry"]
# >>> x,y,z=fruits
# >>> x=y=z=fruits
# >>> print(x)
# ['apple', 'banana', 'cherry']
# >>> print(type(fruits))
# <class 'list'>
# >>>
# >>> fruits=[2,4,7,8,34,50]
# >>> print(fruits)
# [2, 4, 7, 8, 34, 50]
# >>> print(type(fruits))
# <class 'list'>
# >>>
# >>>
# >>>
# >>> x="this is python"
# >>> print(x)
# this is python
# >>>
# >>> x="python"
# >>> y+"is"
# Traceback (most recent call last):
#   File "<python-input-74>", line 1, in <module>
#     y+"is"
#     ~^~~~~
# TypeError: can only concatenate list (not "str") to list
# >>>
# >>> x="python"
# >>> y="is"
# >>> z"good"
#   File "<python-input-78>", line 1
#     z"good"
#      ^^^^^^
# SyntaxError: invalid syntax
# >>>
# >>>
# >>>
# >>> x="python"
# >>> y="is"
# >>> z="good"
# >>> print(x,y,z)
# python is good
# >>> print(x+y+z)
# pythonisgood
# >>>
# >>>
# >>>
# >>>
# >>>
# >>>
# >>> x="good"
# >>> def my_function():
# ...     #function opening
# ...
# ... print("python is"+x)
# ... #action
# ...     my_function()
# ...     #fuction closing
# ...
#   File "<python-input-94>", line 4
#     print("python is"+x)
#     ^^^^^
# IndentationError: expected an indented block after function definition on line 1
# >>>
# ...
# ... def my_function():
# ...     #function opening
# ...
# ...     print("python is"+x)
# ... #action
# ...     my_function()
# ...     #fuction closing
# ...
# >>>
# >>>
# >>>
# >>>
# >>>
# >>> x="good"
# >>>
# >>> def my_function():
# ...     print("python is "+x)
# ... my_function()
# ...
# python is good
# >>>
# >>>
# >>> def my_function():
# ...     global x
# ...     x="good"
# ... my_function()
# ...     print("python is "+)
# ...
#   File "<python-input-106>", line 5
#     print("python is "+)
# IndentationError: unexpected indent
# >>>
# >>>
# >>> def my_function():
# ...     global x
# ...     x="good"
# ...     my_function()
# ...     print("python is "+x)
# ...
# >>>
# >>>
# >>>
# >>>
# >>> def my_function():
# ... ...     global x
# ... ...     x="good"
# ... my_function()
# ... print("python is "+)
# ...
#   File "<python-input-114>", line 2
#     ...     global x
#     ^^^
# IndentationError: expected an indented block after function definition on line 1
# >>>
# >>>
# >>>
# >>>
# >>>
# >>>
# >>>
# >>> def my_function():
# ...     global x
# ... ...     x="good"
# ... my_function()
# ... print("python is "+x)
# ...
#   File "<python-input-122>", line 3
#     ...     x="good"
#             ^
# SyntaxError: invalid syntax
# >>>
# >>>
# >>>
# >>> def my_function():
# ...     global x
# ...     x="good"
# ... my_function()
# ... print("python is "+x)
# ...
# python is good
# >>>
# >>>
# >>>
# >>> x="good"
# >>>
# >>> def my_function():
# ...     print("python is "+)
# ... my_function()
# ...
#   File "<python-input-132>", line 2
#     print("python is "+)
#                        ^
# SyntaxError: invalid syntax
# >>>
# >>>
# >>>
# >>>
# >>>  x="good"
# ... >>>
# ... >>> def my_function():
# ... ...     print("python is "+x)
# ... ... my_function()
# ...
#   File "<python-input-137>", line 1
#     x="good"
# IndentationError: unexpected indent
# >>>
# >>>  x="good"
# ...
# ...  def my_function():
# ... print("python is "+x)
# ... my_function()
# ...
#   File "<python-input-139>", line 1
#     x="good"
# IndentationError: unexpected indent
# >>>
# >>>
# >>>
# >>>
# >>>
# >>>
# >>>
# >>> #DATA TYPES
# >>>
# >>>
# >>> x=5
# >>> print(type(x))
# <class 'int'>
# >>> x="name"
# >>> print(type(x))
# <class 'str'>
# >>> x=5.6
# >>> print(typt(x))
# Traceback (most recent call last):
#   File "<python-input-155>", line 1, in <module>
#     print(typt(x))
#           ^^^^
# NameError: name 'typt' is not defined. Did you mean: 'type'?
# >>> print(type(x))
# <class 'float'>
# >>> x="good"
# >>> print(range(x))
# Traceback (most recent call last):
#   File "<python-input-158>", line 1, in <module>
#     print(range(x))
#           ~~~~~^^^
# TypeError: 'str' object cannot be interpreted as an integer
# >>>
# >>>
# >>> x=1j
# >>> print(type(x))
# <class 'complex'>
# >>> x={"apple","banana"}
# >>> print(type(x))
# <class 'set'>
# >>>
# >>>
# >>>
# >>> x=10
# >>> y=20
# >>>
# >>> print(x+y)
# 30
# >>> print(x-y)
# -10
# >>> print(x*y)
# 200
# >>> print(x/y)
# 0.5
# >>> print(x%y)
# 10
# >>> print(x**y)
# 100000000000000000000
# >>> print(x//y)
# 0
# >>>
# >>>
# >>> #LIST
# >>> my_list=["apple","bannana"]
# >>> print(type(my_list))
# <class 'list'>
# >>> print(my_list)
# ['apple', 'bannana']
# my_list[-5:-1])
# ['banana', 'cherry', 'sjc', 'bkdeshdr']
# >>> print(my_list[-4:])
# ['cherry', 'sjc', 'bkdeshdr', 'guygkuy']
# >>>
# >>>
# >>>>>>
# >>>
# >>> print(len(my_list))
# 2
# >>>
# >>> my_list=["apple","banana",1,3,True]
# >>>
# >>>
# >>> my_list=["apple","banana","cherry"]
# >>> print(my_list[1])
# banana
# >>> print(my_list[-1])
# cherry
# >>>
# >>> my_list=["apple","banana","cherry","sjc","bkdeshdr","guygkuy"]
# >>> print(my_list[2:5])
# ['cherry', 'sjc', 'bkdeshdr']
# >>>
# >>>> print(my_list[:-1])
# ['apple', 'banana', 'cherry', 'sjc', 'bkdeshdr']
# >>> print(my_list[-6])
# apple
# >>> print(my_list[-1:-5])
# []
# >>> print(
# >>> my_list=["apple","banana","sjc","bbhjg","vjkyftk"]
# >>> my_list[1]="mango"
# >>> print(my_list)
# ['apple', 'mango', 'sjc', 'bbhjg', 'vjkyftk']
# >>> print(my_list[-1])
# guygkuy
# >>> print(my_list[-1:])
# ['guygkuy']

#DAY2

print("hello world")
my_list=["apple","banana",1,3,7]
my_list[2]="abc"
print(my_list)

my_list=["apple","banana",1,3,7]
my_list[2:5]="abc"
print(my_list)

my_list=[1,2,4,5,6]
my_list.insert(2,3)
my_list.append("diksha")
print(my_list)

list1=[1,2,3]
list2=[4,5,6]
list1.extend(list2)
print(list1)
#remove
list1=[1,2,3,"apple",4,5,6]
# list1.remove("apple")
list1.pop(3)
print(list1)

#TASK:1

list1=[1,2,3,4,5,6]
list1.insert(2,"apple")
print(list1)
list1.append("banana")
print(list1)
list1.remove("apple")
print(list1)
list1.pop()
print(list1)
list1.clear()
print(list1)

list1=[]
list1.append(1)
print(list1)
list1[0]="hello"
print(list1)
#loopslists
list1=[1,2,3,4,5,6]
for x in list1:
    print(x)
    list1=[1,2,3,4,4,4,5,6]
for x in list1:
    print(x)
#SORT
list=[2,5,1,4,8]
list.sort()
print(list)

list=[2,5,1,4,8]
list.sort(reverse=True)
print(list)

text="diksha"
print(text.upper())
print(text.lower())
print(text.strip())
print(text.replace("diksha","python"))
print(text.split())

age=18
name="diksha"
print(f"my name is {name} and i am {age} years old")

x=5
x+=3
print(x)
x=5
x-=3
print(x)
x=5
x/=3
print(x)
x=5
x*=3
print(x)

x=10
y=7
print(x>y)
print(x==y)
print(x!=y)
print(x<y)
print(x>=y)
print(x<=y)

print("identity operators")
x=[1,2,3]
y=x
z=[1,2,3]
print(x is y)
print(x is z)

#python sets
colors={"red","green","blue"}
print(colors)
colors.add("yellow")
print(colors)
colors.remove("green")
print(colors)
for color in colors:
    print(color)

#DICTIONARY
student={"name":"diksha","course":"b.tech","branch":"AIML","section":"b"}
print(student)
print(student["name"])
student["course"]
student["branch"]
student["section"]
print(student)
student.pop("section")
del student ["branch"]
print(student)
for key,value in student.items():
    print(key,value)

#IF...ELSE IN PYTHON 
   #1.the if statement
age=20
if age>=18:
   print("you are eligible to vote")
else:
    print("you are not eligible to vote")

age=11
if age>=18:
   print("you are eligible to vote")
else:
    print("you are not eligible to vote")



#DAY 3

#if..elif..else statement
marks=85
if marks>=90:
   print("grade:A+")
elif marks>=75:
    print("grade:A")
elif marks>=60:
    print("grade:B")
else:
    print("grade:C")

#NESTED IF
x=15
if x>10:
    print("x is greater than 10")
if x>20:
    print("x is also greater than 20")
else:
    print("x is not greater than 20")

# TASK

x=20
if x%2==0:
    print("x number is even")
else:
    print("x number is odd")

#python for loops
#    1.iterating over a list
fruits=["aaple","banana","cherry"]
for fruit in fruits:
    print(fruit)
# 2.iterating over a string
word="python"
for letter in word:
    print(letter)
# 3.using range in for loops
for i in range(5):
    print(i)
# 4.you can also rage (start,stop,step)
for i in range (1,10,2):
    print(i)
# 5.nested for loops
for i in range(1,4):
    for j in range(1,3):
       print(f"i={i},j={j}")
#6.using break in for loop
for i in range(1,6):
    if i==4:
        break
    print(i)
#7.using continue in for loop
for i in range(1,6):
    if i==3:
        continue
    print(i)

#practice question 
#1.QUESTION PRINT ALL THE NUMBER 1 TO 20 FOR LOOPS
for i in range(0,20):
    print(i)
#2.QUESTION PRINT ALL THE EVEN NUMBERS LESS THAN 30
for i in range(2,30,2):
    print(i)
#3.QUESTION ITERATE OVER A LIST OF YOUR FAVOURITE COLORS AND PRINT EACH 

#PYTHON FUNCTION 
def greet():
    print("hello,python!")
greet()
#function with parameters
def greet(name):
    print(f"hello,{name}!")
greet("alice")
greet("bob")
#function with return value
#example 1 ADDITION
def add(a,b):
    return a+b
result=add(5,3)
print(result)
#example 2 SUBTRACTION
def sub(a,b):
    return a-b
result=sub(5,3)
print(result)
#example 3 MULTIPLICATION
def multi(a,b):
    return a*b
result=multi(5,3)
print(result)
#example 4 DIVISION 
def divide(a,b):
    return a/b
result=divide(5,3)
print(result)
#function with default parameters
def greet(name="student"):
    print(f"Hello,{name}!")
greet()

#scope of variable 
#LOCAL VARIABLE: declared inside a function, asseciable only inside
#GLOBAL VARIABLE:declared outside,asseciable anywhere
x=10
def my_function():
    y=5
    print("inside:",x,y)
my_function()
print("outside:",y)

#practice questions
#QUESTION 1
def greet():
    print("hello")
greet()
#QUESTION 2
def add(a,b):
    return a+b
result=add(10,20)
print(result)
#QUESTION 7
A=30
def my_function():
    B=25
    print("inside:",A,B)
my_function()
print("outside:",A)


#OOPS IN PYTHON 
#1.CLASS AND OBJECT
class car:
   def __init__(self, brand, color):
       self.brand = brand
       self.color = color
   def drives(self):
       print(f"the {self.color} {self.brand} is driving🚗")
car1 = car("bmw","back")
car2 = car("tesla","white")
car1.drives()
car2.drives()

#DAY4
#ARRAY :its is an collection of items of the same type 
#1. USING ARRAY MODULE 
import array
numbers=array.array('i',[1,2,3,4,5])
print(numbers)
#2.ACESSING ARRAY ELEMENTS 
print(numbers[0])
print(numbers[3])

#RANDOM NUMBER IN NUMPY
from numpy import random 
x=random.randint(100)
print(x)
print(type(x)) 


x=random.randint(100,size=(5))
print(x)
x=random.randint(100,size=(3,5))
print(x)
x=random.randint(100,size=(3,5,7))
print(x)
x=random.randint(100,size=(3,5,7,9))
print(x) 
x=random.choice([4,5,6],size=(5))
print(x) 

#PANDAS
import pandas as pd
data = [10,20,30,40]
s=pd.Series(data)
print(s)
#DATA FRAMES
import pandas as pd
data={"Name":["alice","bob","charlie","david"],
"Age":[24,27,22,32],
"City":["Delhi","Mumbai","Chennai","Kolkata"]
}
df=pd.DataFrame(data)
print(df)
#FROM NUMPY ARRAY
import numpy as np
arr=np.array([1,2,3,4,5])
s=pd.Series(arr)
print(s)
#from a dictionary
data={"math":90,"science":85,"english":78}
s=pd.Series(data)
print(s)

#DAY5
