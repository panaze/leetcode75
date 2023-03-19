#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

#Example 1:
#Input: nums = [1,2,3,1]
#Output: true

def containsDuplicate(nums):
        
        dictionary = {}

        #Fill dictionary with key ->> unique number, value ->> number of times it appears in array
        for i in range(len(nums)):
            if nums[i] not in dictionary:
                dictionary[nums[i]] = 1
            else:
                return True
        return False

def main():
    print(containsDuplicate([1,2,3,1]))

main()