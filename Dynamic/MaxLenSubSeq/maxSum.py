def maxSum(array):
    sum = 0
    maxSum = 0
    sumArray = []
    maxSumArray = []
    for ii in array:
        if sum + ii >= ii:
            sum += ii
            if sum > maxSum:
                maxSum = sum
        else:
            sum = ii
            if sum > maxSum:
                maxSum = sum
            else:
                pass
            sumArray.append(sum)
            maxSumArray.append(maxSum)
    nums = list()
    for ii in range(len(maxSumArray) - 1, -1, -1):
        if maxSumArray[ii] == sumArray[ii]:
            if len(nums) < 2:
                print "Added to nums"
                nums.append(ii)
            else:
                break
    return maxSum

print maxSum([1, -2, 3, 10, -4, 7, 2, -5])
