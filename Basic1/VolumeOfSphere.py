import math

r = float(input("input radius of sphere: "))


def calculate_volume(radius):
    volume = (4 / 3 * (math.pi * r ** 3))
    return volume


print("the volume of a sphere with radius " + str(r) + " is " + str(calculate_volume(r)))
