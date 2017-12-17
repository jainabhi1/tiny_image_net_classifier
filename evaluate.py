from __future__ import print_function
from val_data_parser import load_val_data
import keras
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential,model_from_json,load_model
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.models import load_model
import os

num_classes = 50

(x_test, y_test) = load_val_data()
y_test = keras.utils.to_categorical(y_test, num_classes)

x_test = x_test.astype('float32')
# x_train /= 255
x_test /= 255


model = load_model('saved_models/weights-improvement_batch5-33-0.49.hdf5')

scores = model.evaluate(x_test, y_test, verbose=1)

print('Test loss:', scores[0])
print('Test accuracy:', scores[1])
