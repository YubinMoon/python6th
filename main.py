# b = (10) # type int
c = (10,)  # type tuple
d = (10, 20, 30, 40)
e = (10, 20, -50, 21.5, "멋쟁이사자")
f = 10, 20, -50, 21.5, "멋쟁이사자"

print(d, e, f, sep="\n")

print(f[0])
print(f[1])
print(f[2])
print(f[3])
print(f[4])
print(f[:3])
print(f[1:4])
print(f[1:])
q = c + f
print(q)
print(f * 5)
print(10 in f)
h = (10, 20, -50, 21)
print(min(h), max(h))
print(h.count(10))
print(h.index(20))
sorted_h = sorted(h)
print(sorted_h)
a = (10, 20, -50)
x, y, z = a
print(x, y, z)

a = 10
b = 20
print(a, b)
a, b = b, a
print(a, b)

list_h = list(h)
print(list_h, type(list_h))
tuple_h = tuple(list_h)
print(tuple_h, type(tuple_h))

nested_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
