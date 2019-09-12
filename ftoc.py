import sys

print('What is the value in Fahrenheit?', sys.argv[1])

tempF = int(sys.argv[1])

print((tempF - 32) * 5 / 9)