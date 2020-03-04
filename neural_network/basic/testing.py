import numpy as np
from basic import sigmoid

test_input = np.array([[1, 1, 1]])

weights = np.array([[9.19, -2.29, -4.56]])

test_output = sigmoid(np.dot(test_input, weights.T))

print("Testing Output")
print(test_output)