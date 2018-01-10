from time import sleep
input = [4,10,4,1,8,4,9,14,5,1,14,15,0,15,3,5]
iteration = 0
previous_states = [input.copy()]
while True:
	n_max = 0
	i_max = 0
	for i in range(0,len(input)):
		n = input[i]
		if n > n_max:
			n_max = n
			i_max = i
	print("using max value " + str(n_max) + " at index " + str(i_max))
	input[i_max] = 0
	while n_max > 0:
		n_max -= 1
		i_max += 1
		if i_max >= len(input):
			i_max = 0
		input[i_max] += 1
	iteration += 1
	print(str(iteration) + ": " + " ".join([str(n) for n in input]) + "\n")
	if input in previous_states:
		break
	previous_states += [input.copy()]
print("found repeated state after " + str(iteration) + " iterations")
print("cycle is " + str(iteration - previous_states.index(input)) + " cycles long")