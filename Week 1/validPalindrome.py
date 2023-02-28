
def isPalindrome(s):
      s = s.lower()
      final = ""
      for char in s:
        if char.isalnum() == True:
          final = final + char

      reversedFinal = final[::-1]

      if final == reversedFinal:
        return True
      else: return False

def main():
  s = "0P"
  print(isPalindrome(s))

main()