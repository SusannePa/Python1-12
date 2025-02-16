
# Uppgift 6
# Skapa en funktion multiplication_table(n, limit) som returnerar multiplikationstabellen för n upp till limit i en lista.
# def test_funktion():
    # assert multiplication_table(2, 3) == [2, 4, 6]
    # assert multiplication_table(3, 5) == [3, 6, 9, 12, 15]

def multiplication_table(number: int, limit: int):
    """
    Skriv beskrivning här.
    """
    res = []

    for antal in range(1, limit +1):
        res.append(number * antal)

    return res

print(multiplication_table(3, 4))
