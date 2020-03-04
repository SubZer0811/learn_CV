import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout
from random import seed, randrange

dataset = np.loadtxt("first_nn_data_1.csv", delimiter=',')
# print(dataset)
X = dataset[:, 0:4]
y = dataset[:, 4]
print(X.shape, y.shape)

model = Sequential()
model.add(Dense(4, input_dim=4, activation='sigmoid'))
# model.add(Dense(12, activation='relu'))
# model.add(Dense(8, activation='relu'))
# model.add(Dense(4, activation='relu'))
# model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(X, y, epochs=700, batch_size=30)
model.save_weights("weights_1.h5")


Xtest = [[80, 50, 10, 50],
		[50, 60, 70, 80],
		[10, 10, 70, 80],
		[50, 50, 50, 50],
		[40, 60, 70, 80],
		[90, 10, 50, 30],
		[11, 22, 33, 44]]

ytest = [1, 1, 0, 0, 1, 0, 0]

Xtest = np.array(Xtest)
ytest = np.array(ytest)

predictions = model.predict(Xtest)
predictions_class = model.predict_classes(Xtest)

print(predictions)
print(predictions_class)