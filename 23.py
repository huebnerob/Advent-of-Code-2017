text = open('23.txt').readlines()
instructions = []
for line in text:
	ins = line.strip().split(' ')
	if ins[2].isalpha():
		reg = ins[2]
		ins[2] = lambda: mem[reg]
	else:
		int_val = int(ins[2])
		ins[2] = lambda: int_val
	instructions += [ins]
i = 0
mem = {}
for r in 'abcdefg':
	mem[r] = 0
mem['1'] = 1 # lol hax
muls = 0
while i in range(len(instructions)):
	expr = instructions[i]
	i_del = 1
	if expr[0] == 'set':
		mem[expr[1]] = expr[2]()
	elif expr[0] == 'sub':
		mem[expr[1]] -= expr[2]()
	elif expr[0] == 'mul':
		mem[expr[1]] *= expr[2]()
		muls += 1
	elif expr[0] == 'jnz':
		if mem[expr[1]] != 0:
			i_del = expr[2]()
	else:
		raise Exception('invalid command')
	i += i_del

print('finished processing!')
print('encountered ' + str(muls) + ' muls')
	
