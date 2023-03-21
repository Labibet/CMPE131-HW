def double(func):
    def wrapper():
        func()
        print("Let's try that again!")
        func()
    return wrapper


from double import double

@double
def my_func():
    print("Hello, world!")

