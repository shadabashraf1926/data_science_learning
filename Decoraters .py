'''
   Decoraters basically allows us to wrap another function and add
   functionality to it.
   
   It never changes the code of funcion but it modifies or
   extend the behaviour of the function.
   
   It is used for logging, timing, access control,
   or modifies the behaviour of the code. 
   
   
   lets us take some example:-
   
   
   '''
   
   
def my_decoraters(func):
    def inner_deco():
        print(f"Good morning")
        func()
        print(f"good night")
        
    return inner_deco
    
    
    
'''Decoraters applied using "@decoraters" syntax just above the function'''    
    
    
@my_decoraters
def Today_schedule():
    print("Today we are going to learn about decoraters,we have taken some notes and studied further")
   
   
print(Today_schedule())   

''' our result will be:_
    Good morning
    Today we are going to learn about decoraters,we have taken some notes and studied further")
    Good night'''


## Let`s take another example :- 

## First we create a decorater.

import time

def timer_test(func):
    def inner_timer_test():
        start = time.time()
        print(start)
        func()
        end = time.time()
        print(end)
        
    return inner_timer_test

## then add a function to it.

@timer_test
def add():
    a=2
    b=3
    print(a+b)
    print(b-a)
    
    
print(add())
    
    
'''first it will print the start time.
   then add and subtract the number.
   and after that it will gives us the end time'''