"""
Python Functions
def function_name(parameters):
statement(s) """


Creating a Function
def add():
    a = 10
    b = 20
    c = a + b
    print(c)


# Calling a Function
add()


# Arguments, Number of Arguments
def add_arg(a, b):
    c = a + b
    print(c)


add_arg(2, 6)
add_arg(1000, 5000)


# Return value
def add_arg_retu(a, b):
    c = a + b
    return c


result = add_arg_retu(2, 4)
print(result)


# Default Parameter Value
def add_arg_retu(a =0, b= 1):
    c = a + b
    return c

result1 = add_arg_retu()
print(result1)