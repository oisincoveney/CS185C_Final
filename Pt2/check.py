def accuracy(predicted, expected):
    correct = 0
    for i in range(len(predicted)):
        if predicted[i] == expected[i]:
            correct += 1

    return correct / len(predicted)
