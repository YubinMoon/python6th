def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


runner = fibonacci(10)
print(next(runner))
print(next(runner))
print(next(runner))
for num in runner:
    print(num)
