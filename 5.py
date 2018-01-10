input = open("5.in")

instructions = []
for line in input:
	instructions += [int(line)]
print("parsed " + str(len(instructions)) + " instructions")

location = 0
ticks = 0
while location in range(0, len(instructions)):
	move = instructions[location]
	instructions[location] += 1 if move < 3 else -1 
	location += move
	ticks += 1
print("moved " + str(ticks) + " times before going out of bounds")
	