def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print()
n=int(input("Enter Number To Compute Factorial: "))
print(factorial(n))
print()
