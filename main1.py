# = variables
from itertools import product


x = 1 # storing integer
y = 2.5 # storing real number
z = 'string' # storing string or text
n =  'a' # storing character
b = True # storing a boolean value
print(x,y,z,n,b)

# title()
text = 'this blog is awesome'
print(text.title())

# upper()
text = 'this blog is awesome'
print(text.upper())

# lower()
text = 'THIS BLOG Is AWESOME'
print(text.lower())

# Concatenation of strings
text = 'this blog is awesome'
text2 = ' for beginners'
print(text+text2)

# white spaces
print('this blog is\nawesome')
print('\tthis blog is awesome')

# strip functions
z = '  hello'
print(z)
print(len(z))
print(z.strip())
print(z.rstrip())
print(z.lstrip())


# string length
Z ='awesome is the name given to good'
print(len(Z))

# integers whole numbers or real numbers using type it tell you variable datatype
a = 1
type(a)


# floatsfor decimals
a = 1.6
type(a)


# operations of floats and integers
x= 1 # storing integer
y= 2.5 #storing real numbers
z='string' # storing string or a text
n= 'a' # storing character
b= True # spring(x,y,z,n,b)storing a boolean value
print(type(x),type(y),type(z),type(n),type(b))


#type Conversion
#int()
a= '6'
b= 6.5
print(int(a),int(b))

# works only for numbers in str to integers
#a= 'a'
#print(int(a)) # will show error

#float() converts any real number in string form or any integer to float
a='6.5'
b=7
print(float(a),float(b))


#str() converts any int or float to str
a= 6
b= 6.7
c=True
print(str(a),str(b),str(c))


#bool() converts any int, str, float into boolean value
a=a
b= 0
c='c'
print(bool(a),bool(b),bool(c))

#......................................................


# 3 python tuples, lists, sets and dictionaries
# lists in python (in built in python)
# An empty list
empty_list = []
#List with same type of elements
same_type_list = ['1','2','3','6','70']
# list with different types of elements
diff_type_list = ['John','Dev','1.90','True']
print(empty_list)
print(same_type_list)
print(diff_type_list)

# using len(list)
#printing the lenghth of the list
some_list =['p','e','t','e','r','o']
print(len(some_list))
# traversal
for i in range(len(some_list)):
            print(some_list[i])

#max(list)
# printing the maximum of the number stored in the list
num_list = ['1','2','3','4','5','12','78','900','100']
print(max(num_list))


#min(list)
num_list = ['1','2','3','4','5','12','78','900','100']
print(min(num_list))


# sort(list)
#syntax is list.sort(reverse=True|False,key=some function)
num_list = ['1','2','3','4','5','6','900','8','101']
print(num_list)
num_list.sort()
print(num_list)
num_list.sort(reverse = True)
print(num_list)


#map(function,sequence)
#syntax= map(fun,iter)
def square(n):
        return n * n
numbers =[1,2,3,4,5,6,7,8,9]
result= map(square,numbers)
print(list(result))

#python tuple cannot be modified
#creating an empty tuple
empty_tuple = ()

seq_set = {1,2,3}
seq_list = [2,3,4,5]
print(type(seq_set))
print(type(seq_list))
# Converting set into tuple
seq_set_tuple = tuple(seq_set)
print(type(seq_set_tuple))
seq_list_tuple = tuple (seq_list)
print(type(seq_list_tuple))

#difference between python tuples and lists
#tuples with same type of elements
same_type_list = ('1','3','7','10')
print(same_type_list)

#List with different types of elements
diff_type_list = ('John','Dev',1.90,True)
print(diff_type_list)




#PYTHON SETS AND DICTIONARIES
# python sets

#Create a Set using
#A string
print(set('Dev'))

# a list
set(['Mayank','Vardhman','Mukesh','Mukesh'])
print(set(['Mayank','Vardhman','Mukesh','Mukesh']))

# a tuple
set(('Lucknow','Kanpur','India'))
print(set(('Lucknow','Kanpur','India')))

# a dictionary
set({'Sulphur':16,'Helium':2,'Carbon':6,'Oxygen':8})
print(set({'Sulphur':16,'Helium':2,'Carbon':6,'Oxygen':8}))


# operations in Python sets
# Adding an element in a set:
#syntax is set.add(element)
locations = set(('Lucknow','Kanpur','India'))
locations.add('Nairobi city'.upper())
locations.add('mombasa'.title())
locations.add('Kisumu'.upper())
print(locations)

#removing an element fro a set
#3  ways and the syntax is..
#set.remove(element)
#set.discard(element)
#set.pop()
locations = set(('Lucknow','Kanpur','India'))
#removes Lucknow from the set
locations.remove('Lucknow')
print(locations)

locations = set(('Lucknow','Kanpur','India'))
#removes Lucknow from the set
locations.discard('Lucknow')
print(locations)

#set.pop it removes any element from set
locations = set(('Lucknow','Kanpur','Malaysia','India'))
#removes any element from the set
removed_location = locations.pop()
print(locations)
print(removed_location)


#Dictionaries in Python
# Creating an empty Dictionary
Dictionary = {}
print('\tEmpty \nDictionary:'.upper())
print(Dictionary)

#also using dict()
#Creating Dictionary
#With dict9 method
Dictionary= dict({1:'Hello',2:'World',3:'!!!'})
print('\nDictionary by using dict()method:'.upper())
print(Dictionary)

#Creating a Dictionary
Dict = dict({(1,'Hello'),(2,'World')})
print('\nDictionary  by using list of tuples of key and values as a pair:')
print(Dict)


# copy() returns a copy of the dictionary
#clear() removes all the items from the dictionary
#pop() removes and returns an element from a dictionary having the given key
#popitem() removes the arbitrary key-value pair from the dictionary and returns it as a tuple
#get()to access a value for a key
#dictionary_name.values() returns a list of all the values available in each dictionary
#str() it produces a printable string representation of a dictioanary
#update() it adds dictionary key-values pairs to a dictionary
#setdefault() it sets dict[key]='default' if key is not already in the dictionary
#keys() it returns list of dictionary dict`s keys
#items() returns list of dictionaries(key,value)tuple pairs
#has-key()returns true if key in dictionary,false otherwise
#fromkeys() create a new dictionary with keys and values set to value
#type()returns the type of the passed variable
#cmp() Compares elements of both dictionries

# Difference between python sets and dictionaries
# set is a collection of values not necessarily of the same type
#dictionary stores key-value pairs


#5 Conditional statements
#Conditional statements in python-what do they do
#python input()
#Take input
# x=input()
# print(x)

#input with string query in it.
#Take input
#x=input('Please enter your age. ')
#z= ' years old'
#print(x+z)

#datatype functions used in the typecast of a datatype
#Take input
#x=int(input('please enter your age. '))
#y= input('please enter your age. ')
#print(type(x))
#print(type(y))

#if statement in python
#if statement
mask= True
if mask==True:
        print('The person can enter')
     
#syntax in python
#== is for comparison
#what if ?
mask= False
if mask==True:
        print('The person can enter')


#if else in python
#if else statement
mask= True
if mask== True:
        print('The person can enter')
else:
        print('Please, get a mask to enter')


mask= False
if mask== True:
        print('The person can enter')
else:
        print('Please, get a mask to enter!')

#if else statement
mask='nobuy'
if mask =='yes':
        print('the person can enter')
elif mask =='buy':
        print('person bought the mask and can enter')
else:
        print('please, get a mask to enter')


#if else statement
mask ='yes'

if mask=='yes':
        print('the person can enter')

elif mask=='buy':
        print('person bought the mask and can enter')

else:
        print('please, get a mask to enter')


#if else statement
mask='buy'

if mask =='yes':
        print('the person can enter')

elif mask=='buy':
        print('person bought the mask can enter')

else:
        print('please, get a mask to enter')     




#if else statement
mask='test'

if mask =='yes':
        print('the person can enter')

elif mask=='buy':
        print('person bought the mask can enter')

elif mask== 'test':
        print('there is a chance you might enter')

else:
        print('please, get a mask to enter')     



# ASSIGNMENT
#Write a conditional statement program to print grades of a person when their marks are given.
#Please use input in the program.The conditons to be fulfilled are:
# if a student marks > 90 print A
# if a student marks greater than 8o and less than 90 print B
# if a student marks greater than 70 and less than 80 print c
# if marks greater than 60 and less than 70 print D
# if a student marks less than 60 print F

#SOLUTION
# no quotations on integers!

#marks = int(input('Please enter your marks(0-100):\n')) 

#if marks >90 and marks <=100:
        #print('You have Grade: A')
#elif marks >80 and marks<=90:
        #print('Grade: B')
#elif marks >70 and marks<=80:
        #print('Grade: C')
#elif marks >60 and marks <=70:
        #print('Grade: D')
#elif marks <=60:
        #print('Grade: F')
#else:
        #print('invalid')


#6 loops in python
# "for" loop in python

#for Loop
#for var in range(10):
        #print(var)


#for var in range(0,10,1):
       # print(var)


# for loops in list
#X=[1,2,3,4,5,6]
#for i in X:
      #  print(i)


#to include the index 
#X= [1,2,3,4,5,6]
#for i in range(len(X)):
        #print(i,X[i])



#using enumeration function

X= [1,2,3,4,5,6]
for i,value in enumerate(X):
        print(i,value)




#iterating a set using for loop
X={1,2,3,4,5,6}
for i, value in enumerate(X):
        print(i,value)



#iterating a tuple using for loop
X=(1,2,3,4,5,6)
for i,value in enumerate(X):
        print(i,value)




#iterating a dictionary using for loop

X= {"1":1,"2":2}
for key in X.keys():
        print(key)

for value in X.values():
        print(value)

for key,value in X.items():
        print(key,value)




#nested loops in python
a=[1,2]
b=[10,13]
# getting numbers whose product is 13

for i in a:
        for j in b:
                if i*j==13:
                        print(i,j)



#alternative way 

a=[1,2]
b=[10,13]

# getting numbers whose product is 13
for i,j in product(a,b):
 
 if (i*j==13):
         print(i,j)



#while loops in python
# printing 0-9 using while loop
i= 0
 
while (i<10):
        print(i)

        i+= 1

#while loops in python
# printing 0-9 using while loop
#i= 0
 
#while (i<10):
       # print(i)

        #i+= 1



# while loop = execute some code WHILE some condition remains true
name = input("Enter your name: ")

while name =="":
    print("You did not enter your name")
    name = input("Enter your name: ")
print(f"Hello {name}".upper())


age = int(input("Enter your age: "))

while age < 0:
    print('Age can`t be negative')
    age = int(input('Enter your age: '))

print(f'You are {age} years old.')


food = input('Enter a food you like (press q to quit): ')

while not food == 'q':
    print(f'You like {food}')
    food = input('Enter another food you like: ')

print('Bye')



num = int(input('Enter a # between 1 - 10: '))

while num < 1 or num > 10:
    print(f'{num} is not valid!')
    num = int(input('Enter a # between 1 - 10: '))

print(f'Your number is {num}')
   

#python functions as objects
#assigning functions to variables
# first function

def sum(a,b):
   return a+b

sumab=sum

del sum
s=sumab(7,8)

print(s)


#storing python functions in data Structure
#function stories in datastructure

#storedfunctionslists=[len,str.upper(),str.strip(),str.lower()]

#storedfunctionslists

#for fun in storedfunctionslists:
   #print(fun,fun('Hello'))


# Advanced functions in python

def mul(x,y):
    return x*y

def add(mul,y):
    return mul+y

x = add(mul(9,10),10)
print(x)


# using functions inside a function

def mul(x,y):
    m = x*y

    def square(m):
        return m*m
    
    return square(m)

x = mul(9,10)

print (x)



#Arguements in python

def maxarea(a,b):
    if a>b:
        return f'rectangle a has the more area which is {a}'
    else:
        return f'rectangle b has the more area which is {b}'
    
x= maxarea(100,60)
#x= maxarea(10,60)
print(x)


# if there is list
def maxarea(list):
    max = 0
    for i in list:
        if i > max:
            max =i
    return f'rectangle which has the more area is {max}'

x = maxarea([100,60,50])
print(x)

# "*" operator in python
#unpacking arguements into tuple * operator

x= [1,2,3,4]
y= [5,6,7,8]

z=[*x,*y]

print(type(z))
print(z)




#Lists are mutable: Lists are dynamic and allow for modification 
#after creation. You can add, remove, or .
# change elements within a list. Lists are enclosed in square brackets []
my_list = [1, 2, 3]
my_list.append(4)
my_list[0] = 5
print(my_list)  # Output: [5, 2, 3, 4]
##Tuples are immutable: Once a tuple is created, its elements cannot be 
# changed, added, or removed. This makes them suitable for representing 
# fixed collections of data, like coordinates or RGB color values, where the values 
# are not expected to change. Tuples are typically enclosed in parentheses ()
my_tuple = (1, 2, 3)
    # my_tuple[0] = 4  # This would raise an error


# *args
def maxarea(*list):
    max= 0
    for i in list:
        if i > max:
            max =i

    return f'rectangle which has the more area is {max}'

x = maxarea(100, 60, 50, 200)
y = maxarea(100, 60, 50, 200, 9000)
z = maxarea(100, 60, 50, 20, 90)
print(x)
print(y)
print(z)



#**kwargs in python
a= {'h':1,'n':2}
b= {'m':5,'I':10}

c= {**a,**b}

print(type(c))
print(c)



a = {'h':1,'n':2}
b = {'m':5,'I':10}
c = {*a,*b}
print(type(c))
print(c)


#The maxarea function using **kwargs 
def maxarea(**list):

    max= 0
    for i in list.values():
        if i >max:
            max= i

    return f'rectangle which has the more area is {max}'


x= maxarea(a=1,b=2,c=3)
y=maxarea(a=1,b=2)
z=maxarea(a=1,b=2,c=3,d=9)
print(x)
print(y)
print(z)
























































































































































