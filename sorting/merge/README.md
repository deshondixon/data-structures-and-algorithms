# Merge Sort

[Merge Sort Code Challenge](https://github.com/deshondixon/data-structures-and-algorithms/blob/main/python/code_challenges/merge_sort.py)

## Challenge
<!-- Description of the challenge -->

- Review the pseudocode below, then trace the algorithm by stepping through the process with the provided sample array. Document your explanation by creating a blog article that shows the step-by-step output after each iteration through some sort of visual.

- Once you are done with your article, code a working, tested implementation of Merge Sort based on the pseudocode provided.

## Whiteboard Process
<!-- Embedded whiteboard image -->

![Merge Sort](./MergeSort.png)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

Big O Notation:

- time - O(n log n) - the array is split in two and sorts each side.
- space - O(n) - it is split into two arrays that are half the size of the original array.

## API
<!-- Description of each method publicly available to your Stack and Queue-->

- Provide a visual step through for each of the sample arrays based on the provided pseudocode
- Convert the pseudocode into working code in your language
- Present a complete set of working tests

## Tests

[Merge Sort Unit Tests](https://github.com/deshondixon/data-structures-and-algorithms/blob/main/python/tests/code_challenges/test_merge_sort.py)

## Solution

    def merge_sort(arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]
            merge_sort(left)
            merge_sort(right)
            i, j, k = 0, 0, 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1
            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1
        return arr

    def merge(left, right):
        i, j = 0, 0
        result = []
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
        return result

## References

- Pseudocode where used as they were provided from today's code challenge instructions.
