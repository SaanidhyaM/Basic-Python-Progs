def fun1():
    x=100
    def fun2():
        nonlocal x
        x=200
    print(str(x))
    fun2()
    print(str(x))
x=50
fun1()
print(str(x))

