def reverse(arr, end) -> list:
    reversed_arr = [arr[end]]
    if end == 0:
        return reversed_arr
    else:
        reversed_arr.extend(reverse(arr, end - 1))
        return reversed_arr


def insert_sort(arr, end) -> list:
    if end == 0:
        return arr[:1]
    isorted = insert_sort(arr, end - 1)
    for i in range(len(isorted) + 1):
        # if i == len(isorted):
        #     isorted.append(arr[end])
        if i == len(isorted) or arr[end] < isorted[i]:
            isorted.insert(i, arr[end])
            break
    return isorted


def print_i_to_j(arr, i, j, cur=0):
    if i <= cur <= j:
        print(arr[cur], end=' ')
    if cur <= j:
        print_i_to_j(arr, i, j, cur + 1)


if __name__ == '__main__':
    arr = [1, 2, 3]
    print(reverse(arr, len(arr) - 1))

    arr = [3, 1, 5, 2]
    print(insert_sort(arr, len(arr) - 1))
    print_i_to_j(arr, 1, 2)
