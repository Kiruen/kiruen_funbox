import functools


def corpFlightBookings(bookings, n):
    res = [0] * (n + 1)
    diff = [0] * (n + 1)
    for item in bookings:
        i, j = item[0], item[1]
        diff[i] += item[2]
        if j + 1 < len(diff):
            diff[j + 1] -= item[2]
    for i in range(1, len(diff)):
        res[i] = diff[i] + res[i - 1]
    return res[1:]
    # return [diff[i] - diff[i - 1] for i in range(1, len(diff))]


if __name__ == '__main__':
    print(corpFlightBookings([[1, 2, 10], [2, 3, 20], [2, 5, 25]], 5))
