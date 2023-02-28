def twoSum(nums, target):
    for i in range(len(nums)):
      for j in range(i+1,len(nums)):
        if nums[i] + nums[j] == target:
          return [i,j]

def main():
    nums = [3,2,4]
    print(twoSum(nums,6))

main()