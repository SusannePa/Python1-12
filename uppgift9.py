# Uppgift 9
# Skapa en funktion is_palindrome(string) som kontrollerar om en given sträng är ett palindrom (dvs. samma framifrån och bakifrån).
""""
def test_is_palindrome():
    assert is_palindrome("radar") == True
    assert is_palindrome("python") == False
    assert is_palindrome("") == True
"""

def is_palindrome(text: str) -> bool:
    """
    Kontrollerar om en given sträng är ett palindrom (dvs. samma framifrån och bakifrån)
    """
    revText = ''.join(reversed(text))
    if (text == revText):
        return True
    return False
    

print(is_palindrome("anna"))
print(is_palindrome("vicki"))