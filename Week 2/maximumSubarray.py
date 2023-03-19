#Given an integer array nums, find the subarray with the largest sum, and return its sum.

#Example 1:
#Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
#Output: 6
#Explanation: [4,-1,2,1] has the largest sum = 6.

def maxSubArray(self, nums: List[int]) -> int:
          # Kadane's Algorithm
					newNum = maxTotal = nums[0]        
	
					for i in range(1, len(nums)):
						newNum = max(nums[i], nums[i] + newNum)
						maxTotal = max(newNum, maxTotal)

					return maxTotal	
