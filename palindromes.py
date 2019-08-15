

def checkPalindrome(word):
    backwards = ""
    for letter in word:
        backwards = letter + backwards
    if word == backwards:
        return True
    else:
        return False

test1 = "Hannah"
test2 = "hannah"
test3 = "Patrick"

print(checkPalindrome(test1))
print(checkPalindrome(test2))
print(checkPalindrome(test3))