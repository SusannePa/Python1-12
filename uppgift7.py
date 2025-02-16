def validate_password(password):
    """
    Kontrollerar att lösenordet är minst 8 tecken långt och innehåller minst en siffra.
    """
 
    lenPassword = len(password)
    if lenPassword >= 8:
        hasNumber = any(char.isdigit() for char in password)
        if hasNumber == True:
            return True
        else:
            return False
    else:
        return False
    
testPassword = "ABCD1234"
result = validate_password(testPassword)
print(result)
