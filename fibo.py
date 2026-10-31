n = int(input("Enter the number of iterations : "))

# Non-recursive Fibonacci
print("Non recursive fibonacci series")
a = 0
b = 1
for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c

# Recursive Fibonacci
print("Recursive fibonacci series")
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(n):
    print(fibonacci(i))
    