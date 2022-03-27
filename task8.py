def large_numbers():
    scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65, 92, 85]
    numbers = filter(lambda x: x > 80, scores)
    print(list(numbers))

if __name__ == '__main__':
    large_numbers()
