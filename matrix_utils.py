def print_m(m):
	for l in m:
		l_s = ['#' if e else '.' for e in l]
		print(''.join(l_s))
	print()
