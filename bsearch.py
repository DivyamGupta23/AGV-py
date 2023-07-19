import time

from tkinter import *
from tkinter import font

grad = [
'#6b71f5',
    '#b1c8ed'
]


def binarySearch(arr, l, r, x, draw, timeTick):
    while l <= r:

        mid = l + (r - l) // 2
        draw(arr, getclr(len(arr), l, r, True), 0)
        time.sleep(timeTick)
        if arr[mid] == x:
            draw(arr, getclr(len(arr), l, r, False), 0)
            return mid


        elif arr[mid] < x:
            l = mid + 1
            draw(arr, getclr(len(arr), l, r, x=True), 0)
            time.sleep(timeTick)

        else:
            r = mid - 1
            draw(arr, getclr(len(arr), l, r, x=True), 0)
            time.sleep(timeTick)
    return -1


def getclr(datalen, l, r, x=False):
    colors = []
    mid = l + (r - l) // 2
    for i in range(datalen):
        # print("error")
        # if l <= i <= r:
        if i == mid:
            if x:
                colors.append('#E64848')
            else:
                colors.append('#5BB318')
        elif mid > i > l or mid < i < r:
            colors.append("#cccccc")
        else:
            colors.append(grad[i%2])

    return colors
