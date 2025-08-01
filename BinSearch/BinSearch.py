nums = [1,2,6,8,9,12,40,64,80,90,1200]
target = 1200

def BinSearch(nums, target):
    left = 0
    right = len(nums)
    for i in range(len(nums)):
        middle = (left + right) // 2
        if target > nums[middle]:
            left = middle
        else:
            right = middle
        if target == nums[middle]:
            return middle
print(BinSearch(nums,target))
