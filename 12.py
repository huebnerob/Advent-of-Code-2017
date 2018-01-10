input = open("12.in").readlines()

nodes = {}

for l in input:
	l_s = l.split('<->')
	i = int(l_s[0])
	c = [int(n) for n in l_s[1].strip().split(', ')]
#	print("program " + str(i) + " has neighbors " + str(c))
	nodes[i] = c

def count_tree(start_index, counted = []):
	tree_size = 1
	counted += [start_index]
	for child in nodes[start_index]:
		if child not in counted:
			tree_size += count_tree(child, counted)
	return tree_size

tree_index = 0
while len(nodes) > 0:
	counted = []
	node = list(nodes.keys())[0]
	size = count_tree(node, counted)
	tree_index += 1 
	print("tree " + str(tree_index) + " at " + str(node) + " has a size of " + str(size))
	for n in counted:
		del nodes[n]
	