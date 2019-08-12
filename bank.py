
net = 0

while True:
	line = raw_input("> ").split()
	if not line:
		break;
		
	amt = int(line[1])
	if line[0] == 'D':
		net += amt
	elif line[0] == 'W':
		net -= amt

print net
