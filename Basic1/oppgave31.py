num1 = int(input("Enter num 1: "))
num2 = int(input("Enter num 2: "))


def gcd(x, y):
    divisor = 1
    if x % y == 0:
        return y
    for n in range(int(y / 2), 0, -1):
        if x % n == 0 and y % n == 0:
            divisor = n
            break

    return divisor


print("The GCD is " + str(gcd(num1, num2)))
