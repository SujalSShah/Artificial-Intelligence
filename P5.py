import random
import math

# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Derivative of sigmoid
def sigmoid_derivative(y):
    return y * (1 - y)

# Training data for AND gate
X = [(0,0), (0,1), (1,0), (1,1)]
Y = [0, 0, 0, 1]

# Initialize weights and bias randomly
w1 = random.random()
w2 = random.random()
b = random.random()

learning_rate = 0.5

# Training
for epoch in range(5000):
    for i in range(len(X)):
        x1, x2 = X[i]
        target = Y[i]

        # Forward pass
        net = x1*w1 + x2*w2 + b
        output = sigmoid(net)

        # Error
        error = target - output

        # Backpropagation
        delta = error * sigmoid_derivative(output)

        # Update weights and bias
        w1 += learning_rate * delta * x1
        w2 += learning_rate * delta * x2
        b += learning_rate * delta

# Testing
print("Testing AND Gate")
for x1, x2 in X:
    net = x1*w1 + x2*w2 + b
    output = sigmoid(net)
    print((x1, x2), "->", round(output, 3))