import cv2
import numpy as np 
def load_val_data():
	
	f = open('val_images.txt','r')
	line = f.readline()
	val_images = []
	val_classes = []
	while line:
		line = line[:-1]
		tokens = line.split()
		img = cv2.imread(tokens[0], 1)
		label = int(tokens[1])
		val_images.append(img)
		val_classes.append(label)
		line = f.readline()

	val_classes = np.array(val_classes)
	val_images = np.array(val_images)

	return (val_images, val_classes)

