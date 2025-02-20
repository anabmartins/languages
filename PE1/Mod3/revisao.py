

## 1. You can pass information to functions by using parameters. Your functions can have as many parameters as you need.

def hi(name):
    print("Hi,", name)
 
hi("Greg")
 

## An example of a two-parameter function:

def hi_all(name_1, name_2):
    print("Hi,", name_2)
    print("Hi,", name_1)
 
hi_all("Sebastian", "Konrad")
 

## An example of a three-parameter function:

def address(street, city, postal_code):
    print("Your address is:", street, "St.,", city, postal_code)
 
s = input("Street: ")
p_c = input("Postal Code: ")
c = input("City: ")
address(s, c, p_c)
 

## 2. You can pass arguments to a function using the following techniques:

##    positional argument passing in which the order of arguments passed matters (Ex. 1)
##    keyword (named) argument passing in which the order of arguments passed doesn't matter (Ex. 2)
##    a mix of positional and keyword argument passing (Ex. 3.)

## Ex. 1
def subtra(a, b):
    print(a - b)
 
subtra(5, 2) # outputs: 3
subtra(2, 5) # outputs: -3
 
 
## Ex. 2
def subtra(a, b):
    print(a - b)
 
subtra(a=5, b=2) # outputs: 3
subtra(b=2, a=5) # outputs: 3
 
## Ex. 3
def subtra(a, b):
    print(a - b)
 
subtra(5, b=2) # outputs: 3
subtra(5, 2) # outputs: 3
 

## It's important to remember that positional arguments mustn't follow keyword arguments. That's why if you try to run the following snippet:

def subtra(a, b):
    print(a - b)
 
subtra(5, b=2) # outputs: 3
subtra(a=5, 2) # Syntax Error
 

## Python will not let you do it by signalling a SyntaxError.

## 3. You can use the keyword argument-passing technique to pre-define a value for a given argument:

def name(first_name, last_name="Smith"):
    print(first_name, last_name)
 
name("Andy") # outputs: Andy Smith
name("Betty", "Johnson") # outputs: Betty Johnson (the keyword argument replaced by "Johnson")
 
