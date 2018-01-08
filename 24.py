class Member():
	def __init__(self, id, a, b):
		self.id = id
		self.a = a
		self.b = b

members = []
lines = open('24.txt').readlines()
for i in range(len(lines)):
	line = lines[i]
	ports = [int(p) for p in line.strip().split('/')]
	members += [Member(i, ports[0], ports[1])]


