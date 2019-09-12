import sys

# What does end='' do in the print statements?
# Respond here: Combines the print outputs into one line.
print('Hello, ', end='')
print(sys.argv[1]+ ',', sys.argv[2]+ ', and', sys.argv[3], end='')
print('! Welcome.')

# To run this code: python3 hello.py Abraham