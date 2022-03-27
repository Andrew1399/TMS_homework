from functools import reduce

def numbers_multiply():
    values = [1, 2, 3, 4]
    multiply = reduce(lambda x, y: x * y, values)
    print(multiply)

if __name__ == '__main__':
    numbers_multiply()