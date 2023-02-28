def isValid(s):
  #Create stack
  stack = []
  #Create dictionary
  dict = {")":"(", "]":"[", "}":"{"}
    
  #For each character in the string
  for char in s:
    #If character is an opening parenthesis
    if char in dict.values():
      #Add into the stack
      stack.append(char)

   #If character is a closing parenthesis
    elif char in dict.keys():
      #If there is no complementing bracket (stack empty) and we have
      # a closing parenthesis pending
      #Or the opening parenthesis that matches our character is not
      # in the top of the stack
      if stack == [] or dict[char] != stack.pop():
        return False
       
  #If stack is is empty means there is no bracket pending to close
  return stack == []

def main():
  print(isValid("[]"))

main()