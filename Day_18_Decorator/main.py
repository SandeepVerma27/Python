'''
Problem 1: Timing function Execution
-->Write a decorator that measure the time a function takes to execute.

import time
def timer(func):
    def wrrapper(*args,**kwargs): # can take **kwargs
        start=time.time()
        result=func(*args, **kwargs)
        end=time.time()
        print(f"{func.__name__} run in {end-start}")
        return result
    return wrrapper


@timer
def example_function(n):
    time.sleep(n)
example_function(1)
 '''
 
'''
Problem 2: Debugging function call
Create a decorator to print the function name and the values of its arguments every time the function is called. 

  
def debug(func):
    def wrapeer(*args, **kwargs):
        args_value=', '.join([str(arg) for arg in args])
        kwargs_value=', '.join(f"{key} {value}" for key,value in kwargs.items())
        print(f"{func.__name__} args value {args_value} {kwargs_value}")
        return func(*args , **kwargs)    
    return wrapeer

@debug
def greet(name , greeting="Hare Ram"):
    print(f"{greeting}, {name}")
    
greet("sandeep")
''' 

'''
Problem : 3--> Cache Return Values
Implemented a decorator that caches the return values of a function, so that when 
it's called with the same argument the cached is returned instead of re-executing the function
'''
import time
def cache(func):
    cache_val={}
    def wrapper(*args , **kwargs):
        if args in cache_val:
            return cache_val[args]
        result=func(*args , **kwargs)
        cache_val[args]=result
        return result
    return wrapper

@cache
def long_running_function(a,b):
    time.sleep(4)
    return a+b

print(long_running_function(2,5))
print(long_running_function(2,5))
print(long_running_function(2,7))













    

