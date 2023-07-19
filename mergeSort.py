import time

grad = [
   '#6b71f5',
    '#b1c8ed'
]
grad_green = [
    '#C21010',
    '#E64848'
]
swaps = 0


def merge_sort(data, drawData, timeTick):
    merge_sort_alg(data, 0, len(data) - 1, drawData, timeTick)


def merge_sort_alg(data, left, right, drawData, timeTick):
    if left < right:
        middle = (left + right) // 2
        merge_sort_alg(data, left, middle, drawData, timeTick)

        merge_sort_alg(data, middle + 1, right, drawData, timeTick)

        merge(data, left, middle, right, drawData, timeTick)
    if data == sorted(data):
        drawData(data, [grad[x % 2] for x in range(len(data))])


def merge(data, left, middle, right, drawData, timeTick):
    drawData(data, getColorArray(len(data), left, middle, right))
    time.sleep(timeTick)

    leftPart = data[left:middle + 1]
    rightPart = data[middle + 1: right + 1]

    leftIdx = rightIdx = 0

    for dataIdx in range(left, right + 1):
        if leftIdx < len(leftPart) and rightIdx < len(rightPart):
            if leftPart[leftIdx] <= rightPart[rightIdx]:
                data[dataIdx] = leftPart[leftIdx]
                leftIdx += 1
            else:
                data[dataIdx] = rightPart[rightIdx]
                rightIdx += 1

        elif leftIdx < len(leftPart):
            data[dataIdx] = leftPart[leftIdx]
            leftIdx += 1
        else:
            data[dataIdx] = rightPart[rightIdx]
            rightIdx += 1

    drawData(data, [grad[0] if left <= x <= right else "#cccccc" for x in range(len(data))], swaps)
    time.sleep(timeTick)


# def getColorArray(leght, left, middle, right):
#     colorArray = []
#
#     for i in range(leght):
#         if i >= left and i <= right:
#             if i >= left and i <= middle:
#                 colorArray.append(grad[0])
#             else:
#                 colorArray.append(grad[1])
#         else:
#             colorArray.append("#CCCCCC")
#
#     return colorArray

def getColorArray(lenght, left, mid, right):
    colorArray = []
    # mid = (left + right) // 2

    for i in range(lenght):
        if left <= i <= right:
            if left <= i <= mid:
                colorArray.append(grad_green[0])
            else:
                colorArray.append(grad_green[1])
        else:
            colorArray.append("#cccccc")
    return colorArray
