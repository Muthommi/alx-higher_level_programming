#!/usr/bin/python3

def find_peak(list_of_integers):
    if not list_of_integers:
        return None

    def find_peak_util(arr, low, high):
        mid = (low + high) // 2
        n = len(arr)

        if (mid == 0 or arr[mid] >= arr[mid - 1]) and \
           (mid == n - 1 or arr[mid] >= arr[mid + 1]):
            return arr[mid]

        elif mid > 0 and arr[mid - 1] > arr[mid]:
            return find_peak_util(arr, low, mid - 1)

        else:
            return find_peak_util(arr, mid + 1, high)

    return find_peak_util(list_of_integers, 0, len(list_of_integers) - 1)
