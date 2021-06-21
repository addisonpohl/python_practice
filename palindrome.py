def is_palindrome(input_string):
    """Confirms if the input provided is a palindrome by removing capitlization
       and spaces.
    """

    orginal = input_string.lower()

    if " " in orginal:
        orginal = orginal.replace(" ", "")

    reversed = orginal[::-1]

    if orginal == reversed:
        return True
    else:
        return False


print(is_palindrome("Never Odd or Even"))  # Should be True
print(is_palindrome("abc"))  # Should be False
print(is_palindrome("kayak"))  # Should be True
