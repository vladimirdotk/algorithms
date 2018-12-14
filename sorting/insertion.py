from typing import List


def sort(array: List[int]) -> List[int]:
    for index in range(1, len(array)):
        element = array[index]
        pointer = index

        while pointer > 0 and element < array[pointer - 1]:
            array[pointer] = array[pointer -1]
            pointer -= 1

        array[pointer] = element

    return array
