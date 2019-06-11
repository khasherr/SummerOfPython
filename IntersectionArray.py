# This programs checks for
def intersection_array(A,B):
    def intersection(arr1, arr2):
        i, j = 0, 0
        while i < m and j < n:
            if arr1[i] < arr2[j]:
                i += 1
            elif arr2[j] < arr1[i]:
                j += 1
            else:
                print(arr2[j])
                j += 1
                i += 1

    m = int(input())
    arr1 = [int(x) for x in input().split()]
    n = int(input())
    arr2 = [int(y) for y in input().split()]
    arr1.sort()
    arr2.sort()
    intersection(arr1, arr2)
