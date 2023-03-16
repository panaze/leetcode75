def majorityElement(nums):
        dictionary = {}

        #Fill dictionary with key->number value->Number of times it repeats on the array
        for i in range(len(nums)):
            if nums[i] not in dictionary:
                dictionary[nums[i]] = 1
            else:
                dictionary[nums[i]] += 1
        #Get greatest value of dictionary
        max_value = max(dictionary,key = dictionary.get)

        return max_value

def main():
    print(majorityElement([2,2,1,1,1,2,2]))

main()