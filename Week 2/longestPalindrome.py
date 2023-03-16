#Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
#Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

#Example 1:
#Input: s = "abccccdd"
#Output: 7
#Explanation: 
#One longest palindrome that can be built is "dccaccd", whose length is 7.

def longestPalindrome(s: str) -> int:
        #Create a dictionary
        dictionary = {}

        #Key -> Letter 
        #Value -> Numbrer of times it repeats on the string

        #Creare maxiumum length variable
        maximum = 0
        foundAPair = False

        #For each character in the string
        for char in s:
            #Check if character in dictionary
            #If character not in dictionary create a key->value element
            if char not in dictionary:
                dictionary[char] = 1
            #If character in dictionary add one to the quantity it repeats
            else:
                dictionary[char] += 1

        
        for element in dictionary:
            #If the value on the dictionary is divisible by 2 means it can be palindomre
            #so we automatically add it to the maximum value
            if dictionary[element] % 2 == 0:
                maximum = maximum + dictionary[element]
            #If the value on the dictionary is divisible by 3 we add the part that is a pair and         
            #record that we have found a pair
            elif dictionary[element] % 2 == 1:
                foundAPair = True
                maximum = maximum + dictionary[element]-1
        
        if foundAPair == True:
            return maximum + 1
        else:
          return maximum

def main():
    print(longestPalindrome("abccccdd"))
  
main()

