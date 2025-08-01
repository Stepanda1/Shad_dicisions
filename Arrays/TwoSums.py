nums = [1,2,3,4,5,6,7]
target = 10

def TwoSums(nums):
    dict = {}
    for i in range(len(nums)):
        if target - nums[i] in dict:
            return [dict[target-nums[i]], i]
        dict[nums[i]] = i
    return None
        
print(TwoSums(nums))