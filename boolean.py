import sys

#Problem 1
num = int(sys.argv[1])

answer = num % 10

print(answer <= 2 or answer >= 8)

#Problem 2
num1 = int(sys.argv[2])
num2 = int(sys.argv[3])

answer = num1 % num2

print(answer == 0)

#Problem 3
year = int(sys.argv[4])

answer = year % 4
hundred = year % 100
fourhundred = year % 400

print(answer == 0 and ((not hundred == 0) or fourhundred == 0))

#Problem 4
temp = int(sys.argv[5])
is_summer = int(sys.argv[6])
# has to be int not bool, because sys.argv gives a string so it can't register between True or False

print(bool(((60 <= temp <= 90) and is_summer == False) or ((60 <= temp <= 100)and is_summer == True)))





