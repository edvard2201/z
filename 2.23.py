import math
def rectangle_properties(a, b):
perimeter = 2 * (a + b)
diagonal = math.sqrt(a**2 + b**2)
return perimeter, diagonal
a = float(input("2"))
b = float(input("4"))
perimeter, diagonal = rectangle_properties(a, b)
print("{perimeter}")
print("{diagonal:.4f}")