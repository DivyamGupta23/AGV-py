import time

grad = [
    '#60A3D9',
    '#0074B7'
]
grad_green = [
    '#4B8673',
    '#5FD068'
]


def bubble_sort(data, draw, timeTick):
    for i in range(len(data) - 1):
        for j in range(len(data) - 1 - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                colors = [grad_green[x % 2] if x == j or x == j + 1 else grad[x % 2] for x in range(len(data))]
                draw(data, colors)
                time.sleep(timeTick)


    return data
