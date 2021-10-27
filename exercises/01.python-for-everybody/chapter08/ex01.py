# Exercise 1: Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None. Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

cars = ['kadett', 'chevette', 'gol'];

def chop(cars):
	last_element = len(cars) - 1;
	cars = cars[1:last_element];

print(chop(cars))

# ----------------------------

motorcycles = ['mt09', 'tigger', 'cb600'];

def middle(motorcycles):
	last_element = len(motorcycles) - 1;
	return motorcycles[1:last_element];

print(middle(motorcycles))