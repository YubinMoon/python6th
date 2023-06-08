def pw(x, y):
    z = x**y
    print(z)


pw(2, 5)
# pw(5, 2, 3)  # ERROR


def show(name, age=27):
    print(f"Name: {name} Age: {age}")


show(name="멋쟁이사자", age=22)
show(age=22, name="멋쟁이사자")
show("멋쟁이사자")
show("멋쟁이사자", 22)
# show("멋쟁이사자", age=22, roll=12)  # ERROR
