
str = 'A'
def is_palindrome(s):
  # Write your code here
  # Tip: You may use the code template provided
  left = 0 
  right = len(s) - 1
  i = 1
  if left == right:
    return True
  else: 
    while left < right : 
      if s[left] != s[right]:
          return False
      left = left + 1
      right = right - 1 
      i = i + 1
  return True

# is_palindrome(str)

print(is_palindrome(str))