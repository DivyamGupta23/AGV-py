import time

grad = [
    '#60A3D9',
    '#0074B7'
]
grad_green = [
    '#4B8673',
    '#5FD068'
]


def partition(data, head, tail, draw, timeTick):
    border = head
    pivot = data[tail]

    draw(data, getclr(len(data), head, tail, border, border))
    time.sleep(timeTick)
    for j in range(head, tail):
        if data[j] < pivot:
            draw(data, getclr(len(data), head, tail, border, j, True))
            time.sleep(timeTick)
            data[border], data[j] = data[j], data[border]
            border += 1
            time.sleep((timeTick))
        draw(data, getclr(len(data), head, tail, border, j))
        time.sleep(timeTick)
    # draw(data, [grad_green[0] if x == data[border] or x == data[tail] else grad[x % 2] for x in range(len(data))])

    draw(data, getclr(len(data), head, tail, border, tail, True))
    time.sleep(timeTick)
    data[border], data[tail] = data[tail], data[border]
    return border


def quick_sort(data, head, tail, draw, timeTick):
    if head < tail and data != sorted(data):

        pi = partition(data, head, tail, draw, timeTick)

        quick_sort(data, head, pi - 1, draw, timeTick)
        quick_sort(data, pi + 1, tail, draw, timeTick)

    elif data == sorted(data):
        return


def getclr(datalen, head, tail, border, currindx, swaping=False):
    colors = []
    for i in range(datalen):
        if head <= i <= tail:
            colors.append(grad[i % 2])
        else:
            colors.append("white")

        if i == tail:
            colors[i] = grad_green[0]
        elif i == border:
            colors[i] = grad_green[1]
        elif i == currindx:
            colors[i] = 'yellow'

        if swaping:
            if i == border or i == currindx:
                colors[i] = 'red'
    return colors
