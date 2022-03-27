from functools import reduce

def big_number():
    values = [3, 5, 2, 4, 7, 1]
    number = reduce(lambda x, y: x if x > y else y, values)
    print(number)

if __name__ == '__main__':
    big_number()