def maxmin(array):
    if len(array) == 1:
        max = array[0]
        min = array[0]
    else:
        if array[1] > array[0]:
            max = array[1]
            min = array[0]
        else:
            max = array[0]
            min = array[1]

        for num in array[2:]:
            if num > max:
                max = num
            if num < min:
                min = num

    return [min, max]
