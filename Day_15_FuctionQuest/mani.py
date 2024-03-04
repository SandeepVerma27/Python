'''
Question 1: basic function syntax.
write a function to calculate and return the square of a number.


# function definition :(def) definition name(parameter):
def square(number):
    return number**2

result=square(5)
print(result)
# print(square(3))

'''
'''
Question:2-->Create a function that take two number as a parameter and return their sum.



def sum(q,b):
    return q+b
result=sum(12,34)
print(result)
'''

'''
Polymorphism in function:
Question 3: write a function multiply that
multiplies two number, but can also accept and multiply strings

def mul(numberOne,numberTwo):
    return numberOne*numberTwo
print(mul(5,'s'))
print(mul('h',10))
print(mul(5,6))
'''
'''
Question 4: Function returning multiple value:
Create a function that returns both the area and
circumference of a circle given its radius

import math
def circle(radius):
    area=math.pi*radius**2
    circumference=2*math.pi*radius
    return area,circumference
a, c=circle(5)
print("Area",round(a,1) ,"circle",round(c,1))
'''

'''
Question:5
Default Parameter function:
Write a function that greet a user. if no name is provided. 
it should greet with a default name

def greet(name= " sandeep "):
    return print(name + "Take Care bro"+ " !")

print(greet())
print(greet('rahul'))
 '''
 
'''
 Lambda function 6: Create a lambda function to compute the cube of a number.
 
 one liner function for short work only one time use 
  
cube=lambda x: x**3
print(cube(2))
 ''' 
 
'''
Function with *args: 7
*args--> need to write the *args to take multiple value of the user

def sum_all(*args):
    # print(*args)
    print(args)
    print()
    return sum(args)
   
  
print(sum_all(12,3,4,5,5))
print(sum_all(12,3))
print(sum_all(12,3,4,5,3,4,5,45))
Write a function that takes variable number of argument and return their sum.
t
'''

'''
Question: 8  : Funtion with **kwargs
Create a function that accept any number of keyword 
argument and print them in the format in key:value.

def print_kwargs(name,power):
    print("name",name ,"power",power)

print_kwargs(power='50 hp',name='shaktiman') #---> does not matter of the order if argument passed with the named

but I want pass the value in function one with key or more 
than one one value use '**kwargs' for handle we need to for loop 

def print_args(**kwargs):
    for key , value in kwargs.items():
        print(f"{key}:{value}")
        
print_args(name="sandeep",course="b.tech")
print_args(name="shaktiman")
print_args(name="i am sandeep",course="mca",cso="mxkmxksxks",depar="jenjdn")
'''

'''
Question 9: Generate a function with the yield

Write a generator function that yields
even number up to a specified limit.

-yield---->

# simple method 
def even(number):
    # listl=[]
    for num in range(1,number+1):
        if num%2==0:
            print(num)
print(even(10))

def even_generator(number):
    li=[]
    for i in range(2, number+1,2):
        li.append(i)
    return li
print(even_generator(10))

# yield applying 
# yield---> yield is a mehtod that stor the value in location in
# memory and after the complete execution then return the value .


def even_generate(number):
    for num in range(2,number,2):
        yield num
        
for i in even_generate(10):
    print(i)
'''

'''
Question :10 Recursive Function 
Problem: Create a recursive function to calculate the factorial of a number.

Recursive--> recursive is the techniques that call the function inside the function.
check exit for the function.

def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))
'''

# fabonacii series 

# f1=0
# f2=1
# fn=f1+f2

def febo(n):
    if n<=1:
        return n
    else:
        return(febo(n-1)+febo(n-2))

for i in range(febo(6)):
    print(febo(i),end=' ')
    
        
        
        



        
        

    








    
    
    
    










