tupp=("mahindra","indoform","arjun novo","sonalika")

# print(tupp[2]) #print index on given 
# print(tupp[1:]) #print from one index 
# tupp[2]="nott ad "-----> error because of tuple is not changable
 
tupp2=("hmt","new holland","swaraj")
alltupp=tupp+tupp2
print(alltupp) #-----> all add in new varible 

if "hmt" in tupp2:
    print("yes here ")
else:
    print("no")