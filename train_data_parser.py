import numpy as np
import cv2
from class_to_label_mapping import mapc
from random import shuffle

def load_data():
	train_classes = []
	train_images = []
	images_path = []
	class_label = mapc()
	f = open("images.txt",'r')

	line = f.readline()

	while line:
		line = f.readline()
		line = line[:-1]
		if(line.endswith("JPEG")):
			images_path.append(line)
	
	
	shuffle(images_path)
	
	for i in images_path:
		img = cv2.imread(i, 1)
		label = i[12:21]
		train_images.append(img)
		train_classes.append(class_label[label])
		

	train_images = np.array(train_images)
	train_classes = np.array(train_classes)

	return (train_images, train_classes)







