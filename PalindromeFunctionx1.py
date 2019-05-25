def Palindrome(palindrome_number):
      if  (palindrome_number == palindrome_number[::-1]): #checks if 123 == 321 --- [::-1] just reverses
         return True
      else:
         return False

print(Palindrome('101'))