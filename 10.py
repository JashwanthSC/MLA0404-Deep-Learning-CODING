age = 4
mileage = 50000

W1 = 2
W2 = 0.0001
b = 1

prediction = W1 * age + W2 * mileage + b

print("Prediction =", prediction)

error = prediction - 15

dW1 = error * age
dW2 = error * mileage

print("Gradient for W1 =", dW1)
print("Gradient for W2 =", dW2)
