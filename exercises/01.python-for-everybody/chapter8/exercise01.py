# Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None. 

def chop(array):
	array.pop()
	array.pop(0)

first_array = [1,2,3,4,5]

print('First array before:', first_array)
result = chop(first_array)
print("Result: ", result)
print('First array after:', first_array)

print('\n----------\n')

# Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

def middle(array):
	last_element = len(array) - 1
	return array[1:last_element]

second_array = [1,2,3,4,5]
print("Second array before:", second_array)
second_result = middle(second_array)
print("Second result:", second_result)
print("Second array after:", second_array)
