from class_to_label_mapping import mapc
f = open('val_annotations.txt','r')
f1 = open('val_images.txt', 'w')
path = 'val_images/'
line = f.readline()
class_labels = mapc()

while line:
	line = line[:-1]
	tokens = line.split()
	if tokens[1] in class_labels:
		f1.write(path + tokens[0] + ' ' + class_labels[tokens[1]] + '\n')
	line = f.readline()


