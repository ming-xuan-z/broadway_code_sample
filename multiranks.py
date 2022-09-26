from itertools import permutations


def findK(n):
    """Return the length of the output

    Args:
        n (_type_): string
    """
    n = int(n)
    if n == 0:
        return 0
    k = -1
    while n:
        n = n // 2
        k += 1
    return k

def findMedian(vals):
    """return the median of the input list using quickSelect

    Args:
        vals (list): input list 
    """
    n = len(vals)
    if n == 1:
        return vals[0]
    k = n // 2
    def quickSelect(nums, k):
        pivot = nums[0]
        less = [elem for elem in nums if elem < pivot]
        if len(less) == k:
            return pivot
        if len(less) > k:
            return quickSelect(less, k)
        great = [elem for elem in nums if elem > pivot]
        return quickSelect(great, k - len(less) - 1)
    return quickSelect(vals, k)

def deterministicSelect(vals, k):
    """Determinisitic select as described in lecture
    Returns the element of rank k

    Args:
        vals (list): input list
        k (int): rank of the returned element
    """
    partitions = [vals[i:i+5] for i in range(0, len(vals), 5)]
    medians = list(map(findMedian, partitions))
    if len(medians) <= 5:
        pivot = findMedian(medians)
    else:
        middle = len(medians) // 2
        pivot = deterministicSelect(medians, middle)
    less = [elem for elem in vals if elem < pivot]
    if len(less) == k:
        return pivot
    
    if len(less) > k:
        return deterministicSelect(less, k)
    
    great = [elem for elem in vals if elem > pivot]
    return deterministicSelect(great, k - len(less) - 1)

def main(vals, k):
    res = []
    def helper(vals, k):
        nonlocal res
        if k == -1:
            return
        rank = 2**k - 1
        ans = deterministicSelect(vals, rank)
        less = [elem for elem in vals if elem < ans]
        res.append(ans)
        helper(less, k-1)
        return
    helper(vals, k)
    print(" ".join([str(elem) for elem in res[::-1]]))
    return

a = input()
k = findK(a)
print(k)
vals = input().split(' ')
main(vals, k)
