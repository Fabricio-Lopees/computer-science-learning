# Exercise 4: Assume that we execute the following assignment statements:
# width = 17
# height = 12.0
# For each of the following expressions, write the value of the expression and the type (of the value of the expression).
# 1. width//2
# 2. width/2.0
# 3. height/3
# 4. 1 + 2 * 5

width = 17;
height = 12.0;

one = width//2; # result: 8 - type: int
two = width/2.0; # result: 8.5 - type: float
three = height/3; # result: 4.0 - type: float
four = 1 + 2 * 5; # result: 11 - type: int

print(four, type(four))