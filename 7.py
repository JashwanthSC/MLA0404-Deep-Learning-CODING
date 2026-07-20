z = 9

relu = max(0, z)

if z > 0:
    gradient = 1
else:
    gradient = 0

print("ReLU Output =", relu)
print("Gradient =", gradient)
