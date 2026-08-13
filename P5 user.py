import math

# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + math.exp(-x))


# Derivative of sigmoid
def sigmoid_derivative(y):
    return y * (1 - y)


# AND gate training data
X = [(0, 0), (0, 1), (1, 0), (1, 1)]
Y = [0, 0, 0, 1]


# ---------------------------------
# USER INPUT: Initial weights
# ---------------------------------

w1 = float(input("Enter initial weight w1: "))
w2 = float(input("Enter initial weight w2: "))
b = float(input("Enter initial bias b: "))

learning_rate = 0.5


# ---------------------------------
# TRAINING
# ---------------------------------

for epoch in range(5000):

    for i in range(len(X)):

        x1, x2 = X[i]
        target = Y[i]

        # Forward pass
        net = x1 * w1 + x2 * w2 + b
        output = sigmoid(net)

        # Error
        error = target - output

        # Backpropagation
        delta = error * sigmoid_derivative(output)

        # Update weights and bias
        w1 += learning_rate * delta * x1
        w2 += learning_rate * delta * x2
        b += learning_rate * delta


# ---------------------------------
# FINAL TRAINED VALUES
# ---------------------------------

print("\nTraining completed.")
print("Final w1 =", round(w1, 4))
print("Final w2 =", round(w2, 4))
print("Final bias =", round(b, 4))


# ---------------------------------
# USER INPUT FOR TESTING
# ---------------------------------

print("\nEnter values for testing AND gate")

x1 = int(input("Enter x1 (0 or 1): "))
x2 = int(input("Enter x2 (0 or 1): "))


# Forward pass using trained weights
net = x1 * w1 + x2 * w2 + b

output = sigmoid(net)


# Prediction
if output >= 0.5:
    prediction = 1
else:
    prediction = 0


# ---------------------------------
# DISPLAY CALCULATION
# ---------------------------------

print("\nFinal Calculation")
print("------------------")

print("x1 =", x1)
print("x2 =", x2)

print("Net =", round(net, 4))
print("Sigmoid Output =", round(output, 4))

print("Predicted AND Output =", prediction)
