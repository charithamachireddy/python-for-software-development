def is_even(n):
    return n % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]

result = list(filter(is_even, numbers))

print(result)
