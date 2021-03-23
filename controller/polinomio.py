def add_polynom(arr):
    result = ""

    for idx, val in reversed(list(enumerate(reversed(arr)))):
        aux = int(val[0]) + int(val[1])
        result += str(aux) + "x^" + str(idx) + " "

    return result


def product_polynom(arr):
    result = ""
    aux = []

    for inx, val in enumerate(arr):
        for j in arr:
            aux.append(arr[inx][0] * j[1])

    for idx, val in reversed(list(enumerate(reversed(aux)))):
        result += str(val) + "x^" + str(idx) + " "

    return result