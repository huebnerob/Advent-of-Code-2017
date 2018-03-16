# the program is formatted as simple values
# states are zero-indexed from A=0 to F=5
# each line represents a state-value, with parameters:
# 	0. value to write
# 	1. direction to move after (left = -1, right = +1)
# 	2. state to execute following
# to find the next parameters to use:
# i = current_state * 6 + 3 * current_value
# write, move, state = prgm[i], prgm[i+1], prgm[i+2]

state = 0
halt_at = 12425180
prgm = [
	1, +1, 1,	# a 0
	0, +1, 5,	# a 1
	0, -1, 1,	# b 0
	1, -1, 2,	# b 1
	1, -1, 3,	# c 0
	0, +1, 2,	# c 1
	1, -1, 4,	# d 0
	1, +1, 0,	# d 1
	1, -1, 5,	# e 0
	0, -1, 3,	# e 1
	1, +1, 0,	# f 0
	0, -1, 4,	# f 1
]

memory = [0 for i in range(halt_at)]
pos = int(len(memory)/2)

print('starting program...')

for t in range(halt_at):
	if t % int(halt_at/100) == 0:
		print("at t=" + str(t))
	i = state * 6 + 3 * memory[pos]
	write, move, state = prgm[i], prgm[i+1], prgm[i+2]
	memory[pos] = write
	pos += move

print("memory checksum: " + str(sum(memory)))
