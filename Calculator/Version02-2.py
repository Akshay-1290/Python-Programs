print("Equation 1: a1x + b1y = c1")

a1 = float(input("Enter a1: "))
b1 = float(input("Enter b1: "))
c1 = float(input("Enter c1: "))

print("\nEquation 2: a2x + b2y = c2")

a2 = float(input("Enter a2: "))
b2 = float(input("Enter b2: "))
c2 = float(input("Enter c2: "))

d = (a1 * b2) - (a2 * b1)

if d == 0:
    print("\nThe equations have no unique solution.")
else:
    x = ((c1 * b2) - (c2 * b1)) / d
    y = ((a1 * c2) - (a2 * c1)) / d

    print("\nSolution:")
    print("x =", x)
    print("y =", y)