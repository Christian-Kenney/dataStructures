def findMin(nums, x):


    if (x == 1):
        return nums[0]
    return min(nums[x - 1], findMin(nums, x - 1))

def findMax(nums, x):

    if(x == 1):
        return nums[0]
    return max(nums[x - 1], findMax(nums, x - 1))

def reverseList(sen):
    if len(sen) == 0:
        return sen
    else:
        return reverseList(sen[1:]) + sen[0]



if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6]
    sen = "week 3 assignment"
    x = len(nums)
    print(findMin(nums, x))
    print(findMax(nums, x))
    print(reverseList(sen))