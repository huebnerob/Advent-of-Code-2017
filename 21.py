import matrix_utils

def equiv(m):
	if len(m) == 2:
		equivs = equiv_2(m)
	elif len(m) == 3:
	 	equivs = equiv_3(m)
	else:
		raise Exception("invalid size")
	deduped = []
	for eq in equivs:
		if eq not in deduped:
			deduped += [eq]
	return deduped

def rotate_2(m):
	return [[m[1][0], m[0][0]], [m[1][1], m[0][1]]]

def flip_2(m):
	return [[m[0][1], m[0][0]], [m[1][1], m[1][0]]]

def equiv_2(m):
	rotations = []
	for _ in range(4):
		rotations += [m]
		m = rotate_2(m)
	rots_and_flips = []
	for r in rotations:
		rots_and_flips += [r, flip_2(r)]
	return rots_and_flips

def rotate_3(m):
	return [[m[2][0], m[1][0], m[0][0]], [m[2][1], m[1][1], m[0][1]], [m[2][2], m[1][2], m[0][2]]]
	
def flip_3(m):
	return [[m[0][2], m[0][1], m[0][0]], [m[1][2], m[1][1], m[1][0]], [m[2][2], m[2][1], m[2][0]]]

def equiv_3(m):
	rotations = []
	for _ in range(4):
		rotations += [m]
		m = rotate_3(m)
	rots_and_flips = []
	for r in rotations:
		rots_and_flips += [r, flip_3(r)]
	return rots_and_flips


input = open('21.txt').readlines()
rules = {}

for line in input:
	rule = [[[1 if c == '#' else 0 for c in l] for l in grid.split("/")] for grid in line.strip().split(" => ")]
	equiv_triggers = equiv(rule[0])
	#print('rule\n')
	#print_m(rule[1])
	#print("has these triggers: \n")
	for eq in equiv_triggers:
		rules[str(eq)] = rule[1]
		#print_m(eq)

def sub_m(m, row, col, size):
	return [row[col:col+size] for row in m[row:row+size]]

def part_m(m, size, replacer):
	new = []
	for row in range(0, len(m), size):
		for col in range(0, len(m[row]), size):
			m_sub = sub_m(m, row, col, size)
			new_m_sub = replacer(m_sub)
			if col == 0: # new rows, simple append
				new += [row[:] for row in new_m_sub] # copy from rule
			else: # add to existing rows
				for new_row in range(len(new_m_sub)):
					new_row_i = len(new) - len(new_m_sub) + new_row
					new[new_row_i] += new_m_sub[new_row]
	return new

def replace_m(m_r):
	replacement = rules[str(m_r)]
#	print("replacement for ")
#	print_m(m_r)
#	print("\nis")
#	print_m(replacement)
	return replacement
	
fractal = [[0,1,0],[0,0,1],[1,1,1]]	
# print_m(fractal)
iterations = 18

for iter in range(iterations):
	l = len(fractal)
	if l % 2 == 0:
		fractal = part_m(fractal, 2, replace_m)
	elif l % 3 == 0:
		fractal = part_m(fractal, 3, replace_m)
	else:
		raise Exception("invalid fractal size")
	#print_m(fractal)
	print("finished iteration " + str(iter + 1))

# count ones
sum = 0
for row in fractal:
	for col in row:
		sum += col
print("fractal has " + str(sum) + " ones after " + str(iterations) + " iterations")

# 117 is too low but is the right answer for someone else?

"""
for match in rules:
	replacement = rules[match]
	print("for this match")
	print(match)
	print("replace with this")
	print_m(replacement)

test = [[str(row) + ":" + str(col) for col in range(4)] for row in range(4)]
print_m(test)
print_m(sub_m(test,0,2,2))

def replace(m):
	size = len(m)
	size += 1
	return [[size for _ in range(size)] for _ in range(size)]

test = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
print_m(test)
print_m(part_m(test, 2, replace))
"""
