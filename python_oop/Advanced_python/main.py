########################################### Magic Methods or Dunder ##############################################

### Magic methods in Python are the special methods that start and end with the double underscores.
### They are also called dunder methods. Magic methods are not meant to be invoked directly by you, but the invocation happens internally from the class on a certain action.
### For example, when you add two numbers using the + operator, internally, the __add__() method will be called.
### Built-in classes in Python define many magic methods e.g., dir(int) will show magic methods of int class.
### Similarly, we have __init__ magic method which is called automatically while defining object. We don't need to explicitly call this funcion like object.__init__()
### Similarly, we have __del__ which is destructor to delete the object. We can use del p to delete otherwise but underline __del__ method will be calling then too.
### Similarly, we can do magic methods overriding too in which pre-defined operator behavior is overloaded.
### For instance, arithmetic operators by default operate upon numeric operands like integers. This means that numeric objects must be used along with operators like +, -, *, /, etc.
### The + operator is also defined as a concatenation operator in string, list and tuple classes. We can say that the + operator is overloaded.
### In order to make the overloaded behaviour available in our own custom class like vector, the corresponding magic method should be overridden.
### For example, in order to use the + operator with objects of a vector class, it should include the __add__() method.
### In __add__ , self represents the first operand and other represents the 2nd operand like this v1.__add__(v2).
### if we remove the __add__ function, the code will give error of unsupported type vector() and vector() for + operator.
### Error will be :    TypeError: unsupported operand type(s) for +: 'Vector' and 'Vector'
### As add function is giving object , to represent the object we override the representation using __repr__ method.
### Similarly, we have len function overriden to just print 10 and call function to call the object.


                       ################ Magic Methods Briefing #################
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def __del__(self):
#         print('Object is being destructed!')
#
# p = Person('Usama',25)

                        ################ Magic Methods Overriding #################
#
# class Vector:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#
#     def __add__(self,other):
#         return  Vector(self.x + other.x , self.y + other.y)
#
#     def __repr__(self):
#         return f"X: {self.x} , Y: {self.y}"
#
#     def __len__(self):
#         return 10
#
#     def __call__(self, *args, **kwargs):
#         return 'Hello, I was called!'
#
#
# v1 = Vector(20,30)
# v2 = Vector(20,30)
# v3 = v1 + v2
#
# print(v3)
# print(v3.x)
# print(v3.y)
#
# print(len(v1),len(v2),len(v3))                      ### Method overrdiing of len function
#
# print(v3())                             ### To call the class object



########################################### Decorators ###########################################################

                          ################### Decorator Basic Idea #####################

### A Python decorator is a function that takes in a function and returns it by adding some functionality.
### Basically, a decorator takes in a function, adds some functionality to it and returns it.
### Here, we have created two functions: ordinary() that prints "I am ordinary" and make_pretty() that takes a function as its argument and has a nested function named inner(), and returns the inner function.

# def make_pretty(func):
#     def inner():
#         print("I got decorated")
#         func()
#     return inner
#
#
# def ordinary():
#     print("I am ordinary")

# Output: I am ordinary

### Similarly, we have another simple example to explain it. Here, mydecorator() is a decorator function.

# def mydecorator(func):
#     def wrapper():
#         print('I am decorating your function!')
#         func()
#     return wrapper
# def Hello_World():
#     print('Hello World!')
#
# decorated_func = mydecorator(Hello_World)
# decorated_func()

# ### We are calling the ordinary() function normally, so we get the output "I am ordinary".
# ### Now, let's call it using the decorator function.
# ### Notice that make_pretty() is a decorator and it is taking ordinary() function as its argument and returns the inner function, and it is now assigned to the decorated_func variable.
#
# def make_pretty(func):
#     # define the inner function
#     def inner():
#         # add some additional behavior to decorated function
#         print("I got decorated")
#
#         # call original function
#         func()
#
#     # return the inner function
#     return inner
#
#
# # define ordinary function
# def ordinary():
#     print("I am ordinary")
#
#
# # decorate the ordinary function
# decorated_func = make_pretty(ordinary)
#
# # call the decorated function
# decorated_func()
#
#               #################### @ Symbol With Decorator ############################
#
# ### Now , Instead of assigning the function call to a variable, Python provides a much more elegant way to achieve this functionality using the @ symbol.
# ### For example, Here, the ordinary() function is decorated with the make_pretty() decorator using the @make_pretty syntax, which is equivalent to calling ordinary = make_pretty(ordinary).
#
# def make_pretty(func):
#
#     def inner():
#         print("I got decorated")
#         func()
#     return inner
#
# @make_pretty
# def ordinary():
#     print("I am ordinary")
#
# ordinary()
#
#
#            ########################  Decorating Functions with Parameters #########################
#
# ### The above decorator was simple and it only worked with functions that did not have any parameters.
# ### What if we had functions that took in parameters like below.
#
# def divide(a, b):
#     return a/b
#
# ### This function has two parameters, a and b. We know it will give an error if we pass in b as 0.
# ### Now let's make a decorator to check for this case that will cause the error.
# ### When we call the divide() function with the arguments (2,0), the inner() function checks that b is equal to 0 and prints an error message before returning None.
# ### Hence, in this way , we are adding functionality to our original function.
# ### You can observe that we can add this functionality directly within the originak function. But decorator is a good way to do thus.
#
# def smart_divide(func):
#     def inner(a, b):
#         print("I am going to divide", a, "and", b)
#         if b == 0:
#             print("Whoops! cannot divide")
#             return
#
#         return func(a, b)
#     return inner
#
# @smart_divide
# def divide(a, b):
#     print(a/b)
#
# divide(2,5)
#
# divide(2,0)
#
### To generalize this parameters thing, we can do as below.

# def mydecoraator(func):
#     def wrapper(*args,**kwargs):
#         print('I am decorating.')
#         value = func(*args,**kwargs)
#         return value
#     return wrapper
# @mydecoraator
# def Hello(Person):
#     print(f'Hello {Person}')
#
# Hello('Mike')

#         ###################### Chaining Decorators in Python  ############################
#
# ### Multiple decorators can be chained in Python.
# ### To chain decorators in Python, we can apply multiple decorators to a single function by placing them one after the other, with the most inner decorator being applied first.
# ### Hence, percent decorateor is being called first due to inner most decorator then star decorator.
#
# def star(func):
#     def inner(*args, **kwargs):
#         print("*" * 15)
#         func(*args, **kwargs)
#         print("*" * 15)
#     return inner
#
#
# def percent(func):
#     def inner(*args, **kwargs):
#         print("%" * 15)
#         func(*args, **kwargs)
#         print("%" * 15)
#     return inner
#
#
# @star
# @percent
# def printer(msg):
#     print(msg)
#
# printer("Hello")

### Practical Example: 1

# def logged(func):
#     def wrapper(*args,**kwargs):
#         value = func(*args,**kwargs)
#         fname = func.__name__
#         with open('logfile.txt','a+') as f:
#             print(f'{fname} added to {value}')
#             f.write(f'{fname} added to {value}')
#         return value
#     return wrapper
#
# @logged
# def Hello(x,y):
#     return x+y
#
# print(Hello(10,20))


############################################## Generators #######################################################

### A generator is a just function that returns an iterable object which we can iterate over (one value at a time).
### Moreover, a generator function has one main difference from a regular function. It has a yield statement instead of a return statement in a regular function.
### To build an iterator in Python you should do a lot of work. You have to implement a class with __iter__ and __next__ magic method, keep track of internal states and raise StopIteration when there are no values to be returned.
### A generator is a very simple way to create an iterator because a generator does all of these steps automatically.


                           ################ 1. Create Generator ######################

### A function becomes a generator function if it contains at least one yield statement (it may contain several yield and even return).
### To make it clear, yield and return return some values from a function. So, you just have to build function with at least oneyield
### The main difference is that return statement terminates a function entirely while yieldstatement pauses a function saving all its states and later continues from there on successive calls.


             ################# 2.Generator Function Vs Regular Function  ######################

### A generator function includes one or more yield statements.
### It returns an iterator object but does not execute immediately.
### Methods such as__iter__() and __next__() are implemented automatically. It means that we can iterate through the items using next().
### Once the function yields, it is paused and the control is handed over to the caller.
### Local variables and their states are memorized between successive calls.
### When A generator function finishes, StopIteration is raised automatically on further calls.
### An interesting thing to notice is that the value of the variable num is memorized between every call.
##3 Unlike regular functions, the local variables are not destroyed when the function yields. Furthermore, a generator object can only be iterated one time.
### To start the process again, you have to create another a generator object using something like gen = simple_generator().
### The last point to notice is that you can use generators with for loops directly.
### This is because a for loop takes an iterator and iterates over it using a next() function. It automatically ends when StopIteration is raised.


# def simple_generator():
#     num = 1
#     print(f"{num} -- This is first")
#     yield num
#
#     num += 1
#     print(f"{num} -- This is second")
#     yield num
#
#     num += 1
#     print(f"{num} -- This is third and the last")
#     yield num
#
#
# gen = simple_generator()
# next(gen)
# next(gen)
# next(gen)
# next(gen)


                           #################  3. Generator With a Loop  ###################

### The above example makes no sense and I showed it just to you understand the work process of a generator.
### Typically, generator functions are implemented with a loop having a suitable termination condition.

# def reverse_string(string):
#     length = len(string)
#     for el in range(length - 1, -1, -1):
#         yield string[el]
#
#
# for word in reverse_string("hello"):
#     print(word)


                   ######################### 4. Generator Expression ########################

### Simple generators can be easily created using generator expressions. This helps to build generators easily.
### Similar to the lambda functions which create anonymous functions, generator expressions create anonymous generator functions.
### The syntax for the generator expression is similar to that of list comprehension. However, the square brackets are replaced with round parentheses.
### The major difference between a list comprehension and the generator expression is that a list comprehension produces the whole list whereas the generator expression produces one item at a time.

# list_numbers = [10, 18, 13, 23]
#
# list_square = [x**2 for x in list_numbers]
# generator = (x**2 for x in list_numbers)
#
# print(list_square)
# print(generator)
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# next(generator)

                     ##################### 5. Use of Generator ###################

#### There are several reasons why generators are powerful to implement.
#### Easy to Implement : Generators can be implemented clearly and concisely as compared to their iterator class counterpart.
### Below is an example of an implementation of a 2 power sequence using an iterator class.
### Maybe we can create batch using generator.


# class PowTwo:
#     def __init__(self, max=0):
#         self.number = 0
#         self.max = max
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.number > self.max:
#             raise StopIteration
#         result = 2 ** self.number
#         self.number += 1
#         return result

### The code above was long and confusing. Now, let’s do the same using a generator function.

# def pow_two_generator(maximum=0):
#     number = 0
#     while number < maximum:
#         yield 2**number
#         number += 1
#         assert number < maximum, f'You have reached your maximum limit of value {number}'
# gen = pow_two_generator(maximum = 3)
#
# print(next(gen))
# print(next(gen))
# print(next(gen))
# # print(next(gen))


             ###################### 5.2. Memory Efficient #################################

### A regular function to return a sequence is going to create the whole sequence in memory before returning the result. This is overkill if the number of items in the sequence is very large.
### A generator implementation of such sequences is memory friendly and is preferable because it only produces one item at a time.
### Let's see an example:

# def my_generator_function(n):
#     for i in range(n):
#         yield i
#
# def my_regular_function(n):
#     result = []
#     for i in range(n):
#         result.append(i)
#     return result
#
# from memory_profiler import profile
#
# @profile
# def test_generator():
#     # Call the generator and iterate through the items
#     result = my_generator_function(1000000)
#
#
# @profile
# def test_regular_function():
#     # Call the regular function and store the result in a variable
#     result = my_regular_function(1000000)
#
# test_generator()
# test_regular_function()



                 #################  5.3. Represent Infinite Stream  ###################

### A generator is an excellent medium to represent an infinite flow of data. Infinite flows can’t be stored in memory, and since generators produce only one item at a time, they can represent an infinite stream of data.

# def all_even():
#     number = 0
#     while True:
#         yield number
#         number += 2


                  ###################### 5.4. Pipelining Generators ########################

### Multiple generators can be used to pipeline a series of operations. This is best illustrated with one example.
### Let’s say you have a generator that produces the numbers in the Fibonacci series. And we have another generator for squaring numbers.
### If we want to find out the sum of squares of numbers in the Fibonacci series, we can do it in the following way by pipelining the output of a generator's functions together.

# def fibonacci_numbers(numbers):
#     x, y = 0, 1
#     for _ in range(numbers):
#         x, y = y, x + y
#         yield x
#
#
# def square(numbers):
#     for num in numbers:
#         yield num ** 2
#
#
# print(sum(square(fibonacci_numbers(30))))


############################################ Argument Parsing ####################################################

### It helps to run your code from command line (or terminal) Every programming language has a feature to create scripts and run them from the terminal or being called by other programs. When running such scripts we often need to pass on arguments needed by the script for various functions to be executed inside the script.
### Every programming language has a feature to create scripts and run them from the terminal or being called by other programs. When running such scripts we often need to pass on arguments needed by the script for various functions to be executed inside the script.
### Using sys.argv : This is a inbuilt module sys.argv can process arguments that are passed on with the script.
### By default the first argument which is considered at sys.argv[0] is the file name. the rest of the arguments are indexed as 1,2 and so on. In the below example we see how a script uses the arguments passed onto it.
### With correct directory, we use : python main.py Usqama , to run this.

import sys
# print(sys.argv[0])
# print("Hello ",sys.argv[1],", welcome!")


### To give undefined number of arguments (means list of arguments) , we can do the following.
### In actual, sys. argv is a list in Python that contains all the command-line arguments passed to the script.


#print(sys.argv)                       ### python main.py Usama Hassan 10 Majeed


### To open file with text and filename as arguments, we can do the following.

# filename = sys.argv[1]
# message = sys.argv[2]
#
# with open(filename,'w+') as f:
#     print(f'Your message {message} has been saved!')
#     f.write(message)


### Using argparse: There is a library called argparse that includes a lot more functionality to do with argument parsing and it’s already included in the Python Standard Library (so you don’t need to worry about installing it)! This library contains the .ArgumentParser() method which allows you to create a parser object that will do the actual parsing of arguments (importing values from the command-line).
### Once that’s done you will need to use the parser object’s .add_argument() method to add an argument and, finally, its .parse_args() method will be needed to actually parse the arguments. In other words, you need to do at least these three things in your script:
### Step:1 : Import the argparse library and Create the parser object with argparse.ArgumentParser()
### Step:2 : Use the parser object to add arguments with parser.add_argument()
### Step:3 : Use the parser object to parse the arguments with parser.parse_args()
### The text "The World says 'Hello' back" has been passed into the script from the command-line as an argument called message and saved as the variable args.message.
### This is how a user can control what a script does; in this case we decided what message was printed without editing the code itself.
### This is an example of a positional argument because it works by assigning the value of the first argument that appears on the command-line to the variable “message”.
### If we had added a second positional argument with parser.add_argument('recipient') then the second argument on the command-line would have been assigned to the variable “recipient”.
### These are positional arguments because their position (order) on the command-line determines which variable name they get assigned to. A positional argument is also a required argument by default; if it is omitted it will create an error.

### Usage : python main.py 'Usama Hassan'

import argparse

# # Create command-line argument parser
# parser = argparse.ArgumentParser()
# # Add positional argument
# parser.add_argument('message')
# # Parse arguments from terminal
# args = parser.parse_args()
#
# # Access the arguments
# message = args.message
# print(message)

### Similarly, we have optional arguments too.
### Alternatively, you can create optional arguments by using flags. These are, as the name suggests, optional and will not cause the script to crash if they are omitted.
### When the name of an argument starts with a dash it will automatically be interpreted as an optional argument and, within the programming world, argument names that start with a dash are known as “flags”:
### Note also that optional arguments need the flag to be included when called. This is different from positional arguments where the name of the variable is not included and instead their positions are used to determine which argument is assigned to which variable.
### By convention, flags that start with two dashes are the full names of the arguments while flags that start with only one dash are the shorthand versions of those names.
### Here’s a script that defines three optional arguments (message, recipient and extra):
### Note that we can pass long form of flag also e.g., python main.py --message 'Usama'

### Usage: python main.py -m 'Usma' -r 'Hassna'  or python main.py -m 'Usama' and so on.


# Create command-line argument parser
# parser = argparse.ArgumentParser()
# # Add optional arguments
# parser.add_argument('--message', '-m')
# parser.add_argument('--recipient', '-r')
# parser.add_argument('--extra', '-e')
# # Parse arguments from terminal
# args = parser.parse_args()
#
# # Access the arguments
# message = args.message
# print(message)
# recipient = args.recipient
# print(recipient)


### Similarly, we can set default values also.
### Sets a default value for an optional argument. In other words, if the argument is omitted, this is the value that the variable will take, for example:
### Parse like this: parser.add_argument('--colour', '-c', default='blue')
### will cause the variable colour to have the value “blue” if it is not specified in the call.



### Similarly, we can set types of arguments also.
### All arguments are parsed as strings, unless this keyword argument is used to convert them to another type:
### Using this:   parser.add_argument('integer', type=int)
### The above will cause the inputted argument to be converted to an integer. The other common type option is float. If you are trying to parse a multi-element object such as a list, you will probably want to use the nargs='*' keyword argument discussed below rather than doing type=list. While the latter will work in the sense that it won’t cause an error, it will convert your single-string input argument into a list of its characters which probably isn’t what you want to do.
### Note that it’s not recommended to use type=bool to convert inputs to Booleans because it will consider all non-empty strings to be True and the empty string to be False. In other words, “False” will be evaluated as True, which is not something you want your code to be able to do.


### More info on argument Parsing:  https://rowannicholls.github.io/python/advanced/argument_parsing.html



########################################### Encapsulation #######################################################

### Data hiding : encapsulation. Make your attributes private but we can read them through getters and write through setters method.
### We make attributes private using __ like self.__name ,etc. We make getter method use @property decorator and @functionName.setter for setter method.

# class Person:
#     def __init__(self,name,age,height):
#         self.__name = name
#         self.__age = age
#         self.height = height
#
#     @property
#     def Name(self):
#         return self.__name
#
#     @Name.setter
#     def Name(self,value):
#         self.__name = value
#
# p1 = Person('Usama',25,6)
# print(p1.Name)
# p1.Name = 'Bob'
# print(p1.Name)

######################################### Type Hinting #########################################################

# def hello(param):
#     assert type(param) == int, f'Type of param is {type(param)} but not int'
#     print(param)
#
# hello(10)

# def type_check(func):
#     def wrapper(param):
#         assert type(param) == int , f'Your parameter type is {type(param)} but not int.'
#         func(param)
#         return func
#     return wrapper
#
# @type_check
# def hello(param):
#     print(param)
#
# hello(10)

