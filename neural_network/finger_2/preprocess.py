import numpy as np
import cv2
import os

data = []
labels = []

i = 0

for imgPath in os.listdir('dataset/train'):

    img = cv2.imread('dataset/train/' + imgPath, 0)
    img = cv2.resize(img, (64, 64)).flatten()

    # print(imgPath)
    data.append(img)

    label = imgPath[-6]
    labels.append(label)
    # print(label)

    print(i)
    i += 1

data = np.array(data, dtype="float") / 255.0
labels = np.array(labels)

print(data.shape)
print(labels.shape)

np.save('data_64x64_gray.npy', data)
np.save('labels_64x64_gray.npy', labels)