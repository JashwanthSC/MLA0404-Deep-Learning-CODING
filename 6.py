W = 2
b = 1
learning_rate = 1.0
dW = -24
db = -6

W_new = W - learning_rate * dW
b_new = b - learning_rate * db

print("Weight =", W_new)
print("Bias =", b_new)
print("Large learning rate may cause unstable training.")
