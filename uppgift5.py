def filtrera_num(numbers):
    """
    Returnerar en lista med alla jämna tal från den givna listan.
    """
    even_numbers = []  # Skapar en tom lista för jämna tal
    for number in numbers:
        if number % 2 == 0:  # Om talen är jämnt
            even_numbers.append(number)  # Ska tallet läggas till i Listan
    return even_numbers
 
numbers = [11, 12, 33, 45, 50, 64, 72, 78, 19, 0]
result = filtrera_num(numbers)
print(result)