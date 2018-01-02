input = open('13.in').readlines()

scanners = {}
sum = 0

def pos_scan(t, l):
	f_len = 2 * l - 2
	p_t = t % f_len
	if p_t > f_len / 2:
		p_t = f_len - p_t
	return p_t

for l in input:
	vals = l.strip().split(': ')
	layer = int(vals[0])
	l_range = int(vals[1])
	print("layer " + str(layer) + " has a range of " + str(l_range))
	scanners[layer] = l_range
	
	if pos_scan(layer, l_range) == 0:
		print("caught!!!")
		sum += layer*l_range

print("sum severity is " + str(sum))

t_offset = 0
for i in range(10000000):
	caught = False
	for layer in scanners.keys():
		range = scanners[layer]
		if pos_scan(layer+i, range) == 0:
			# print("caught!!!")
			caught = True
			break
	if not caught:
		t_offset = i
		break

print("found viable route at delay " + str(t_offset))		
