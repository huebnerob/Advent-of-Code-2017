instructions = open("8.in").readlines()

memory = {}

def ensure_exists(register):
	if register in memory:
		return
	memory[register] = 0

def check_condition(register, operator, value):
	ensure_exists(register)
	reg_val = memory[register]
	return {
		'>': lambda x: reg_val > x,
		'<': lambda x: reg_val < x,
		'==': lambda x: reg_val == x,
		'!=': lambda x: reg_val != x,
		'>=': lambda x: reg_val >= x,
		'<=': lambda x: reg_val <= x
	}[operator](value)

max_mem_during = -999999

def execute_command(register, operator, value):
	global max_mem_during
	ensure_exists(register)
	delta = value if operator == "inc" else -value
	print("changing register " + register + " from " + str(memory[register]) + " to " + str(memory[register] + delta))
	memory[register] += delta 
	max_mem_during = max(max_mem_during, memory[register])

for ins in instructions:
	tok = ins.strip().split(" ")
	if check_condition(tok[4], tok[5], int(tok[6])) == True:
		print("EVAL: " + ins.strip())
		execute_command(tok[0], tok[1], int(tok[2]))
	else:
		print("PASS: " + ins.strip())
		
max_mem = -99999
for m in memory:
	max_mem = max(max_mem, memory[m])
print("max mem is " + str(max_mem))
print('max mem during is ' + str(max_mem_during))