'''
Normal global variables are simply declared outside functions.
Use the global keyword to declare a global variable inside function.
However the function must first be called before a global variable defined inside can be accessed.
'''
def multiply_values(num_1, num_2):
    global ubiq
    ubiq = "free radical"
    return num_1 * num_2

def use_default_param(var_1, var_2=9):      #default parameters
    print("Value 1 is: " + str(var_1))
    print("Value 2 is: " + str(var_2))

def use_args(*sentences):               #*args when you have an indefinite number of arguments
    for sentence in sentences: 
        print(sentence)

def use_kwargs(**emails):               #*kwargs when you have a dictionary
    for k, val in emails.items(): 
        print("Name = {}, email = {}".format(k, val))
        print(f"Name = {k}, email = {val}")

print(f"Product of multiplication is {multiply_values(9, 6)} plus {ubiq}")
use_default_param(7)
use_args("This is sentence 1", "This is sentence 2", "This is sentence 3", "This is sentence n")
use_kwargs(a='joebrown@test.com', b='johndoe@test.com', c='mikelee@test.com')
# import and use built-in module
import random as r
print(r.random())
# import and use custom module. divmod.py is in same path
import divmod as dv     #import custom module divmod.py with alias dv
print(f"The results are {dv.divmod_func(3,3)} and {dv.div_by_3(9)}") # call divmod_func and div_by_3
# import and use custom module. divmodrel.py is in different path. requires sys.path.append and os
import sys
import os
#this is relative path. 'testmod' is one directory up. '..' is one directory down
sys.path.append(os.path.join(os.path.dirname(__file__), 'testmod')) 

# Now you can import modules from the 'my_modules' directory
import divmodcp as dvcp
print(f"The results are {dvcp.divmod_func(3,3)} and {dvcp.div_by_3(9)}")

#this is full path
sys.path.append(os.path.join(os.path.dirname(__file__), '/home/username/learnpy/prep-pcep/learn-python-quickly/testmod2'))
import divmodcp2 as dvcp2 
print(f"The results are {dvcp2.divmod_func(3,3)} and {dvcp2.div_by_3(9)}")