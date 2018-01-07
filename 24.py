for line in open('24.txt').readlines():
	ports = [int(p) for p in line.strip().split('/')]
	print("member with ports " + str(ports[0]) + " and " + str(ports[1]))
