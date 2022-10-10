# Write python program that swap two number with temp variable and without temp variable

x = input("Enter value of x: ")
y = input("Enter value of y: ")
temp = x
x = y
y = temp
print("after swapping x :",(x))
print("after swapping y :",(y))

#
x = 5
y = 10
x, y = y, x
print("x =", x)
print("y =", y)


