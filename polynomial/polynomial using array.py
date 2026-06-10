degree = int(input("Enter degree of polynomial: "))

poly = [0] * (degree + 1)

for i in range(degree, -1, -1):
    poly[i] = int(input(f"Enter coefficient of x^{i}: "))

print("\nPolynomial = ", end="")

for i in range(degree, -1, -1):
    if poly[i] != 0:
        print(f"{poly[i]}x^{i}", end=" ")
        if i != 0:
            print("+", end=" ")