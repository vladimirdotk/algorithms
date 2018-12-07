from typing import List


def bubble_sort(array: List[int]) -> List[int]:
    for _ in range(len(array) - 1):
        
        was_changes = False
        
        for index in range(len(array) - 1):
            if array[index] > array[index+1]:
                array[index], array[index+1] = array[index+1], array[index]
                was_changes = True
        
        if not was_changes:
            break

    return array