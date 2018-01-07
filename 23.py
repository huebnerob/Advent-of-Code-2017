import math

text = open('23.txt').readlines()
#output = open('23-out.txt', 'w')
instructions = []
for line in text:
	ins = line.strip().split(' ')
	instructions += [ins]

# shortcut
# program effective result:
# count the composite numbers between 106500 and 123500

def is_composite(val):
	for i in range(2, int(math.sqrt(val)) + 1):
		if val % i == 0:
			return True
	return False

composites = 0
start = 106500
end = 123500
step = 17
for val in range(start, end + 1, step):
	print("checking " + str(val))
	if is_composite(val):
		composites += 1
	else:
		print(str(val) + " is prime")

print("found " + str(composites) + " composites every " + str(step) + "th value between " + str(start) + " and " + str(end))

i = 0
mem = {}
for r in 'abcdefgh':
	mem[r] = 0
mem['1'] = 1 # lol hax
mem['a'] = 1 # turn off debug mode
muls = 0
while i in range(len(instructions)):
	expr = instructions[i]
	if expr[2].isalpha():
		val = mem[expr[2]]
	else:
		val = int(expr[2])
	#output.write("[" + str(i+1) + "]: executing instruction: " + str(expr) + " with val " + str(val) + "\n")
	i_del = 1
	if expr[0] == 'set':
		mem[expr[1]] = val
	elif expr[0] == 'sub':
		mem[expr[1]] -= val
	elif expr[0] == 'mul':
		mem[expr[1]] *= val
		muls += 1
	elif expr[0] == 'jnz':
		if mem[expr[1]] != 0:
			i_del = val
	else:
		raise Exception('invalid command')
	#output.write("increasing i by " + str(i_del) + "\n")
	if expr[1] == 'h':
		print('accessed reg h --> ' + str(mem['h']))
	i += i_del

print('finished processing!')
print('encountered ' + str(muls) + ' muls')
	
