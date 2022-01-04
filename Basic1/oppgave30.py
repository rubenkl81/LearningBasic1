base = float(input("input base: "))
heigth = float(input("input heigth: "
                     ""))


def cal_area(b, h):
    area = 0.5 * b * h
    return area


print("The area of the triangle is " + str(cal_area(base, heigth)))
