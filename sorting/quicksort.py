# Quick Sort Algorithm
# Lomuto partition scheme

def quicksort(a, lo, hi):
    if lo < hi:
        p = partition(a, lo, hi)
        quicksort(a, lo, p - 1)
        quicksort(a, p + 1, hi)
    return a


def partition(a, lo, hi):
    pivot = a[hi]
    i = lo
    for j in range(lo, hi + 1, 1):
        if a[j] < pivot:
            # swap lo with i
            a[i], a[j] = a[j], a[i]
            i = i + 1
    # swap lo with hi
    a[i], a[hi] = a[hi], a[i]
    return i


a = [5, 9, 1, 3, 4, 6, 6, 3, 2]
print(quicksort(a, 0, len(a) - 1))
