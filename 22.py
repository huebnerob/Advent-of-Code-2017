from matrix_utils import print_m

text = open('22.txt').readlines()

grid = []
for line in text:
	row = []
	for c in line.strip():
		row += [1 if c == '#' else 0]
	grid += [row]

'''
grid = [[0 for _ in range(9)] for _ in range(9)]
grid[4][3] = 1
grid[3][5] = 1
#'''

print_m(grid)

row = int(len(grid)/2)
col = int(len(grid)/2)
print("starting at " + str(row) + " " + str(col))
iterations = 10000000
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
curr_dir = 0
infections = 0
expansions = 0

for i in range(iterations):
	if grid[row][col] == 1: # infected
		curr_dir += 1 # turn right
		grid[row][col] = 7 # become flagged
	elif grid[row][col] == 5: # weakened
		curr_dir += 0 # dont turn
		grid[row][col] = 1 # become infected
		infections += 1
	elif grid[row][col] == 7: # flagged
		curr_dir += 2 # turn around
		grid[row][col] = 0 # become clean
	else: # clean
		curr_dir -= 1 # turn left
		grid[row][col] = 5 # become weakened
	
	curr_dir %= len(directions)
	delta = directions[curr_dir]
	row, col = row + delta[0], col + delta[1]
	
	# expand grid if necessary
	if row < 0:
		grid.insert(0, [0 for _ in range(len(grid[0]))])
		row += 1
		expansions[0] += 1
	if row >= len(grid):
		grid += [[0 for _ in range(len(grid[0]))]]
		expansions[1] += 1
	if col < 0:
		for r in grid:
			r.insert(0, 0)
		col += 1
		expansions[2] += 1
	if col >= len(grid[row]):
		for r in grid:
			r += [0]
		expansions[3] += 1
			
	if i % int(iterations/100) == 0:
		print("done with iteration " + str(i) + ", expanded " + str(expansions) + " times") 
		expansions = [0, 0, 0, 0]
		

print("after " + str(iterations) + " iterations: \n")
#print_m(grid)
print(str(infections) + " infections occurred")
