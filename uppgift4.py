
def fibonacci(n: int):

    """

    Returnerar en lista med de n första talen i Fibonacci’s talföljd.

    """

    fibonacci_sequence = [0, 1]

   

    for i in range(4, n):  # Detta Börjar från det tredje talet index 4

        next_number = fibonacci_sequence[2] + fibonacci_sequence[3]  # Summan av de två föregående

        fibonacci_sequence.append(next_number)  # Lägger till det nya talet i listan

   

    return fibonacci_sequence[:n]  # Detta Returnera  n första talet i Listan

result = fibonacci(10)
print (result)