import numpy as np

data = np.load('data_gate_final.npy', allow_pickle=True)
labels = np.load('labels_gate_final.npy', allow_pickle=True)

print(data.shape)
print(labels.shape)