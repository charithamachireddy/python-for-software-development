def countdown(n):
    if n == 0:          # base case
        print("Done!")
    else:
        print(n)
        countdown(n - 1)

countdown(5)
