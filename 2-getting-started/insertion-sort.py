def ins_sort(l):
    if len(l) < 2:
        return l

    ret = [l[0]]
    for i, num in enumerate(l):
        if i == 0:
            continue

        j = i - 1
        ret.append(num)
        while j >= 0 and num < ret[j]:
            ret[j + 1] = ret[j]
            ret[j] = num
            j -= 1

    return ret


if __name__ == '__main__':
    target = [5, 2, 4, 6, 1, 3]
    print(ins_sort(target))