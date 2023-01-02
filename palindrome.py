def palindrome(word):
    """Checks whether a word is a palindrome"""
    reversed_word = word[::-1]
    if (word == reversed_word):
     print("Паліндром")
    else:
     print("Непаліндром")   

word = "анна"
palindrome(word)