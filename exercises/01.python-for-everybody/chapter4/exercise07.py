try:
	score=float(input("Enter a number between 0.0 and 1.0: "))
	grade=None

	def computegrade(sc):
		if sc >= 0.9:
			grade="A"
		elif sc >= 0.8:
			grade="B"
		elif sc >= 0.7:
			grade="C"
		elif sc >= 0.6:
			grade="D"
		else:
			grade="F"

		return grade

	if score < 0 or score > 1:
		print("Bad score!")
	else:
		result=computegrade(score)
		print(result)
except:
	print("Bad score!")