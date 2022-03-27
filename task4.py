def ingredients(func):
    def wrapper(*args, **kwargs):
        print('bread')
        func(*args, **kwargs)
        print('salad')
        print('cutlet')
        print('tomato')
    return wrapper
def sandwich(food):
    print(food)

if __name__ == '__main__':
    sandwich = ingredients(sandwich)
    sandwich('ham')
