x = input()


def factorial(n):
    string = 1
    for i in range(1, int(n) + 1):
        string *= i
    return int(string)


print(factorial(x))
