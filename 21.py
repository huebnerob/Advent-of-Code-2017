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

def print_m(m):
	for l in m:
		l_s = [str(e) for e in l]
		print(' '.join(l_s))
	print()


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

def proc_3(f):
	return rules[str(f[0:3][0:3])]

def proc_4(f):
	return f

def sub_m(m, row, col, size):
	return [row[col:col+size] for row in m[row:row+size]]
	
fractal = [[0,1,0],[0,0,1],[1,1,1]]	
print_m(fractal)

for iter in range(10):
	l = len(fractal)
	if l % 3 == 0:
		fractal = proc_3(fractal)
	elif l % 4 == 0:
		fractal = proc_4(fractal)
	else:
		raise Exception("invalid fractal size")
	print_m(fractal)
	
test = [[str(row) + ":" + str(col) for col in range(4)] for row in range(4)]
print_m(test)
print_m(sub_m(test,0,2,2))
