import time

grad = [
'#6b71f5',
    '#b1c8ed'
]
grad_ = [
    '#5BB318',
    '#2B7A0B'
]
swaps = 0


def partition(data, head, tail, draw, timeTick):
    global swaps
    border = head
    pivot = data[tail]

    draw(data, getclr(len(data), head, tail, border, border), swaps)
    time.sleep(timeTick)
    for j in range(head, tail):
        if data[j] < pivot:
            draw(data, getclr(len(data), head, tail, border, j, True), swaps)
            time.sleep(timeTick)
            swaps += 1
            data[border], data[j] = data[j], data[border]
            border += 1
            time.sleep((timeTick))
        draw(data, getclr(len(data), head, tail, border, j), swaps)
        time.sleep(timeTick)
    # draw(data, [grad_green[0] if x == data[border] or x == data[tail] else grad[x % 2] for x in range(len(data))])
    swaps += 1
    draw(data, getclr(len(data), head, tail, border, tail, True), swaps)
    time.sleep(timeTick)
    data[border], data[tail] = data[tail], data[border]
    return border


def quick_sort(data, head, tail, draw, timeTick):
    global swaps
    if head < tail:
        pi = partition(data, head, tail, draw, timeTick)

        quick_sort(data, head, pi - 1, draw, timeTick)
        quick_sort(data, pi + 1, tail, draw, timeTick)

    if data == sorted(data):
        draw(data, [grad[x % 2] for x in range(len(data))], swaps)
        swaps = 0


def getclr(datalen, head, tail, border, currindx, swaping=False):
    colors = []
    for i in range(datalen):
        if head <= i <= tail:
            colors.append(grad[i % 2])
        else:
            colors.append("#CCCCCC")

        if i == tail:
            colors[i] = grad_[0]
        elif i == border:
            colors[i] = grad_[1]
        elif i == currindx:
            colors[i] = '#FEC260'

        if swaping:
            if i == border or i == currindx:
                colors[i] = '#EB1D36'
    return colors
