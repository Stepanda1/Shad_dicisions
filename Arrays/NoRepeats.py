nums = [1,2,3,1]

def repeats(nums):
    dict = {}
    for num in nums:
        if num in dict:
            return True
        else:
            dict[num] = 1
    return False

print(repeats(nums))