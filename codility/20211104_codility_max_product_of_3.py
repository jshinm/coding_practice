# A non-empty array A consisting of N integers is given. The product of triplet (P, Q, R) equates to A[P] * A[Q] * A[R] (0 ≤ P < Q < R < N).

# For example, array A such that:

#   A[0] = -3
#   A[1] = 1
#   A[2] = 2
#   A[3] = -2
#   A[4] = 5
#   A[5] = 6
# contains the following example triplets:

# (0, 1, 2), product is −3 * 1 * 2 = −6
# (1, 2, 4), product is 1 * 2 * 5 = 10
# (2, 4, 5), product is 2 * 5 * 6 = 60
# Your goal is to find the maximal product of any triplet.

# Write a function:

# def solution(A)

# that, given a non-empty array A, returns the value of the maximal product of any triplet.

# For example, given array A such that:

#   A[0] = -3
#   A[1] = 1
#   A[2] = 2
#   A[3] = -2
#   A[4] = 5
#   A[5] = 6
# the function should return 60, as the product of triplet (2, 4, 5) is maximal.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [3..100,000];
# each element of array A is an integer within the range [−1,000..1,000].

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    # find two most negative number and three most positive number at most
    # find all products
    # TC: O(N)
    min_neg = [] #there must be minimum negative and maximum negative and evaluate both
    neg = []
    pos = []
    
    for i in A:
        if len(pos) < 3 and i >= 0:
            pos.append(i)
        elif len(neg) < 3 and i < 0:
            neg.append(i)
            min_neg.append(i)
        elif i >= 0:
            for n, j in enumerate(pos):
                if j < i:
                    pos[n] = i
                    break
        elif i < 0:
            for n, j in enumerate(neg):
                if j > i:
                    neg[n] = i
                    break
            for n, j in enumerate(min_neg):
                if j < i:
                    min_neg[n] = i
                    break

    if not pos:
        nums = neg
        nums2 = min_neg
    else:
        nums = neg + pos
        nums2 = min_neg + pos

    top = None

    for num in [nums, nums2]:
        for i, n in enumerate(num[:-2]):
            for j, m in enumerate(num[i+1:-1]):
                for k, o in enumerate(num[i+2:]):
                    tmp = n*m*o

                    if not top or top < tmp:
                        top = tmp
    
    return top

# alternatively there are 4 conditions
# if there are more than 3 pos numbers
    # 1. 3 positive number (3 largest)
# if there are 2 pos numbers
    # 2. 2 smallest product of 2 positive numbers + a smallest negative number
# if there is 1 pos number
    # 3. 1 largest product of 2 negative numbers + a largest positive number
# if there is no pos number
    # 4. smallest negative number