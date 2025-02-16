def sum_list(numbers:[int]) -> int: # type: ignore
    """
    Returnerar summan av alla siffror i listan.
    """
    total = 0
    for number in numbers:
        total += number
    return total
 # Exempel
numbers = [8, 7, 3, -4, 7,4]
result = sum_list(numbers)
print(result)
# Resultatet blir 25 List[int]