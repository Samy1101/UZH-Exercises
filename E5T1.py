def merge(a, b):
    new_list = []
    if len(a) == 0 or len(b) == 0:
        return new_list

    if not len(a) == len(b):
        while len(a) < len(b):
            a.append(a[-1])

        while len(b) < len(a):
            b.append(b[-1])

    new_list = list(zip(a, b))
    return new_list


print(merge([], [5, 6]))
