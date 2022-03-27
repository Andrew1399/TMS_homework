# 2, 3
def my_decorator_help(func):
    """Decorator and wrapper."""
    def more_help(*args, **kwargs):
        print('Wait a few seconds')
        func(*args, **kwargs)
        print("Hi, I came back. Let's carry on!")
    return more_help

def helper(name):
    print(name, "one more second please!")
if __name__ == '__main__':
    helper = my_decorator_help(helper)
    helper('Andrew')

