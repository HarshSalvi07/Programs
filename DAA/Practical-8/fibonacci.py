def fibonacci(n):
    if n < 0:
        return False
    if n <= 1:
        return n
    return fibonacci(n-2) +fibonacci(n-1)

n=int(input("Enter the number for Fibonacci Series: "))
for i in range(0,n+1):
    print(fibonacci(i),end=" ")
