# Variables Demo
# 9/9/19
# Some basic examples of variables and math you can do with them

import math

ur = int(input("Hi there! Give me some data..."))
# good variable names: variable, name, x, y, z, xyz, number1, number2, zoo_keeper, camelCase
# bad variable names: print, True, input, =, #funtimes, asgdhggfsgdhggsfa, 123go, super awesome, COOL

x = 1
y = 2
z = 3

answer = x + y
print(answer) # 3

answer = x - z
print(answer) # -2

answer = answer * y
print(answer) # -4

answer = 4 / y
print(answer) # 2

answer = 5 // y
print(answer) # 2
#floored division

updated_user_response = ur + 1
print(updated_user_response)

answer = z % y # remainder
print(answer) # 1

answer = y ** 3 # exponent
print(answer) # 8

answer = math.sqrt(9)
print(answer) # 3



