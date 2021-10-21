# Exercise 7: Rewrite the grade program from the previous chapter using a function called computegrade that takes a score as its parameter and returns a grade as a string.

try:
	score = float(input('Enter score between 0.0 and 1.0: '));
except:
	print('Bad score!');
	exit()

def computegrade(score):
	if score < 0 or score > 1:
		result = 'Bad score!';
	elif score >= 0.9:
		result = 'A';
	elif score >= 0.8:
		result = 'B';
	elif score >= 0.7:
		result = 'C';
	elif score >= 0.6:
		result = 'D';
	else:
		result = 'F';
	return result;

result = computegrade(score);
print(result);