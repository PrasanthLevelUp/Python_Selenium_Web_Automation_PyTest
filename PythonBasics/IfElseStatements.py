a = 10
b = 20
age = 45
num = 0

# if..else statement
if a < b:
    print('a is smallest')
else:
    print('b is smallest')

# nested if statement

if age > 18:
    print("he is eligible")
    if age > 45:
        print("senior citizen")
else:
    print('not eligible for voting')

# else if statement

if num >0:
    print('number is positive')
elif num ==0:
    print("zero")
else:
    print('negative number')