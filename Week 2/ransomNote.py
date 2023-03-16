#Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
#Each letter in magazine can only be used once in ransomNote.



def canConstruct( ransomNote: str, magazine: str) -> bool:
        
        for c in ransomNote:
             # If there are none of c left in the String, return False.
            if c not in magazine:
                return False
             # Find the index of the first occurrence of c in the magazine.
            location = magazine.index(c)

            # Use splicing to make a new string with the characters 
            # before "location" (but not including), and the characters 
            #after "location". 
            magazine = magazine[:location] + magazine[location + 1:]
        # If we got this far, we can successfully build the note.
        return True

def main():
    print(canConstruct("aa", "aab"))
  
main()