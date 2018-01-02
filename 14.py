import math

input = "uugsqrei"
#input = "flqrgnkx"

print('starting hashing with input: ' + input)

def knot_hash_binary(string):
	lengths = [ord(c) for c in string]
	lengths += [17, 31, 73, 47, 23]
	numbers = [x for x in range(256)]
	loc = 0
	skip = 0
	bin_string = ""
	
	def do_swaps(loc, length, array):
		for i in range(math.floor(length/2)):
			start = (loc + i) % len(array)
			end = (loc + length - 1 - i) % len(array)
			array[start], array[end] = array[end], array[start]
	
	for _ in range(64):
		for length in lengths:
			do_swaps(loc, length, numbers)
			loc += length + skip
			skip += 1
	
	for b in range(16):
		xor = 0
		for n in range(16):
			i = 16*b+n
			xor = numbers[i] ^ xor
		bin_string += format(xor, "08b")
	return bin_string

total_bits = 0
matrix = []
for i in range(128):
	hash = knot_hash_binary(input + "-" + str(i))
	print(hash[0:80] + "...")
	vals = [int(c) for c in hash]
	matrix += [vals]
	bits_in_hash = sum(vals)
	total_bits += bits_in_hash

print("total bits used is " + str(total_bits))

def process_node(i, j):
	if not i in range(len(matrix)) or not j in range(len(matrix[i])):
		return 0
	if matrix[i][j] == 0:
		return 0
	matrix[i][j] = 0
	for d in [(1,0), (-1,0), (0,1), (0,-1)]:
		d_i, d_j = d[0], d[1]
			#print(str(i) + " + " + str(d_i) + ", " + str(j) + " + " + str(d_j))
		process_node(i+d_i, j+d_j)
	return 1

groups = 0
for i in range(len(matrix)):
	for j in range(len(matrix[i])):
		# print('processing ' + str(i) + " " + str(j))
		groups += process_node(i, j)
	
print("found a total of " + str(groups) + " groups")
