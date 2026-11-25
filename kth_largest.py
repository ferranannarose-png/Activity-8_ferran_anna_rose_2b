# Activity 4: Kth largest

import heapq


def kth_largest(numbers, k):

    if k < 1 or k > len(numbers):
        raise ValueError("Invalid value of k.")

    min_heap = []

    for number in numbers:

        if len(min_heap) < k:
            heapq.heappush(min_heap, number)

        elif number > min_heap[0]:
            heapq.heapreplace(min_heap, number)

    return min_heap[0]



numbers = [7, 2, 9, 4, 15, 6]
k = 3

print("ACTIVITY 4: KTH LARGEST")
print("Numbers:", numbers)
print("K:", k)

answer = kth_largest(numbers, k)

print("Kth largest value:", answer)


sorted_numbers = sorted(numbers, reverse=True)

print("Sorted list:", sorted_numbers)
print("Verification:", sorted_numbers[k - 1])


print("\nADDITIONAL TESTS")
print("1st largest:", kth_largest([8, 3, 5, 1], 1))
print("Last largest:", kth_largest([8, 3, 5, 1], 4))
print("Duplicates:", kth_largest([5, 2, 5, 1, 3], 2))