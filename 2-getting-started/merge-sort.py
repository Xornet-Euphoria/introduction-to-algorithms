# l[a:b]とl[b:c]はソート済と仮定
def merge(l, a, b, c):
    l1 = l[a:b]
    l2 = l[b:c]
    l1_i = 0
    l2_i = 0

    for i in range(c-a):
        if l1_i == len(l1):
            l[a+i] = l2[l2_i]
            l2_i += 1
        elif l2_i == len(l2):
            l[a+i] = l1[l1_i]
            l1_i += 1
        elif l1[l1_i] <= l2[l2_i]:
            l[a+i] = l1[l1_i]
            l1_i += 1
        else:
            l[a+i] = l2[l2_i]
            l2_i += 1


# l[a:b]をソートする
def merge_sort(l, a, b):
    if b - a == 1:
        return
    half = (b - a + 1) // 2
    merge_sort(l, a, a + half)
    merge_sort(l, a + half, b)
    merge(l, a, a + half, b)


if __name__ == "__main__":
    target = [5, 2, 4, 7, 1, 3, 2, 6]

    merge_sort(target, 0, 8)
    print(target)