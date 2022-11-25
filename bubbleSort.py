import time

grad = [
    '#60A3D9',
    '#0074B7'
]
grad_green = [
    '#C21010',
    '#E64848'
]

swaps = 0
def bubble_sort(data, draw, timeTick):
    global swaps
    for i in range(len(data) - 1):
        for j in range(len(data) - 1 - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                colors = [grad_green[x % 2] if x == j or x == j + 1 else grad[x % 2] for x in range(len(data))]
                draw(data, colors, swaps)
                time.sleep(timeTick)
                swaps += 1

    draw(data, [grad[x % 2] for x in range(len(data))], swaps)
    swaps = 0
    return data
