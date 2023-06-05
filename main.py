# 명시적 타입 변환
a = 5
b = 2
value = a / b
print(value, type(value))
int_value = int(value)
print(int_value, type(int_value))

q = 20
u = "10"
print(u, type(u))
r = q + int(u)
print(r, type(r))
r = str(q) + u
print(r, type(r))

n1 = 10.77
vn1 = int(n1)

print(vn1, type(vn1))

n1 = 10
vn1 = complex(n1)
print(vn1, type(vn1))
