def merge(li1, li2):
    # new list for storing the merged list
    li3 = []
    # while both li1 and li2 are not empty
    while li1 and li2:
        # comparing first element of two lists
        if li1[0] < li2[0]:
            # pop out the first element of li1
            n = li1.pop(0)
            # and append it to li3
            li3.append(n)
        else:
            # pop out the first element of li2
            n = li2.pop(0)
            # and append it to li3
            li3.append(n)
    # while there are some elements still left in li1
    while li1:
        # pop those elements and append to li3
        li3.append(li1.pop(0))
    # while there are some elements still left in li2
    while li2:
        # pop those elements and append to li3
        li3.append(li2.pop(0))
    # return the merged list
    return li3


def merge_sort(nums):
    # if 1 or 0 elements left, recursion should be stopped
    if len(nums) <= 1:
        return nums
    # else divide, and conquer
    else:
        mid = len(nums) // 2
        # merge sort the left half of list
        a1 = merge_sort(nums[:mid])
        # merge sort right half of list
        a2 = merge_sort(nums[mid:])
        # merge the two sorted array and return it
        return merge(a1, a2)


if __name__ == "__main__":
    arr = [3, 6, 45, 1, 20, 0, 34, 2, 1, 343, 56, 67]
    sortedarr = merge_sort(arr)
    print(sortedarr)
