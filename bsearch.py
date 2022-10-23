import time

grad = [
    '#60A3D9',
    '#0074B7'
]


def binarySearch(arr, l, r, x, draw, timeTick):
    while l <= r:

        mid = l + (r - l) // 2
        draw(arr, getclr(len(arr), mid, x))
        time.sleep(timeTick)
        if arr[mid] == x:
            return mid


        elif arr[mid] < x:
            l = mid + 1
            draw(arr, getclr(len(arr), mid=l + (r - l) // 2, x=x))
            time.sleep(timeTick)

        else:
            r = mid - 1
            draw(arr, getclr(len(arr), mid=l + (r - l) // 2, x=x))
            time.sleep(timeTick)
    return -1


def getclr(datalen, mid, x):
    colors = []
    for i in range(datalen):
        if i == mid:
            colors.append('yellow')
        else:
            colors.append(grad[i % 2])

    return colors
