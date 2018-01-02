str = open('21.txt').readlines()
rules = []

for line in str:
	rule = [grid.split("/") for grid in line.strip().split(" => ")]
	rules += [rule]
	print(rule)
