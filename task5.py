def decorator(func):
    def say_function_name(*args, **kwargs):
        print('Function: decorator')
        func(*args, **kwargs)
    return say_function_name

def say_name():
    print('Argument: func')

if __name__ == '__main__':
    say_name = decorator(say_name)
    say_name()
