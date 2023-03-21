def twoSum(nums, target):
    d = {}
    for i in range(len(nums)):
      r = target - nums[i]
      if r in d: 
        return [d[r], i]
      d[nums[i]] = i
		

def main():
    nums = [2,7,11,15]
    target = 9
    print(twoSum(nums, target))

main()