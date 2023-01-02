def palindrome(word):
    """Checks whether a word is a palindrome"""
    letters_list = [letter for letter in word]
    reversed_letters_list = letters_list[::-1]
    if(letters_list==reversed_letters_list):
     return True
    else:
     return False
