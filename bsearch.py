import time

from tkinter import *
from tkinter import font

grad = [
    '#60A3D9',
    '#0074B7'
]


def binarySearch(arr, l, r, x, draw, timeTick):
    while l <= r:

        mid = l + (r - l) // 2
        draw(arr, getclr(len(arr), mid, True), 0)
        time.sleep(timeTick)
        if arr[mid] == x:
            draw(arr, getclr(len(arr), mid, False), 0)
            return mid


        elif arr[mid] < x:
            l = mid + 1
            draw(arr, getclr(len(arr), mid=l + (r - l) // 2, x=True), 0)
            time.sleep(timeTick)

        else:
            r = mid - 1
            draw(arr, getclr(len(arr), mid=l + (r - l) // 2, x=True), 0)
            time.sleep(timeTick)
    return -1


def getclr(datalen, mid, x=False):
    colors = []
    for i in range(datalen):
        if i == mid:
            if x:
                colors.append('#E64848')
            else:
                colors.append('#5BB318')
        elif i == mid - 1 or i == mid - 2 or i == mid + 1 or i == mid + 2:
            colors.append('grey')
        else:
            colors.append(grad[i % 2])

    return colors
