input = open("11.in").read().split(',')

tally = {"n": 0, 
	    "s": 0, 
	    "se": 0, 
	    "nw": 0, 
	    "sw": 0, 
	    "ne": 0}

max_dist = 0
i = 0
for step in input:
	tally[step] += 1
	i += 1
	opposite_pairs = [('n','s'), ('se','nw'), ('sw', 'ne')]
	
	for opp in opposite_pairs:
		if tally[opp[0]] > tally[opp[1]]:
			tally[opp[0]] = tally[opp[0]] - tally[opp[1]]
			tally[opp[1]] = 0
		else:
			tally[opp[1]] = tally[opp[1]] - tally[opp[0]]
			tally[opp[0]] = 0

	equivalent_pairs = [('s', 'nw', 'sw'), 
					('sw', 'n', 'nw'), 
					('nw', 'ne', 'n'), 
					('n', 'se', 'ne'), 
					('ne', 's', 'se'), 
					('se', 'sw', 's')]
					
	for eq in equivalent_pairs:
		if tally[eq[0]] > tally[eq[1]]:
			tally[eq[0]] = tally[eq[0]] - tally[eq[1]]
			tally[eq[2]] += tally[eq[1]]
			tally[eq[1]] = 0
		else:
			tally[eq[1]] = tally[eq[1]] - tally[eq[0]]
			tally[eq[2]] += tally[eq[0]]
			tally[eq[0]] = 0
			
	distance = sum(tally.values())
	max_dist = max(max_dist, distance)
	
	print("the quickest path at " + str(i) + " is " + str(distance) + " steps long, max dist is now " + str(max_dist))