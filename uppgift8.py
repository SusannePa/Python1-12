# Uppgift 8
# Skapa en funktion count_letters(string) som returnerar en dictionary med varje bokstav som nyckel och antalet förekomster som värde.

"""
def test_funktion():
    assert count_letters("hello") == {"h": 1, "e": 1, "l": 2, "o": 1}
    assert count_letters("") == {}
    assert count_letters("aaa") == {"a": 3}
"""

def count_letters(string: str) -> dict:
    """
    Returnerar en dictionary med varje bokstav som nyckel och antalet förekomster som värde.
    """
    letter_count = {}
    for letter in string:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count

#def test_funktion():
print(count_letters("Susanne"))
 
