num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
num3 = int(input("Enter num3: "))


def calculate_sum(n1, n2, n3):
    sum = 0
    if n1 == n2 or n1 == n3 or n2 == n3:
        return sum
    else:
        sum = n1 + n2 + n3
        return sum


print(calculate_sum(num1, num2, num3))
