import numpy as np

def accuracy_score(y_true, y_pred):

    number_of_correct_prediction = 0
    total_number_of_prediction = 0
    accuracy = 0.0

    for num1 , num2 in zip(y_true , y_pred):
        total_number_of_prediction += 1
        if num1 == num2 :
            number_of_correct_prediction += 1


    accuracy = number_of_correct_prediction / total_number_of_prediction

    return accuracy
