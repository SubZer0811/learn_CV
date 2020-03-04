import numpy as np


def sigmoid(x):
	return (1/(1+np.exp(-x)))

def sigmoid_der(x):
	return sigmoid(x) * (1 - sigmoid(x))

inputs = np.array([[1, 0, 0],
					[1, 0, 1],
					[0, 0, 1],
					[0, 1, 1]])

outputs = np.array([[1, 1, 0, 0]]).T

np.random.seed(1)

weights = 2 * np.random.random((3, 1)) - 1

print("Random initial weights are : ")
print(weights)

# training #

for iter in range (1000):

	input_layer = inputs

	prod = np.dot(input_layer, weights)
	output = sigmoid(prod)
	
	error = outputs - output
	adjust = error * sigmoid_der(output)

	weights += np.dot(input_layer.T, adjust)


print("Output after training : ")
print(output)

print(weights)