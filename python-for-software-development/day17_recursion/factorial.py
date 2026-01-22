def sum_numbers(n):
    if n == 0:          # base case
        return 0
    else:
        return n + sum_numbers(n - 1)

num = 5
print("Sum of first", num, "numbers is:", sum_numbers(num))
