import sys

input = open('16.txt').read().split(",")

letters = list("abcdefghijklmnop")
original = list("abcdefghijklmnop")
danced = list("ionlbkfeajgdmphc")

def spin(n):
	global letters
#	print('spinning by ' + str(n))
	letters = letters[-n:] + letters[:-n]	

def exchange(a, b):	
	global letters
#	print('exhanging position ' + str(a) + " with position " + str(b))
	letters[a], letters[b] = letters[b], letters[a]

def swap(a, b):
#	print('swapping programs ' + a + " and " + b)
	a_i = letters.index(a)
	b_i = letters.index(b)
	exchange(a_i, b_i)

encountered = set()

print('starting parse...')
for i in range(1000):
	#if i % 10 == 0:
	#	sys.stdout.write('.')		
	for move in input:
		if move[0] == 's': # spin
			spin(int(move[1:]))
		elif move[0] == 'x': # exchange
			pos = [int(n) for n in move[1:].split('/')]
			exchange(pos[0], pos[1])
		elif move[0] == 'p': # partner
			progs = move[1:].split('/')
			swap(progs[0], progs[1])
	#	print("--> " + str(letters))

	# print("".join(letters))
	string = "".join(letters)
	if string in encountered:
		print(string + " is already added")
	else:
		print("adding " + string)
		encountered.add(string)

print("found " + str(len(encountered)) + " unique arrangements")
"""
pos_moves = []
for i in range(len(danced)):
	c = danced[i]
	new_i = original.index(c)
	pos_moves += [new_i]

new_l = []
iter = 0
for _ in range(1000):
	for m in pos_moves:
		new_l += [letters[m]]
	letters = new_l
	new_l = []
	iter += 1
	print(str(iter) + " : " + "".join(letters))
"""
