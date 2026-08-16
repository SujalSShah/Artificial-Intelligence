from sklearn.neural_network import MLPClassifier

# AND gate input
X = [[0, 0, 0],
     [0, 0, 1],
     [0, 1, 0],
     [0, 1, 1],
     [1, 0, 0],
     [1, 1, 0],
     [1, 1, 1]]

# AND gate output
y = [0, 0, 0, 0, 0, 0, 1]


# Create neural network
model = MLPClassifier(
    hidden_layer_sizes=(2,),
    activation='logistic',
    solver='lbfgs',
    max_iter=1000,
    random_state=1
)

# Train the network
model.fit(X, y)

# Take input from user
a = int(input("Enter first input (0 or 1): "))
b = int(input("Enter second input (0 or 1): "))
c = int(input("Enter second input (0 or 1): "))

# Predict output
prediction = model.predict([[a, b, c]])

print("AND output =", prediction[0])
