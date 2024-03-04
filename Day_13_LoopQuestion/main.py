# --------Loop questions---------
'''
Question 1 Continuing Positive Number :
numbers =[1,-2,3,-4,5,6,-7,-8,9,10]

numbers =[1,-2,3,-4,5,6,-7,-8,9,10]
positive=[]
positive_count=0
negative=[]
negative_count=0
for num in numbers:
    if num >0:
        positive_count=positive_count+1
        positive.append(num)
    else:
        negative_count=negative_count+1
        negative.append(num)
print("Positive Number: ",positive, "and cout is ",positive_count,)
print("Negative Number: ",negative,"Negative count is",negative_count)
'''  
'''
Questions 2 :

number=int(input("Enter the number: "))
sum=0
for num in range(1,number+1):
    sum+=num
print(sum)
'''

'''
modify question2 sum of all even number :


number =int(input("Enter the number: "))
sum=0
for num in range(1, number+1):
    if num%2==0:
        sum+=num
print(sum)
'''      

'''
Question 3 
Print the multiplication table for the given number up 10, but 
skip the number 5 

for num in range(1, 11):
    if num==5:
        continue
    
    else:
        print(num)
        print()
        for j in range(1,11):
            print(j," x ",num," = ",j*num)
        print()
    print()
            
'''

'''
Question 4: Reverse a string usign loop


input_string=input("Enter the string for the reverse: ")
reverse_string=""
for char in input_string:
    reverse_string=char+reverse_string
print(reverse_string)
'''

'''
Question:5
Find the first Non-repeated character in given string

input_string=input("enter the string :")
for i in input_string:
    if input_string.count(i)==1:
        print(i)
        break
'''
'''
Question 6: factorial of the give number:
5*4*3*2*1 

number =int(input("Enter the number that you want: "))
fact=1
for i in range(1,number+1):
    fact=fact*i
print(fact)
    
    
number=int(input("Enter the number: "))
fact=1
i=1
while (i<number+1):
    # fact=fact*i
    fact*=i
    i+=1
    # i=i+1
print(fact)
    
''' 

'''
Question-7: 
Validate input:
Keep asking the user for input
until they enter a number between 1 and 10.


while True:
    number=int(input("Enter the number between 1 to 10: "))
    if 1<= number <=10:
        print("Thanks")
        break
    else:
        print("invalid number: ")
 '''
 
'''
 Question : 8 : print the prime number 1 to n
   
number=int(input("Enter the number"))
count=0
for i in range(2,number+1):
    if (number%i == 0):
        count=count+1
if(count==1):
    print("Prime Number")
else:
    print("Non-Prime")
 '''

'''
Question 9 : List Uniqueness checker:
check the elements in a list are unique. if a duplicate is found, exit the loop and print the duplicate.
items=["apple","banana","orange","apple","mongo"]

items=["apple","banana","orange","apple","mongo"]
count =0
reapet=set()
for item in items:
    if items.count(item)>1:
        reapet.add(item)
        count=count+1      
print(reapet,count)
 '''
'''
Question :10
implement an exponential backoff strategy that double the
wait time between retrives, starting from
1 second, but stop after 5 retries
'''  

'''
Problem 10 : Implement an exponential backoff
strategy that double the wait time between retries, starting form 1 second, but after 5 retries.
'''
import time
wait_time=1
max_retries=5
attempt=0

while attempt<max_retries:
    print("Attempt",attempt+1,"- wait time",wait_time, )
    time.sleep(wait_time)
    wait_time*=1.5
    attempt+=1





     
    
        
    




    
    













































