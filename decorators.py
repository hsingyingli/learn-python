

def start_end_decorator(func):
    def wrapper(*args, **kwargs):
        print("Start")
        res = func(*args, **kwargs)
        print("End")
        return res
    return wrapper


@start_end_decorator
def add(x):
    return x + 5



print(add(10))


def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper
    return decorator_repeat




@repeat(num_times = 4)
def greet(name):
    print(f'Hello {name}')

greet('aaron')
