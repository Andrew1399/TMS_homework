def palindromes():
    values = ["demigod", "rewire", "madam",
               "fortran", "python", "xamarin", "salas", "PHP"]
    palindrome = list(filter(lambda x: (x.lower() == "".join(reversed(x.lower()))), values))
    print(palindrome)

if __name__ == '__main__':
    palindromes()