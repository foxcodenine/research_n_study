# A decorator is a function that takes another function and extends the 
# behavior of the latter function without explicitly modifying it.

def pline():
    print('\n______________________________________________________ \n')



pline() # ______________________________________________________________


# 1. First-Class Objects

# In Python, functions are first-class objects. This means that 
# functions can be passed around and used as arguments

def say_hello(name):
    return f"Hello {name}" 

# print(say_hello('James')) 

def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

# print(be_awesome('James')) 

def greet_bob(greeter_func):
    return greeter_func("Bob")

# The greet_bob(), expects a function as its argument. 

print(greet_bob(say_hello))

print(greet_bob(be_awesome))

# The say_hello function is named without parentheses. This means that 
# only a reference to the function is passed. The function is not 
# executed. The greet_bob() function, on the other hand, is written with 
# parentheses, so it will be called.

pline() # ______________________________________________________________


# 2. Inner Functions

# It’s possible to define functions inside other functions. Such 
# functions are called inner functions.

def parent():
    print("Printing from the parent() function") 

    def first_child():
        print("Pringing from the first_child() function")

    def second_child():
        print("Printing from the second_child() function") 

    second_child()
    first_child()

parent()

# The inner functions are not defined until the parent function is called. 
# They are locally scoped to parent(): they only exist inside the parent() 
# function as local variables. If calling first_child() you'll get an error:

pline() # ______________________________________________________________

# 3. Returning Functions From Functions

# Python also allows you to use functions as return values. The following
#  example returns one of the inner functions from the outer parent() function:

def parent2(num):
    def first_child():
        print("Hi, I am Ema")

    def second_child():
        print("Call me Liam") 
    if num == 1:
        return first_child
    else:
        return second_child
        

# Note that you are returning first_child without the parentheses. 
# Recall that this means that you are returning a reference to the 
# function first_child. In contrast first_child() with parentheses 
# refers to the result of evaluating the function. 
# This can be seen in the following example:

first = parent2(1)
second = parent2(2)

print(first)
print(second)

first()
second()

pline() # ______________________________________________________________

# 4. Simple Decorators

def my_decorator(func): 
    def wrapper(): 
        print("Something is happing before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!") 

say_whee = my_decorator(say_whee)  

say_whee() 


pline() # ______________________________________________________________

# The so-called decoration happens at the following line:
# say_whee = my_decorator(say_whee) 

print(say_whee)

pline() # ______________________________________________________________

# 5. Another Example:

from datetime import datetime 

def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func() 
        else:
            print('Hush, the neighbors are asleep')
    return wrapper

def say_wheee():
    print("Wheeeeeeeeeeeeeeeeeeeeeee!")

say_wheee = not_during_the_night(say_wheee)

say_wheee()

pline() # ______________________________________________________________ 

# 6. Syntactic Surgar! 

def xmass_decorations(func):
    def wrapper():
        print("Christmass", end=' ')
        func() 
        print('XD XD XD XD XD XD') 
    return wrapper 

@xmass_decorations
def tree():
    print('Tree')
    
tree()

# Python allows you to use decorators in a simpler way with the @ symbol.

pline() # ______________________________________________________________ 

# 7. Another Example:

def do_twice(func):
    def wrapper_do_twice(): 
        func()
        func() 
    return wrapper_do_twice 

@do_twice 
def say_cheese():
    print("Cheese...")

say_cheese()

pline() # ______________________________________________________________ 

# 8. Decorating Functions With Arguments:
 
# For a wrapper to take Arguments (function with paramiters) you need 
# to use *args and **kwargs in the inner warpper function and also pass 
# them to its inner wrapped funtion/s

def do_two_times(func):
    def wrapper_do_two_times(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_two_times 



@do_two_times
def say_ham():
    print('HAM!')

say_ham()

@do_two_times
def greet(name):
    print(f'Hello {name}!')
        

greet('World')


pline() # ______________________________________________________________ 

# 9. Returning Values From Decorated Functions 

@do_two_times
def return_greeting(name):
    print("Creating greeting")
    return f'Hi {name}' 

# "Creating greeting"
# "Creating greeting"

hi_adam = return_greeting("Adam") 

print(hi_adam)
# None

# Because the do_two_times_wrapper() doesn't explicitly return a value, 
# the call return_greeting("Adam") ended up returning None.

# To fix this, you need to make sure the wrapper function returns the 
# return value of the decorated function.

def do_2_times(func):
    def do_2_times_wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return do_2_times_wrapper 

@do_2_times
def hello_greeting(name):
    print("Creating greeting")
    return f'Hello {name}'

hello_adam = hello_greeting('Adam') 

print(hello_adam)



pline() # ______________________________________________________________ 

# 10. Who Are You, Really?

print(print)

print(print.__name__)

help(print)

pline() # ______________________________________________________________ 

# Compare to our wrapped functions

print(say_cheese)

print(say_cheese.__name__)

help(say_cheese)


pline() # ______________________________________________________________ 


# To fix this, decorators should use the @functools.wraps decorator, 
# which will preserve information about the original function.

from functools import wraps 



def add_stuff(func):
    """Add stuff to the origial function"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        
        # Do something before         
        value = func(*args, **kwargs)
        do_something_before_n_after = f'Hello! {value}, See you latre'
        # Do something after
         
        return do_something_before_n_after 

    return wrapper 



@add_stuff
def nice_2_meet_u(name):
    """Greetings function"""
    return f'Nice to meet you {name}'




Chris = nice_2_meet_u('Chris')


print(nice_2_meet_u.__name__)

help(nice_2_meet_u)

print(nice_2_meet_u)

print(Chris)



pline() # ______________________________________________________________


# Notice that decoratorl mainly follow this pattern:

import functools 

def decorator(func):
    @functools.wraps(func):
    def wrapper_decorator(*args, **kwargs):
        # Do Something before 
        value = func(*args, **kwargs)
        # Do Something after 
        return value 
    return wrapper_decorator 

# 1. Define decorator and pass fanction as paramiter.
# 2. Add the @functools.wraps and pass the same fanction as paramiter. 
# 3. Define the wrapper function (inner function)
#    and pass *args, **kargs as paramiters
# 4. Do something before function / Original Function /dosomething after: 
# 5. Return function value 
# 6. Return wrapper function without executing it.