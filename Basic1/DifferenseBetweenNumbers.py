n = int(input("Input your number: "))


def difference(number):
    if number < 17:
        return 17 - number
    else:
        return (number - 17) * 2


print(str(difference(n)))

