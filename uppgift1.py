def is_odd(number: int):
    """
    Returnerar True om number är udda, annars False.
    """
    return number % 2 != 0
# Testar med talet 1 , 6 , 4 0ch 7
print(is_odd(1))  
print(is_odd(6))
print(is_odd(4))
print(is_odd(7))
# talet 1 blir True eftersom 1 är udda Tal
# Talet 6 blir False eftersom 6 är ett jämnt tal
# Talet 4 blir False eftersom 4 är ett jämnt tal
# Talet 7 blir True eftersom  7är ett udda Tal