import math

lengths = [ord(c) for c in "106,16,254,226,55,2,1,166,177,247,93,0,255,228,60,36"]
lengths += [17, 31, 73, 47, 23]
numbers = [x for x in range(256)]
loc = 0
skip = 0
hex_string = ""

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
	hex_string += format(xor, "02x")

print(numbers)
print(str(numbers[0]) + " * " + str(numbers[1]) + " = " + str(numbers[0]*numbers[1]))
print("Knot Hash is " + hex_string)