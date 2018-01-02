map = open('19.txt').readlines()

# find start point
row = 0
col = 0
for i in range(len(map[row])):
	c = map[0][i]
	if c == '|':
		col = i
		break
print("start at (" + str(row) + ", " + str(col) + ")")

dir = (1, 0)
steps = 0
while row in range(len(map)) and col in range(len(map[row])):
	c = map[row][col]
	if c in ['|', '-']:
		pass # ignore
	elif c == ' ':
		break
	elif c == '+':
		#print("+ at (" + str(row) + ", " + str(col) + ")")
		for nei in [(-1,0,'|'),(0,1,'-'),(1,0,'|'),(0,-1,'-')]:
			if nei[0] == -dir[0] and nei[1] == -dir[1]: 
				continue
			nei_row, nei_col = row + nei[0], col + nei[1]
			if nei_row not in range(len(map)) or nei_col not in range(len(map[nei_row])): 
				continue
			nei_c = map[nei_row][nei_col]
			if nei_c == nei[2] or nei_c == '+' or nei_c.isalnum():
				dir = (nei[0], nei[1])
				break
	else:
		print(c)
	row, col = row + dir[0], col + dir[1]
	steps += 1

print("done")
print("took " + str(steps) + " steps")
