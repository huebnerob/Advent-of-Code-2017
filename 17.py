test = 0
steps = 3 if test else 370
buffer = [0]
pos = 0
to_insert = 1
last_insert = 50000000
after_zero = 0

while to_insert <= last_insert:
	if to_insert % 100000 == 0:
		print("processing " + str(to_insert))
	pos = (pos + steps) % to_insert + 1
	if pos == 1:
		after_zero = to_insert
	to_insert += 1

# 2nd part answer for 50000 is 15954
print("the number after 0 is " + str(after_zero))
