# def login():
#     print("python")
# login()
#
# def add():
#     x=10
#     y=20
#     c=x+y
#     print(c)
# add()
#
# def login(username,password):
#     print(f"Your username is: {username} and your password is: {password}")
# login("bukku","hyaaaaaaa")

# def add(y):
#     x=10
#     c=x+y
#     print(c)

# def show(name,age):
#     print(f"Name: {name} Age: {age}")
# show(name="Sristy", age=19)

# def show(name,age=19)
#     print()


# def show(*num):
#     z=num[0]+num[1]+num[2]
#     print(z)
# show(5,4,3)


# def add(y):
#     x=10
#     c=x+y
#     print("The sum is",c)
# add(20)


# def sum(numbers):
#     total=0
#     for x in numbers:
#         total +=x
#     return total
# print(sum((8,2,3,0,7)))


# def multiply(numbers):
#     total=1
#     for x in numbers:
#         total *= x
#     return total
# print(multiply((8,2,3,-1,7)))

# def greeter(name):
#     print("Good Morning")
#     print("Hello" + str(name))
# print("Go")
# greeter("World")


# def disp():
#     def show():
#         print("Show Function")
#     print("Disp Function")
#     show()
# disp()

# def disp():
#     def show():
#         return "Show Function"
#     result = show()+"Dis Function"
#     return result
# a=disp()
# print(a)


# def inner():
#     x=4
#     print(x)
# inner()

# y=10
# def outer():
#     z=4
#     def inner():
#         x=10
#         print("x:",x)
#         print('inside the function y:',y)
#     inner()
#     print("x:z")
# outer()

# y=10
# def outer():
#     z=4
#     def inner():
#         x=4
#         nonlocal z
#         z=z+1
#         print(x)
#         print("inside the function y:",y)
#     inner()
#     print()
#     print("z:",z)
# outer()

# y=10
# def inner():
#     x=4
#     print(x)
#     print("inside the function y",y)

# x=10
# def outer():
#     x=4
#     def inner():
#         x=8
#         print(x)
#     inner()
# outer()

# def outer():
#     x="local"
#     def inner():
#         nonlocal x
#         x="nonlocal"
#         print("inner:",x)
#     inner()
#     print("Outer:",x)
# outer()

# result=lambda n1, n2, n3: n1 + n2 +n3
# print("sum of three values:", result(10,20,25))

# result=lambda n1,n2,n3: n1 * n2 * n3
# print("product of three values:", result(10,20,25))
#
# add_sub=lambda x,y:(x+y,x-y)
# a,b=add_sub(5,2)
# print(a)
# print(b)

# li=[5,7,22,97,54,62,77,23,73,61]
# square_list=list(map(lambda x: x**2,li))
# print(square_list)

# a=[1,2,3]
# b=[3,4,5]
# abc=list(map(lambda x,y:x+y,a,b))
# print(abc)

# data=[1,2,3,4,5,5,6,6,7,9,10]
# var=list(filter(lambda x:x%2==0, data))
# print(var)

# from functools import reduce
# li=[5,8,10,20,50,100]
# sum=reduce((lambda x,y:x+y),li)
# print(sum)




