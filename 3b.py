input = 312051
directions = [[1, 0], [0, 1], [-1, 0], [0, -1]] # right, up, left, down
neighbors = [[x, y] for x in [-1, 0, 1] for y in [-1, 0, 1]]
neighbors.remove([0,0])
print(neighbors)

def lengths_for(spiral): 
	s_len = 2*spiral
	return [s_len-1, s_len-1, s_len, s_len]

array_size = 13
v = []
for _ in range(0, array_size):
	v += [[0 for _ in range(0, array_size)]]

x = int(array_size/2)
y = int(array_size/2)
v[x][y] = 1
spiral = 1
direction = directions[0]
lengths = lengths_for(spiral)
first_biggest = None
print("starting at [" + str(x) + ", " + str(y) + "]")
while x in range(1, array_size-2) and y in range(1, array_size-2):
	x += direction[0]
	y += direction[1]
	nei_sum = sum([v[x+n[0]][y+n[1]] for n in neighbors])
	v[x][y] = nei_sum
	if nei_sum > input:
		first_biggest = nei_sum
		break
	lengths[0] -= 1
	if lengths[0] == 0:
		lengths.pop(0)
		directions.pop(0)
		if len(lengths) == 0:
			spiral += 1
			lengths = lengths_for(spiral)
			directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
		direction = directions[0]

print('finished grid')
for line in v:
	print("\t".join([str(num) for num in line]))
print('found first value higher than ' + str(input) + ' is ' + str(first_biggest))