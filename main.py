# 덧셈
a = 4
b = 2
total = a + b
print("total = a + b:", total)

# 뺄셈
a = 4
b = 2
total = a - b
print("total = a - b: ", total)

# 곱셈
total = a * b
print("total = a * b: ", total)

# 나눗셈
print("a / b: ", a / b)

# 나머지
a = 5
b = 2
print("a % b: ", a % b)

# 거듭제곱
print("a ** b: ", a**b)

# 몫 (양수)
print("a // b : ", a // b)

# 몫 (음수)
a = -5
print("a // b(음수) :", a // b)

# 비교 연산자
a = 5
b = 2
print("a:", a, "b:", b)

print("a < b: ", a < b)

print("a <= b: ", a <= b)

print("a == b: ", a == b)

print("a != b: ", a != b)

# 논리 연산자
a = 5
b = 2
c = 3
d = 200

print("AND 연산자")
print("a > b and a < c: ", a > b and a < c)
print("b < a < c: ", b < a < c)

print("OR 연산자")
print("a > b or a < c: ", a > b or a < c)

print('NOT 연산자')
print('not(a < b): ', not (a < b))

# 할당 연산자 =
a = 10
b = 20
m = 15

y = a + b
print(y)

m += 10  # m = m + 10
print(m)

m **= 2
print(m)

m //= 10
print(m)

# 비트 연산자 실습
a = 10
b = 15

print("a: ", bin(a))
print("b: ", bin(b))
print("-a: ", bin(-a))
print("a & b: ", bin(a & b))
print('a << 2: ', a << 2)
print('a >> 2: ', a >> 2)

# 멤버 in 연산자
st1 = "Welcome to 멋쟁이 사자"
print("to" not in st1)

st2 = "Welcome top 멋쟁이 사자"
print("to" not in st2)

st3 = "Welcome to 멋쟁이 사자"
print("subs" not in st3)

# is 연산자
a = 10
b = 10
print(a is not b)

a = 10
b = '10'
print(a is not b)
