# --------Question---------
# Q:1  Basic class and object 
# -->crate a car class with attribute like brand and model. 
# then create an instance of this class.

# class Car:
#     brand=None
#     model=None

# my_car=Car()-->some problem with pass variable
# print(my_car)

# another 
# class Car:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model

# my_car=Car("scarpio","s11")
# print(my_car.brand)
# print(my_car.model)
# my_car2=Car("Toyota","fartuner")
# print(my_car2.brand)
# print(my_car2.model)


# Question 2: Class method and self
# ---> Add a method to the Car class 
# displays the full name of the car (brand and model).

# class Car:
#     def __init__(self,brand, model):
#         self.brand=brand
#         self.model=model
#         # self.price=price
#     def full_name(self):
#         # print(self.brand +" "+self.model)
#         return (f"{self.brand} {self.model}")


# my_car=Car("sacrpio","s11",1000)
# # print(my_car.brand)


# # print(my_car.full_name())
# print(my_car.price())


# Question 3:
# --Inheritance:
# Problem: Create an Electric car that inherit from the Car
# class and has an addition attribute battery_size.

# class Car:
#     def __init__(self,brand,model,price):
#         self.brand=brand
#         self.model=model
#         self.price=price
#     def show(self):
#         return (f"{self.brand} {self.model} {self.price}")
    
    
# # inheritance
# class Electric_car(Car):
#     def __init__(self,brand,model,price,battery_size):
#         super().__init__(brand,model,price)
#         self.battery_size=battery_size
#     def show2(self):
#         return(f"brand is{self.brand}and model is {self.model} and price is{self.price} and the batterry is  {self.battery_size}")
       
    
# my_car=Car("mahinda","sacarpio", 150000,)
# print(my_car.show())

# # 2nd 
# my_electric_car=Electric_car("Tesla","hybrid","2Cr","large")
# print(my_electric_car.show2())
# print(my_electric_car.show())
   
   
# Question : 4
# --------Encapsulation: private only access inside the class.
# -->
# --> Modify the car class to encapsulate the brand attributes,
# making it private, and provide a getter method for it 

# class Car:
#     def __init__(self,brand,model,price):
#         self.__brand=brand
#         self.model=model
#         self.price=price
#     def show(self):
#         return (f"{self.__brand} {self.model} {self.price}")
    
#     def get_brand(self):
#         return (self.__brand ,"!")


# # second inherit class 
# class Electric(Car):
#     def __init__(self, brand, model, price,special_fea):
#         super().__init__(brand, model, price)  
#         self.special_fea=special_fea 
#     def show2(self):
#         return (f"{self.brand} {self.model} {self.price} special {self.special_fea}")
             

# # first object 
# obj=Car("mahindra","scarpio",1222)
# # print(obj.get_brand())
# # print(obj.show())
    
# # # second class obj 
# # obj2=Electric("toyota","fortuner",350000,"suroof")
# # print(obj2.show2())
# # print(obj2.get_brand())
# # print(obj2.brand)

# print(obj.get_brand())
# print(obj.show())
# # print(obj.__brand)
    


# -----Polymorphism--- one method can take different type
# Question:5 many type , many form 
# Problem: Demonstrat the polymorohism by
# defining a method fuel in both Car and 
# electricCar classes but with different behavior 

'''
class Car:
    object_count=0
    def __init__(self,brand,model,price):
        self.__brand=brand
        self.model=model
        self.price=price
        Car.object_count+=1 #can call by object
        self.object_count+=1 #can take like this
    def show(self):
        return(f"{self.__brand} {self.model} {self.price}")
    def fuel_type(self):
        return "petrol or disel"

class ElectricCar(Car):
    def __init__(self, brand, model, price,special_method):
        super().__init__(brand, model, price)
        self.special_method=special_method
    def show2(self):
        return (f"{self.brand} {self.model} {self.price} {self.special_method}")
        
    def fuel_type(self):
        return "charge"

safari=ElectricCar("tata", "safari","3433","sunrooof")
safari2=Car("tata", "safari","3433")
safari23=ElectricCar("tata", "safari","3433","sunrooof")

print(safari2.fuel_type())
print(safari.fuel_type())
print(Car.object_count) # its counted the objects of the variable.

'''

        
# Question:6 Class Variables
# Problem: Add a class variable to Car that keep track 
# of the number of cars created . track the objects of one class.
# ----------this questoin is solved in uper 


# Question:7 Static Variable (@staticmethod)-->called decorator this method inhanced the functionality of the method or function.,rule inhanced
# Add a static method to car class that return a general descreption of a car 
# static method --> can't access by object directly

# class Car:
#     def __init__(self,brand,model,price):
#         self.brand=brand
#         self.model=model
#         self.price=price
#     # staticmethod
#     @staticmethod
#     def static_method():
#         return("This is static method it not will be call through the object")

# obe=Car("scarpio","mahindar","2332223")
# print(obe.static_method())
# # it also called by the car object but its not recommonded always called by the classname directly.
# print(Car.static_method())

# Question 8: Property Decorator
# Use a property decorator in the Car class to make the model attribute read-only
# @property ---->make private not for access everyone , access by some special method

# class Car:
#     def __init__(self,brand,model,price):
#         self.brand=brand
#         self.__model=model
#         self.price=price
#     # staticmethod
#     @staticmethod
#     def static_method():
#         return("This is static method it not will be call through the object")
#     @property #hide this method not access for every one make sure change will never
#     def model(self):
#         return self.__model

# obj=Car("bolero","mahindra","121212")
# # print(obj.model())
# # obj.__model="toyota"
# print(obj.model)


# -----------Inheritance and insinstance() Function
# Problem: Demonstrate the use of insinstance if my_tesla  is an instance of the Car and elelctric car 
        # isinstance --> is method to check which instance of the class.
        
# 10. Multiple Inheritance:
# Create tow class battery and engine and let the ElectricCar class inherit form both, 
# demonstrating multiple inheritance.

class Battery:
    def battery_info(self):
        return "this is battery class"
    pass
class Engine:
    def ingine_info(self):
        return "this is engine info class"

class ElectricCar2(Battery,Engine):
    def main(self):
        return "this class is inherite by all "

my_new_car=ElectricCar2()
print(my_new_car.battery_info())
print(my_new_car.ingine_info())
print(my_new_car.main())
        
        
        
    

