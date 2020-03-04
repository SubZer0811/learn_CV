import numpy as np
import os
import cv2
from keras.models import Sequential
from keras.layers import Dense, Dropout, Conv2D, Flatten, MaxPooling2D


def calc_class(string):

	if(string == 'gate_side'):
		return 0
	if(string == 'gate_mid'):
		return 1
	if(string == 'obstacle'):
		return 2
	if(string == 'bucket'):
		return 3
	else:
		cv2.waitKey()


data = []
labels = []
i = 1
train_path = '/home/subzer0/Documents/AUV_Gate/Images/'

f = open('/home/subzer0/Documents/AUV_Gate/Tags/tags_side.csv')
l = f.readline()
l = f.readline()

while(l is not None):

	if(l == '' or i == 100):
		break
	spl = l.split(sep=',')
	img_path = spl[0]
	# img_path = img_path[1:-1]
	print(i)
	# print(spl[5][1:-2])
	# print(spl[5][:-1])
	# label = [float(spl[1]), float(spl[2]), float(spl[3]), float(spl[4]), calc_class(spl[5][1:-2])]
	label = [float(spl[1]), float(spl[2]), float(spl[3]), float(spl[4]), calc_class(spl[5][:-1])]
	# print(label)
	img_path = train_path + img_path
	# print(img_path)
	img = cv2.imread(img_path)
	# print(img.shape)
	img = cv2.resize(img, (180, 320))
	
	cv2.imshow('img', img)
	# cv2.waitKey(1)
	data.append(img)
	
	labels.append(label)
	# print(label)
	l = f.readline()
	i += 1
	# labels.append(int(imgPath[0]))

print("Done")

data = np.array(data).reshape(-1, 180, 320, 3)
labels = np.array(labels)
data = data / 255.0

# print(data)
# print('labels')
# print(labels)

np.save('data_gate_final.npy', data)
np.save('labels_gate_final.npy', labels)

model = Sequential()

model.add(Conv2D(filters=96, input_shape=data.shape[1:], kernel_size=(11,11), strides=(4,4), padding='valid', activation='relu'))
# Max Pooling
# model.add(MaxPooling2D(pool_size=(2,2), strides=(2,2), padding='valid')
model.add(MaxPooling2D())
# 2nd Convolutional Layer
model.add(Conv2D(filters=256, kernel_size=(5,5), strides=(1,1), padding="same", activation = "relu"))

# Max Pooling
# model.add(MaxPooling2D(pool_size=(2,2), strides=(2,2), padding='valid')
model.add(MaxPooling2D())

# 3rd Convolutional Layer
model.add(Conv2D(filters=384, kernel_size=(3,3), strides=(1,1), padding='valid', activation='relu'))

# 4th Convolutional Layer
model.add(Conv2D(filters=384, kernel_size=(3,3), strides=(1,1), padding='valid', activation='relu'))

# 5th Convolutional Layer
model.add(Conv2D(filters=256, kernel_size=(3,3), strides=(1,1), padding='valid', activation='relu'))
# Max Pooling
# model.add(MaxPooling2D(pool_size=(2,2), strides=(2,2), padding='valid', activation='relu'))
model.add(MaxPooling2D())


# Passing it to a Fully Connected layer
model.add(Flatten())
# 1st Fully Connected Layer
model.add(Dense(4096, input_shape=data.shape[1:], activation='relu'))
# Add Dropout to prevent overfitting
model.add(Dropout(0.4))

# 2nd Fully Connected Layer
model.add(Dense(4096, activation='relu'))
# Add Dropout
model.add(Dropout(0.4))

# 3rd Fully Connected Layer
model.add(Dense(1000, activation='relu'))
# Add Dropout
model.add(Dropout(0.4))

model.add(Dense(5, activation='softmax'))

model.compile(optimizer="adam",
              loss='binary_crossentropy',
              metrics=['accuracy'])

model.summary()

model.fit(data, labels, epochs=25, validation_split=0.2)

model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)

model.save_weights("weights1.h5")