def mapc():
	f = open('mapping.txt','r')
	d = {}
	line = f.readline()
	count = 0
	while line:
		line = line[:-1]
		tokens = line.split()
		d[tokens[0]] = tokens[1]
		line = f.readline()

	return d

