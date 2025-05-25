import math

def softmax(scores):

	e = math.e
    prob_sum  = 0
    prob = []
    for i in range(len(scores)):
        prob_sum += e**(scores[i])
    for j in range(len(scores)):
        score = (e**(scores[j])) / prob_sum
        score = f"{score:.4f}"
        prob.append(score)

	return prob
