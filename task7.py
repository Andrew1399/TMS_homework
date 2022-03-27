def integers():
    values = [6.56773, 9.57668, 4.00914, 56.24241, 9.01344, 32.00013]
    integer = map(lambda x: round(x), values)
    print(list(integer))

if __name__ == '__main__':
    integers()
