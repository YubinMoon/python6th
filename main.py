# 암시적 타입 변환
a = 5
b = 2
print(b, type(b))
value = a / b
print(value, type(value))

x = 10
y = 5.5
total = x + y
print(total, type(total))

j = "Hello"
k = "like lion"
p = j + k
print(p, type(p))

## TypeError: unsupported operand type(s) for +: 'int' and 'str'
# q = 20
# u = "10"
# r = q + u
# print(r, type(r))
