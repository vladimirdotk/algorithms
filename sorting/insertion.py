from typing import List


def sort(array: List[int]) -> List[int]:
    for index in range(1, len(array)):
        element = array[index]

        while index > 0 and element < array[index - 1]:
            array[index] = array[index - 1]
            index -= 1

        array[index] = element

    return array
