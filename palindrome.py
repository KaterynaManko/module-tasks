def palindrome(word):
    """Checks whether a word is a palindrome"""
    reversed_word = word[::-1]
    return word == reversed_word
        
     
word = "око"
print(palindrome(word))