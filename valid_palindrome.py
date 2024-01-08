
str = 'amanaplanacanalpanama'
def is_palindrome(s):
    # 125. Valid Palindrome
  # Write your code here  
  # Tip: You may use the code template provided
   result_string= re.sub('[^a-zA-Z0-9]','',s).lower()
        print(result_string)
        left = 0
        right = len(result_string) - 1
        i = 1
        if left == right:
            return True
        else: 
            while(left < right):
                if (result_string[left] != result_string[right]):
                    return False
                left = left + 1
                right = right -1 
                i = i + 1
        return True

# is_palindrome(str)

print(is_palindrome(str))