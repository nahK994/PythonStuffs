def finucci_number():
    yield 0
    yield 1
    a = 0
    b = 1
    while True:
        yield a+b
        b=a+b
        a=b-a


func = finucci_number()
for i in range(10):
    print(next(func))
