input = open("4.in")

valid = 0
for line in input:
	words = str(line).split()
	words = ["".join(sorted(word)) for word in words]
	if len(set(words)) == len(words):
		print(" ".join(words) + " is a valid passphrase")
		valid += 1
	else:
		print(" ".join(words) + " is NOT a valid passphrase")
		
print("there are " + str(valid) + " valid passphrases")