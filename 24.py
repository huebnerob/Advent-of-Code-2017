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
	
def strength(bridge):
	return sum([m.a + m.b for m in bridge])

def strongest_bridge(existing, next_port):
	strongest = existing
	max_strength = strength(strongest)
	for member in filter(lambda x: x not in existing, members):
		bridge = None
		if member.a == next_port:
			bridge = strongest_bridge(existing + [member], member.b)
		elif member.b == next_port:
			bridge = strongest_bridge(existing + [member], member.a)
		if bridge != None:
			new_strength = strength(bridge)
			if new_strength > max_strength:
				strongest = bridge
				max_strength = new_strength
	return strongest

def longest_strongest_bridge(existing, next_port):
	strongest = existing
	max_strength = strength(strongest)
	max_len = len(strongest)
	for member in filter(lambda x: x not in existing, members):
		bridge = None
		if member.a == next_port:
			bridge = longest_strongest_bridge(existing + [member], member.b)
		elif member.b == next_port:
			bridge = longest_strongest_bridge(existing + [member], member.a)
		if bridge != None:
			new_strength = strength(bridge)
			new_len = len(bridge)
			if new_len > max_len or (new_len == max_len and new_strength > max_strength):
				strongest = bridge
				max_strength = new_strength
				max_len = new_len
	return strongest

strongest = longest_strongest_bridge([], 0)

print(strength(strongest))

# 1647 is too low for part A

# 1906 is too high for part B