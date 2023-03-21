def palindrome(lst):
    if len(lst) <= 1:
        return True

    if lst[0] == lst[-1]:
        return palindrome(lst[1:-1])
    else:
        return False

# Testing
print(palindrome([1, 2, "Espresso", "Madeline", 2, 1])) 
print(palindrome(['a', True, False, False, True, 'a'])) 
print(palindrome([3])) 
