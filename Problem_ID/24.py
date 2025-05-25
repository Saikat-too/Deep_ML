import math

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
	# Your code here
    e = math.e
    output = []
    prob = []
    for i in range(len(features)):
        neuron_sum = 0
        for j in range(len(features[0])):
            neuron_sum += features[i][j] * weights[j]
        neuron_sum += bias
        neuron_sum = 1 / (1 + e** (-neuron_sum))
        neuron_sum = round(neuron_sum , 4)
        output.append(neuron_sum)

    mse = 0

    for k in range(len(output)):
        mse += (labels[k] - output[k]) ** 2


    mse = mse / len(output)

    mse = round(mse , 4)
    # output = f"{output:.4f}"

	return output, mse
