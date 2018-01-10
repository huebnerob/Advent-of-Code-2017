class Node():
	def __init__(self, string):
		comps = string.split(" ", maxsplit = 3)
		self.name = comps[0]
		self.weight = int(comps[1].strip('\n').strip('()'))
		if len(comps) == 4:
			self.children = comps[3].strip().replace(',', '').split(" ")
		else:
			self.children = []
		self.child_nodes = []

input = open("7.in")

leaves = []
tree = []

root_node = None

for node_string in input:
	node = Node(node_string)
	if len(node.children) > 0:
		tree += [node]
	else:
		leaves += [node]

print("\nfound " + str(len(leaves)) + " leaf nodes and " + str(len(tree)) + " internal nodes")

def find_parent_for_node(child):
	global root_node
	for parent in tree:
		if child.name in parent.children:
			print(child.name + " has parent " + parent.name)
			parent.child_nodes += [child]
			return
	# no parent found
	root_node = child

for n in leaves:
	find_parent_for_node(n)

for n in tree:
	find_parent_for_node(n)

print("\nprocessed all parent-child relationships, found root node named: " + root_node.name if root_node != None else "Error: root node not found")

print("\nstarting cumulative weight calculation\n")

def calc_cumu_weight(node):
	cumu_weight = node.weight
	for c in node.child_nodes:
		cumu_weight += calc_cumu_weight(c)
	node.cumu_weight = cumu_weight
	print(node.name + " has cumulative weight " + str(cumu_weight))
	return cumu_weight

calc_cumu_weight(root_node)

print("\nchecking for imbalances\n")

def preorder(node, processor):
	processor(node)
	for n in node.child_nodes:
		preorder(n, processor)

def check_imbal(node):
	weights = [n.cumu_weight for n in node.child_nodes]
	if len(weights) < 2:
		return
	imbal = False
	check = weights[0]
	for w in weights:
		if w != check:
			imbal = True
	if imbal == False:
		return
	print(node.name + " has child cumu weights of " + ' '.join([str(w) for w in weights]))

preorder(root_node, check_imbal)