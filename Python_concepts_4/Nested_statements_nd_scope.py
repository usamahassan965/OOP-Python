### Scope is a concept that determines where you can see or access a variable.
### Local Vs Global
# x = 'outside'
#
# def report():
#     x = 'inside'
#     return x
#
#
# print(report())   ### Here x is referenced via local scope
# print(x)          ### Here x is referenced via global scope


######################## Scope Rule #####################
### Python has standard rule of 'LEGB' to try to figure out what you are actually referencing .
### Is it local , enclosing , global or built in.


### Local scope reference

# def report():
#     x = 'local'
#     print(x)

### Enclosing scope - Here python looks for local scope first which id inside function. It can't find x reference here.
### Then, it looks for enclosing level and it finds in enclosing function.
### But if we comment out that x = 'enclosing level' then python will look for global level.

# x = 'Global scope'
#
# def enclosing():
#     x = 'Enclosing level'
#     def inside():
#         print(x)
#     inside()
#
# enclosing()

### But if we comment x = 'Global scope' too then it will look for built in variable and returns Nameerror if it couldn't find any builtin variable.

##################### global keyword ##################

#### Global keyword gives global scope to the variable.

x = 'outside'

def report():
    # Globalize the variable x
    global x
    # Reassign global x from local level
    x = 'inside'
    return x

print(report())
print(x)

### Hence, the reassigning of x inside the report function ,after declaring x as global, will make this local scope x value as global defined.
### Hence, now x will be equal to 'inside' not 'outside'. But if we comment out global x then x = outside as global scope.
