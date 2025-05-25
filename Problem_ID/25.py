import numpy as np

def sigmoid(x) :
    return 1 / (1 + np.exp(-x))

def forward(features , weights , bias):
    outputs = np.dot(weights , features.T)
    outputs = outputs + bias
    outputs = np.round(sigmoid(outputs) , 4)
    return outputs

def backprop_weights(weights , features , labels , outputs ,  lr):
    new_weights = np.zeros(weights.size)
    for j in range(weights.size):
        delta_weight = 0.0
        for i in range(outputs.size):
            delta_weight += (outputs[i] - labels[i]) * outputs[i] * (1 - outputs[i]) * features[i][j]

        delta_weight = (2 * delta_weight) / (labels.size)
        new_weights[j] = np.round(weights[j] - lr* delta_weight , 4)

    return new_weights


def backprop_bias(bias , features , labels , outputs , lr):
    delta_bias = 0.0
    for i in range(outputs.size):
        delta_bias += (outputs[i] - labels[i]) * outputs[i] * (1- outputs[i])

    delta_bias = (2 * delta_bias) / (outputs.size)
    new_bias = np.round(bias - lr * delta_bias , 4)

    return new_bias


def train_neuron(features: np.ndarray, labels: np.ndarray, initial_weights: np.ndarray, initial_bias: float, learning_rate: float, epochs: int) -> (np.ndarray, float, list[float]):
	# Your code here
    mse = []
    outputs = forward(features , initial_weights , initial_bias)
    new_weights  = initial_weights.copy()
    new_bias = initial_bias
    for i in range(epochs):
        square = np.square(outputs - labels)
        mse.append(np.round(np.mean(square) , 4))
        new_weights = backprop_weights(new_weights , features , labels , outputs , learning_rate)
        new_bias = backprop_bias(new_bias , features , labels , outputs , learning_rate)
        outputs = forward(features , new_weights , new_bias)
	return new_weights, new_bias, mse
