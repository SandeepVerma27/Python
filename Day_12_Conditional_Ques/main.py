# -----condition statement--------
# 10 Question in conditional statement 

'''
 1. Age Group categorization
    ---->Child(<13),Teenager(13-19),Adult(20-59),Senior(60+)
Age =int(input("Enter Your age : "))
if(Age<13):
    print("You are 'Child ': ")
elif(Age>13 and Age<19):
    print("You are 'Teenager' : ")
elif(Age>20 and Age<59):
    print("Your are 'Adult' person")
else:
    print("Respect the 'Senior' people")


Age=70
if Age<13:
    print("child")
elif Age<20:
    print("teenager")
elif Age <60:
    print("Adult")
else:
    print("Senior people")
'''


'''
2. Movie Ticket Pricing
   ------>Bassed on age $12 for adults (18 and Over ) $8 for children. 
   Everyone get $2 discount on wednesday.
   

Day=input("Enter the day: ")
if Day=="wednesday" or Day=="Wednesday":
    Age =int(input("Enter the age for discount: "))
    if Age <18:
        print("Your movie ticket is and discount :" ,"$",8-2 )
    else:
        print("Your movie price with the discount is :","$",12-2)
else:
    Age =int(input("Enter the age for discount: "))
    if Age <18:
        print("Your movie ticket is : ", "$",8)
    else:
        print("Your movie price with the  :","$",12)  

age =66
day="wednesday"

price= 12 if age>=18 else 8
if(day=="wednesday"):
    price-=2
print(price)

'''

'''
3. Grade Calculator
   ------->Assign a letter grade bessed on a student score
   A(90-100), B(80-89), C(70-79), D(60-69), F(below - 40).


score=int(input("Enter the score : "))
if(score<0 or score >100):
    print("Enter the range in 1 - 100 only ")
    exit()
else:
    if score>=90:
        print("A")
    elif score >=80:
        print("B")
    elif score >=70:
        print("C")
    elif score >=60:
        print("D")
    elif score >=50:
        print("E")
    else:
        print("F")   
'''

''' 
Question 3 : Determine a fruit is ripe,overripe on unripe bessed of color (eg . if Banana : Green - Unripe, Yellow:- Ripe , Brown-Overipe, )

color=input("Enter the color of banana: ")
fruit=input("Enter the fruit ")
if fruit=="banana" or fruit=="Banana":
    if color == "green" or color== "Green":
         print("Banana is Unripe")
    elif color == "yellow" or color== "Yellow":
        print("Banana is Ripe")
    elif color == "Brown" or color== "brown":
        print("Banana is Overripe")
    else:
        print("Enter the only 'Green','Yellow','Brown' only")

else:
    print("Enter only banana : ")




# Question 5
# Weather situation suggest an activity on the weather
# (eg Sunny- go for walk , Rainy - Read a book, Snowy- Build a snowman)
weather=input("Enter the weather condition: ")
if weather=="Sunny":
    print("you can go for a walk: ")
elif weather=="Rainy":
    print("Read the book: ")
elif weather=="Snowy":
    print("Build a snowman: ")
else:
    print("Enter the write weather! ")
'''
# transport endicator 
'''


distance=int(input("Enter the distance: "))
if distance<0:
    activity="Enter the valid distance: "
else:
    if distance <3:
        activity="Go walk"
    elif distance <15:
        activity="Go with bike"
    elif distance >25 and distance<300:
        activity="Go with Car"
    else:
        activity="go with transport"
print(activity)


9. question
   
password=input("Enter the password : ")
lenn=len(password)
if lenn <=3:
    warn="Very unsecure pass: "
elif lenn <=8:
    warn="strong password: "
elif lenn >10:
    warn="Very strong password" 
    
    
print(warn)
    

 '''


# leap year 

# divisible by 4 but not 100

# unless divide by 400
'''

year =int(input("Enter the year :"))
if year %400==0:
    print("Leap Year")
else:
    if (year %4==0 and year%100!=0):
        print("Leap year ")
    else:
        print("not lear year")
        
'''

# optimized approach
year=2023
if (year%400==0) or (year%4==0 and year%100!=0):
    print("Leap year " ,year)
else:
    print("Not leap year : ",year)





















































