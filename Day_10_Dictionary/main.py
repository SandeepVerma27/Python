# choice={"key":"value","one":"mahindra 265","two":"arjun novo","third":"sonalika",4:"jhon deere",6:"swaraj"}

# methods 

# print(choice["key"])---> pass the key 
# print(choice.get("one")) #--> also to give value without the 
# print(choice.get("haha")) --> also give none if not present 
# choice[4]="balwaan" --> add the custom index value 

# for i in choice:
    # print(i)--> it's simple print the key only 
    # print(i,"=", choice[i])---> it give the value and key both 
# print(choice)
# print(choice)

# for key, val in choice.items(): # special for the dictionary 
#     print(key , val)
    
    
# if "one" in "sjs":
#     print("yes")----> 
# print(len(choice))
# choice["hare"]="krishna" ----> add the key and value in dict 
# print(choice)

# dell=choice.pop("two")--> must to define the key which you want to delete 
# print(dell)
# print(choice.popitem()) ---> it delete the last value of the dict .
# del choice["two"] ----> it delete the key and the value both

# choice2=choice.copy()---> two differ dict 
# choice2["shshs"]="sjnjs"
# print(choice2)
# {{},{},{},{}} dict inside the dict 
# print(choice)


# group={
#     "first":{'first':"first_number",'second':"second_number",'third':"third_number"},
#     "secon":{ 'neve':'dnskds','skekek':"dndnd"},
#     "third":{'first':"first_number",'second':"second_number",'third':"third_number"}
# }

# print(group["secon"]["skekek"])---> print inside the dict 

# dictionary comprehensive 

# squared_dict={x:x**3 for x in range(1,10)} #-->calculate the single line of the operation
# squared_dict.clear() #--->clear the list 
# print(squared_dict)


keys=["one","two","three"]
# default="number"
# defaultt=[["mahindra"],["arjun"],["novo"]] ---> it adding the as it is in every key 
new_dict=dict.fromkeys(keys,defaultt)  #------> set the value of the keys 
# new_dict=dict.fromkeys(keys,keys) ---> add the array of the every key 
print(new_dict)
    
    