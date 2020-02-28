def swap(i, j, l):
    if i < 0 or j < 0 or i > len(l) or j > len(l):
        raise ValueError("out of range")

    l[i], l[j] = l[j], l[i]

    return


def get_min(l):
    ret = [None, -1]
    for i, n in enumerate(l):
        if ret[0] is None or ret[0] > n:
            ret[0] = n
            ret[1] = i

    return tuple(ret)


def sel_sort(l):
    for i in range(len(l) - 1):
        _, min_i = get_min(l[i:])
        swap(i, i + min_i, l)


if __name__ == "__main__":
    target = [5, 2, 4, 6, 1, 3]
    sel_sort(target)
    print(target)
