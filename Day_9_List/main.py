# tea=["sonalika","indo form","mahindra arjun","new holland","jhon deere"]
# print(tea)
# print(tea[1])---first 
# print(tea[-1])---> last 
# print(tea[1:3])-->slicing 
# print(tea[1:5:2])--->skipping 
# tea[3]="my new tractor"---> change the value 
# print(tea)

# tea[1:2]="hmttract"---> like a array not suggest
# tea[1:2]=["now add"] ---> it will add at the 1 index 
# tea[1:3]=["first","second"]--->it replace the both of the element 
# print(tea[1:1])---->

# tea[1:1]=["same","same"]---> add the from the list in define index contigeuos 
# tea[4:4]=["one","second","third"]------>add contigeuos from the 4 index 

# print(tea)

# for tractor in tea:
#     print(tractor)

# if "novo" in tea:
#     print("yes there are available")
# else:
#     tea.append("novo") # add the last of the list 
# print(tea)

# if "novo" in tea:
#     print("now available")

# tea.pop()#---> remove the last value for the list 
# tea.remove("new holland")---> remove defineable index 
# tea.insert(3, "position")-----> add at position 

# tea2=tea ----> same memory reference 
# tea2=tea.copy() #---->two differ copy inside the memory (mutable)

# list comprehension ----------
# write and calculation inside the lsit 
# listt=[1,3,5,6,7,8,7,8]
# square_lisst=[x**2 for x in listt]
# print(square_lisst)

# [operation loop ]

# list comprehension 
# print([x**4 for x in range(1,11)])

list1=[10,100,1000,10000,100000,10000000,100000000,100000]
print([x+2 for x in list1])


# print(tea)

