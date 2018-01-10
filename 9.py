import re

#input = "{{<!!>},{<!!>},{<!!>},{<!!>}}"
input = open("9.in").read()

print("original input:")
print(input)
print()

# 1. remove all 'escaped' characters
escaped_regex = r'!.'
input = re.sub(escaped_regex, "", input)

print("after removing escaped:")
print(input)
print()

# 2. remove and count all garbage
garbage_regex = r'<.*?>'
garbage_len = 0
def counter(m):
	global garbage_len
	garbage_len += len(m.group(0))-2
	return ""
input = re.sub(garbage_regex, counter, input)

print("after removing garbage:")
print(input)
print()

# 3. remove commas
garbage_regex = r','
input = re.sub(garbage_regex, "", input)

print("after removing commas:")
print(input)
print()

# 4. count groups

level = 0
total = 0
for c in input:
	if c == '{':
		level += 1
	elif c == '}':
		print('adding group of level ' + str(level))
		total += level
		level -= 1
	else:
		raise ValueError()

print("groups level sum is " + str(total))
print('removed ' + str(garbage_len) + " garbage")
