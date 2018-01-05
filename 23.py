text = open('23.txt').readlines()
instructions = []
for line in text:
	ins = line.strip().split(' ')
	if ins[2].isalpha():
		ins[2] = lambda: mem[ins[2]]
	else:
		int_val = int(ins[2])
		ins[2] = lambda: int_val
	instructions += [ins]
i = 0
mem = {}
for r in 'abcdefg':
	mem[r] = 0
mem['1'] = 1 # lol hax
while i in range(len(instructions)):
	expr = instructions[i]
	
