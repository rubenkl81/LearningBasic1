num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))


def sum_up(n1, n2):
    value = n1 + n2
    if value in range(15, 20):
        return 20
    else:
        return value


print(sum_up(num1, num2))
