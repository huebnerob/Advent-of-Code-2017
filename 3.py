input = 312051

print(input)

# 	17	16	15	14	13
#	18	5	4	3	12	
# 	19	6	1	2	11
# 	20	7	8	9	10
# 	21	22	23	24	25	

# the edge lengths of the straight components of the spiral increase 1 every 2 sides
# 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6
# order of directions is right, up, left, down
# number after spiral N is 2*sum(1,2*N)

spirals = 0
location = 1
while location < input:
	spirals += 1
	location += (8 * spirals) - 2
	print("location after spiral " + str(spirals) + " is " + str(location))	
print("input is within spiral " + str(spirals))
l_x = -spirals
l_y = -spirals
print("starting at [" + str(l_x) + ", " + str(l_y) + "], positioning within spiral")
directions = [[0, 1], [1, 0], [0, -1], [-1, 0]] # up, right, down, left
s_len = (2 * spirals)
lengths = [s_len, s_len, s_len-1, s_len-1]
while location > input:
	location -= 1
	lengths[0] -= 1
	d = directions[0]
	l_x += d[0]
	l_y += d[1]
	if lengths[0] == 0:
		print("switching directions")
		lengths.pop(0)
		directions.pop(0)
print("positioning complete, found " + str(input) + " at [" + str(l_x) + ", " + str(l_y) + "]")
distance = abs(l_x) + abs(l_y)
print("manhattan distance is " + str(distance))