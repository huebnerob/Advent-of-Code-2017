show_logs = 0
def log(message):
	if show_logs:
		print(message)

program = open('18.txt').readlines()
program = [[p.strip() for p in ins.split(' ')] for ins in program]

class Process():
	def __init__(self, p):
		self.i = 0
		self.memory = {'p': p, '1': 1}
		self.inbox = []
		self.linked = None
		self.sent = 0
		
	def evaluate(self):
		params = program[self.i]
		cmd = params[0]
		
		reg = params[1]
		if reg not in self.memory:
			self.memory[reg] = 0
		
		val = params[2] if len(params) > 2 else None
		if val in self.memory:
			val = self.memory[val]
		elif val:
			val = int(val)

		i_delta = 1
		
		if cmd == 'snd':
			log("sending value in " + reg)
			self.linked.inbox += [self.memory[reg]]
			self.sent += 1
		elif cmd == 'set':
			log("setting register " + reg + " to " + str(val))
			self.memory[reg] = int(val)
		elif cmd == 'add':
			log("adding " + str(val) + " to register " + reg)
			self.memory[reg] += val
		elif cmd == 'mul':
			log("multiplying " + str(val) + " to register " + reg)
			self.memory[reg] *= val
		elif cmd == 'mod':
			log("modulo " + str(val) + " to register " + reg)
			self.memory[reg] %= val
		elif cmd == 'rcv':
			if len(self.inbox) == 0:
				log("waiting for value...")
				return True
			log("receiving value into " + reg)
			self.memory[reg] = self.inbox.pop(0)
		elif cmd == 'jgz':
			log("jumping if " + reg + " greater than zero with offset " + str(val))
			if self.memory[reg] > 0:
				i_delta = val
		else:
			raise Exception("invalid command found: " + cmd)
		
		self.i += i_delta
		
		return False

a = Process(p=0)
b = Process(p=1)
a.linked = b
b.linked = a

print("starting processes a and b")

while a.i in range(len(program)) and b.i in range(len(program)):
	a_locked = a.evaluate()
	b_locked = b.evaluate()
	if a_locked and b_locked:
		print("deadlocked!")
		break

print("finished processing!")
print("program 0 sent " + str(a.sent) + " values")
print("program 1 sent " + str(b.sent) + " values")
