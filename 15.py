import sys

test = 0
a = 65 if test else 591
b = 8921 if test else 393
a_f = 16807
b_f = 48271
div = 2147483647
mask = (2**16) - 1
m = 0

print("starting with a = " + str(a) + " and b = " + str(b))

for _ in range(5000000):
	a = (a * a_f) % div
	while a % 4 != 0:
		a = (a * a_f) % div
	b = (b * b_f) % div
	while b % 8 != 0:
		b = (b * b_f) % div
	a_bin = a & mask
	b_bin = b & mask
	if a_bin == b_bin:
		m += 1
		sys.stdout.write(".")

print("\nFound " + str(m) + " matches")
